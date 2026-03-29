# src/rarelink/phenopackets/validate.py
import json
import re
import shutil
import subprocess
from pathlib import Path
from typing import List, Tuple, Union
import logging

from rarelink.phenopackets.adapter.ontology_routing_adapter import (
    check_prefix_placement,
)

logger = logging.getLogger(__name__)

_REQUIRED_TOP_LEVEL = {"id", "metaData"}
_REQUIRED_METADATA = {"created", "createdBy", "phenopacketSchemaVersion"}
_CURIE_PATTERN = re.compile(r"^[A-Za-z][A-Za-z0-9_]*:[A-Za-z0-9._\-]+$")


def validate_phenopackets(
    path: Path,
) -> Union[Tuple[bool, str], List[Tuple[bool, str]]]:
    """
    Validate a phenopacket file or directory of phenopackets.

    Runs up to three stages:

    1. **Python-native structural checks** — required fields, schema version,
       CURIE format, ``subject.id``.
    2. **Ontology-prefix placement checks** — soft warnings when HP: terms
       appear outside ``phenotypicFeatures`` or MONDO: terms appear outside
       ``diseases``. Non-fatal: the phenopacket still passes, but warnings
       are surfaced in the return string to help catch routing errors.
    3. **phenopacket-tools CLI** — when the CLI is on PATH, provides deeper
       schema-level validation on top of stages 1 and 2.

    Args:
        path: Path to a single ``.json`` file or a directory.

    Returns:
        - Single file  → ``(bool, str)``
        - Directory    → ``List[(bool, str)]``

    Raises:
        ValueError: If path does not exist, is not a JSON file, or a
                    directory contains no JSON files.
    """
    logger.info("Starting validation of phenopackets...")

    if not path.exists():
        raise ValueError(f"Path {path} does not exist.")

    if path.is_file():
        if path.suffix == ".json":
            return _validate_single_phenopacket(path)
        raise ValueError(f"File {path} is not a valid JSON file.")

    if path.is_dir():
        results = [
            _validate_single_phenopacket(fp)
            for fp in sorted(path.glob("*.json"))
        ]
        if not results:
            raise ValueError(f"Directory {path} contains no JSON files.")
        passed = sum(1 for ok, _ in results if ok)
        logger.info(
            f"Validation completed: {passed}/{len(results)} files passed."
        )
        return results

    raise ValueError(f"Path {path} is neither a file nor a directory.")


def _validate_single_phenopacket(file_path: Path) -> Tuple[bool, str]:
    """Run all available validation stages on one file."""
    logger.debug(f"Validating {file_path}...")

    # Stage 1: structural
    ok, msg = _python_validate(file_path)
    if not ok:
        logger.warning(f"Structural validation failed for {file_path}: {msg}")
        return False, msg

    # Stage 2: prefix placement warnings (non-fatal)
    prefix_warnings = _prefix_placement_check(file_path)

    # Stage 3: CLI (optional)
    if shutil.which("phenopacket-tools"):
        ok, cli_msg = _cli_validate(file_path)
        if not ok:
            logger.warning(f"CLI validation failed for {file_path}: {cli_msg}")
            detail = cli_msg
            if prefix_warnings:
                detail += "\n\nOntology prefix warnings:\n" + "\n".join(
                    f"  ⚠  {w}" for w in prefix_warnings
                )
            return False, detail
        logger.debug(f"CLI validation passed: {file_path}")
    else:
        logger.debug(
            "phenopacket-tools not found on PATH — skipping CLI validation. "
            "Install for deeper schema checks: "
            "https://github.com/phenopackets/phenopacket-tools"
        )

    detail = f"OK: {file_path}"
    if prefix_warnings:
        detail += "\n\nOntology prefix warnings (non-fatal):\n" + "\n".join(
            f"  ⚠  {w}" for w in prefix_warnings
        )

    logger.debug(f"Validation passed: {file_path}")
    return True, detail


def _python_validate(file_path: Path) -> Tuple[bool, str]:
    """Python-native structural checks against the Phenopacket v2 JSON schema."""
    try:
        with open(file_path) as f:
            doc = json.load(f)
    except json.JSONDecodeError as exc:
        return False, f"Invalid JSON: {exc}"

    errors: List[str] = []

    missing = _REQUIRED_TOP_LEVEL - doc.keys()
    if missing:
        errors.append(f"Missing required top-level keys: {sorted(missing)}")

    meta = doc.get("metaData", {})
    if isinstance(meta, dict):
        missing_meta = _REQUIRED_METADATA - meta.keys()
        if missing_meta:
            errors.append(
                f"metaData missing required keys: {sorted(missing_meta)}"
            )
        schema_ver = meta.get("phenopacketSchemaVersion", "")
        if schema_ver and not schema_ver.startswith("2"):
            errors.append(
                f"phenopacketSchemaVersion is '{schema_ver}', expected '2.x'"
            )

    subject = doc.get("subject")
    if subject is not None:
        if not isinstance(subject, dict) or not subject.get("id"):
            errors.append("subject block is present but missing 'id'")

    errors.extend(_check_curie_terms(doc, path="$"))

    if errors:
        return False, "; ".join(errors)
    return True, "Structural checks passed"


def _prefix_placement_check(file_path: Path) -> List[str]:
    """Load the phenopacket JSON and run ontology-prefix placement checks."""
    try:
        with open(file_path) as f:
            doc = json.load(f)
        return check_prefix_placement(doc)
    except Exception as exc:
        logger.debug(
            f"Could not run prefix-placement check on {file_path}: {exc}"
        )
        return []


def _cli_validate(file_path: Path) -> Tuple[bool, str]:
    """Run ``phenopacket-tools validate`` and return (success, output)."""
    command = ["phenopacket-tools", "validate", str(file_path)]
    try:
        output = subprocess.check_output(
            command, stderr=subprocess.STDOUT, text=True
        )
        return True, output
    except subprocess.CalledProcessError as exc:
        return False, exc.output or str(exc)


def _check_curie_terms(node, path: str) -> List[str]:
    """
    Recursively check that all ontology term ids are valid CURIEs.
    An OntologyClass-like object is any dict with both ``"id"`` and ``"label"``.
    """
    errors: List[str] = []
    if isinstance(node, dict):
        if "id" in node and "label" in node:
            term_id = node["id"]
            if isinstance(term_id, str) and not _CURIE_PATTERN.match(term_id):
                errors.append(
                    f"Ontology term id '{term_id}' at {path} "
                    f"is not a valid CURIE (expected PREFIX:localid)"
                )
        for key, value in node.items():
            errors.extend(_check_curie_terms(value, path=f"{path}.{key}"))
    elif isinstance(node, list):
        for i, item in enumerate(node):
            errors.extend(_check_curie_terms(item, path=f"{path}[{i}]"))
    return errors


if __name__ == "__main__":
    import argparse
    import sys

    logging.basicConfig(level=logging.INFO)

    parser = argparse.ArgumentParser(
        description="Validate a phenopacket file or directory of phenopackets."
    )
    parser.add_argument(
        "path",
        type=Path,
        help="Path to the phenopacket file or directory to validate.",
    )
    args = parser.parse_args()

    try:
        results = validate_phenopackets(args.path)
        if isinstance(results, list):
            for success, details in results:
                if not success:
                    logger.error(details)
            if not all(ok for ok, _ in results):
                sys.exit(1)
        else:
            success, details = results
            if not success:
                logger.error(details)
                sys.exit(1)
    except ValueError as ve:
        logger.error(str(ve))
        sys.exit(1)