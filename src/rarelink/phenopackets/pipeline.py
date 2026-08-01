import json
import logging
import warnings as _warnings
import os
import signal
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional

from rarelink.phenopackets import create_phenopacket
from rarelink.phenopackets.write import write_phenopackets

logger = logging.getLogger(__name__)


class TimeoutException(Exception):
    pass


def timeout_handler(_signum, _frame):
    raise TimeoutException(
        "Pipeline processing exceeded the timeout limit."
    )


@dataclass
class PipelineResult:
    """Structured result returned by phenopacket_pipeline."""
    phenopackets: list = field(default_factory=list)
    failed_creations: List[Dict[str, str]] = field(default_factory=list)
    failed_validations: List[Dict[str, str]] = field(default_factory=list)
    creation_warnings: List[Dict[str, str]] = field(default_factory=list)
    total_records: int = 0

    @property
    def n_created(self) -> int:
        return len(self.phenopackets)

    @property
    def n_failed_creation(self) -> int:
        return len(self.failed_creations)

    @property
    def n_failed_validation(self) -> int:
        return len(self.failed_validations)

def phenopacket_pipeline(
    input_data: list,
    output_dir: str,
    created_by: str,
    mapping_configs: Optional[Dict[str, Any]] = None,
    timeout: int = 3600,
    debug: bool = False,
    progress_callback: Optional[Callable] = None,
    validation_callback: Optional[Callable] = None,
) -> PipelineResult:
    """
    Process input records into Phenopackets in two explicit phases:

      Phase 1 — Create: all records are mapped and built in memory.
      Phase 2 — Write & Validate: write_phenopackets() serializes each one
                to disk and optionally validates it.

    Args:
        input_data:          List of record dicts.
        output_dir:          Directory to write JSON files into.
        created_by:          Creator name for phenopacket metadata.
        mapping_configs:     Mapping configurations for Phenopacket creation.
        timeout:             Wall-clock timeout in seconds (default 3600).
        debug:               Enable verbose debug logging.
        progress_callback:   Optional callable(record_id, success, error)
                             called after each creation attempt.
        validation_callback: Optional callable(file_path, success, error)
                             called after each validation attempt.
                             Forwarded directly to write_phenopackets().

    Returns:
        PipelineResult with created phenopackets and per-stage failure details.
    """
    logging.getLogger("rarelink").setLevel(
        logging.DEBUG if debug else logging.WARNING
    )

    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(timeout)

    result = PipelineResult(total_records=len(input_data))

    try:
        if not mapping_configs:
            raise ValueError("Mapping configurations are required")

        os.makedirs(output_dir, exist_ok=True)

        # ── Phase 1: Create all Phenopackets ──────────────────────────────────
        for record in input_data:
            record_id = record.get("record_id", "unknown")
            try:
                with _warnings.catch_warnings(record=True) as caught:
                    _warnings.simplefilter("always")
                    phenopacket = create_phenopacket(
                        data=record,
                        created_by=created_by,
                        mapping_configs=mapping_configs,
                        debug=debug,
                    )
                record_warnings = [str(w.message) for w in caught]
                result.phenopackets.append(phenopacket)

                for w in record_warnings:
                    result.creation_warnings.append(
                        {"record_id": record_id, "warning": w}
                    )

                if progress_callback:
                    # Pass warnings as error string even on success
                    warn_str = (
                        "\n".join(f"⚠ {w}" for w in record_warnings)
                        if record_warnings else None
                    )
                    progress_callback(record_id, success=True, error=warn_str)
            except Exception as e:
                error_msg = str(e)
                result.failed_creations.append(
                    {"record_id": record_id, "error": error_msg}
                )
                if progress_callback:
                    progress_callback(record_id, success=False, error=error_msg)
                # Guard on the logger, not on the `debug` parameter: the level is
                # already configured above. isEnabledFor avoids serializing the
                # record when debug output is off (the argument would otherwise
                # be evaluated eagerly).
                if logger.isEnabledFor(logging.DEBUG):
                    logger.debug(
                        "Record structure: %s...",
                        json.dumps(record, default=str, indent=2)[:1000],
                    )

        # ── Phase 2: Write & Validate ─────────────────────────────────────────
        def _validation_callback(file_path: str, success: bool, error: Optional[str]):
            if not success:
                result.failed_validations.append(
                    {"file": file_path, "error": error or ""}
                )
            if validation_callback:
                validation_callback(file_path, success=success, error=error)

        write_phenopackets(
            phenopackets=result.phenopackets,
            output_dir=output_dir,
            validate=True,
            validation_callback=_validation_callback,
        )

        # ── Write failure report (only if failures exist) ─────────────────────
        all_failures = [
            {**f, "stage": "creation"} for f in result.failed_creations
        ] + [
            {**f, "stage": "validation"} for f in result.failed_validations
        ]
        if all_failures:
            failure_file = os.path.join(output_dir, "failures.json")
            with open(failure_file, "w") as fh:
                json.dump(all_failures, fh, indent=2)
            logger.debug(f"Failure report written to {failure_file}")

        # ── Write warnings report (only if warnings exist) ────────────────────
        all_warnings = [
            {**w, "stage": "creation"} for w in result.creation_warnings
        ]
        # Prefix warnings will be added by export.py after validation,
        # but pipeline-level warnings are written here.
        if all_warnings:
            warnings_file = os.path.join(output_dir, "warnings.json")
            with open(warnings_file, "w") as fh:
                json.dump(all_warnings, fh, indent=2)
            logger.debug(f"Warnings report written to {warnings_file}")

        return result

    except TimeoutException as te:
        logger.error(f"Timeout occurred: {te}")
        raise
    finally:
        signal.alarm(0)