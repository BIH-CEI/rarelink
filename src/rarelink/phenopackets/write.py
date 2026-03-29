import json
import logging
from pathlib import Path
from typing import Callable, Optional

from google.protobuf.json_format import MessageToDict
from phenopackets import VitalStatus as VitalStatusEnum

from rarelink.phenopackets.validate import validate_phenopackets

logger = logging.getLogger(__name__)


def write_phenopackets(
    phenopackets: list,
    output_dir: str,
    validate: bool = True,
    validation_callback: Optional[Callable] = None,
) -> None:
    """
    Serialize Phenopackets to JSON files (Phenopacket v2 spec)
    and optionally validate each one after writing.

    Args:
        phenopackets:        List of Phenopacket protobuf objects.
        output_dir:          Directory to write JSON files into.
        validate:            Run validation after each write. Defaults to True.
        validation_callback: Optional callable(file_path, success, error)
                             called after each validation attempt.
                             Allows the pipeline to drive progress bars.
    """
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    for phenopacket in phenopackets:
        full = MessageToDict(
            phenopacket,
            preserving_proto_field_name=False,
            including_default_value_fields=False,
        )

        # 2) Extract the raw integer enum value for vital status.
        raw_status_int = phenopacket.subject.vital_status.status

        # 3) Map back to the enum name string.
        try:
            status_name = VitalStatusEnum.Status.Name(raw_status_int)
        except Exception:
            status_name = "UNKNOWN_STATUS"

        # 4) Overwrite the vitalStatus block with just {"status": name}.
        if "subject" in full:
            full["subject"]["vitalStatus"] = {"status": status_name}

        # 5) Write to disk.
        file_path = output_path / f"{phenopacket.id}.json"
        with open(file_path, "w") as f:
            json.dump(full, f, indent=2)
        logger.debug(f"Written: {file_path}")

        # 6) Optionally validate after writing.
        if validate:
            try:
                success, details = validate_phenopackets(file_path)
                if success:
                    logger.debug(f"Validation passed: {file_path}")
                    if validation_callback:
                        validation_callback(
                            str(file_path), success=True, error=None
                        )
                else:
                    logger.warning(
                        f"Validation failed for {file_path}: {details}"
                    )
                    if validation_callback:
                        validation_callback(
                            str(file_path), success=False, error=details
                        )
            except Exception as e:
                error_msg = str(e)
                logger.warning(f"Validation error for {file_path}: {error_msg}")
                if validation_callback:
                    validation_callback(
                        str(file_path), success=False, error=error_msg
                    )