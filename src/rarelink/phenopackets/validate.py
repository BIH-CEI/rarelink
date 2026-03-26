import json
import re
import shutil
import subprocess
from pathlib import Path
from typing import List, Tuple, Union
import logging

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Required top-level keys for a Phenopacket v2 JSON document
# ---------------------------------------------------------------------------
_REQUIRED_TOP_LEVEL = {"id", "metaData"}

# Required keys inside metaData
_REQUIRED_METADATA = {"created", "createdBy", "phenopacketSchemaVersion"}

# Basic pattern for CURIE-style ontology term IDs (e.g. HP:0001250, MONDO:0007843)
_CURIE_PATTERN = re.compile(r"^[A-Za-z][A-Za-z0-9_]*:[A-Za-z0-9._\-]+$")


def validate_phenopackets(
    path: Path,
) -> Union[Tuple[bool, str], List[Tuple[bool, str]]]:
    """
    Validates a phenopacket file or directory of phenopackets.

    Validation is performed in two stages:
      1. **Python-native checks** — always available, no external tooling needed.
         Verifies JSON structure, required fields, and ontology term format.
      2. **phenopacket-tools CLI** — used automatically when the CLI is on PATH,
         providing deeper schema-level validation on top of the Python checks.

    Args:
        path (Path): Path to a single ``.json`` file or a directory of them.

    Returns:
        - Single file  → ``(bool, str)``  — (passed, detail message)
        - Directory    → ``List[(bool, str)]`` — one tuple per file

    Raises:
        ValueError: If the path does not exist, is not a JSON file, or a
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
            _validate_single_phenopacket(fp) for fp in sorted(path.glob("*.json"))
        ]
        if not results:
            raise ValueError(f"Directory {path} contains no JSON files.")
        passed = sum(1 for ok, _ in results if ok)
        logger.info(
            f"Validation completed: {passed}/{len(results)} files passed."
        )
        return results

    raise ValueError(f"Path {path} is neither a file nor a directory.")


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _validate_single_phenopacket(file_path: Path) -> Tuple[bool, str]:
    """Run all available validation stages on one file."""
    logger.info(f"Validating {file_path}...")

    # --- Stage 1: Python-native structural validation ---
    ok, msg = _python_validate(file_path)
    if not ok:
        logger.error(f"Structural validation failed for {file_path}: {msg}")
        return False, msg

    # --- Stage 2: phenopacket-tools CLI (optional) ---
    if shutil.which("phenopacket-tools"):
        ok, msg = _cli_validate(file_path)
        if not ok:
            logger.warning(f"CLI validation failed for {file_path}: {msg}")
            return False, msg
        logger.info(f"CLI validation passed for {file_path}")
    else:
        logger.debug(
            "phenopacket-tools CLI not found on PATH — skipping CLI validation. "
            "Install it for deeper schema checks: "
            "https://github.com/phenopackets/phenopacket-tools"
        )

    logger.info(f"Validation passed: {file_path}")
    return True, f"OK: {file_path}"


def _python_validate(file_path: Path) -> Tuple[bool, str]:
    """
    Lightweight Python-native checks against the Phenopacket v2 JSON schema:

    - Valid, parseable JSON
    - Required top-level keys present (``id``, ``metaData``)
    - ``metaData`` contains ``created``, ``createdBy``, ``phenopacketSchemaVersion``
    - ``phenopacketSchemaVersion`` is ``"2.0"``
    - All ontology terms (wherever ``{"id": ..., "label": ...}`` objects appear)
      have a CURIE-formatted ``id``
    - ``subject.id`` present when ``subject`` block exists
    """
    # 1. Parse JSON
    try:
        with open(file_path) as f:
            doc = json.load(f)
    except json.JSONDecodeError as exc:
        return False, f"Invalid JSON: {exc}"

    errors: List[str] = []

    # 2. Required top-level keys
    missing = _REQUIRED_TOP_LEVEL - doc.keys()
    if missing:
        errors.append(f"Missing required top-level keys: {sorted(missing)}")

    # 3. metaData checks
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
                f"phenopacketSchemaVersion is '{schema_ver}', expected '2.0'"
            )

    # 4. subject.id
    subject = doc.get("subject")
    if subject is not None:
        if not isinstance(subject, dict) or not subject.get("id"):
            errors.append("subject block is present but missing 'id'")

    # 5. Ontology term CURIE format — walk the whole document
    curie_errors = _check_curie_terms(doc, path="$")
    errors.extend(curie_errors)

    if errors:
        detail = "; ".join(errors)
        return False, detail

    return True, "Structural checks passed"


def _check_curie_terms(node, path: str) -> List[str]:
    """
    Recursively walk *node* and collect CURIE-format violations for any
    object that has an ``"id"`` key whose sibling is ``"label"`` — i.e. an
    OntologyClass-like object.
    """
    errors: List[str] = []

    if isinstance(node, dict):
        # Looks like an OntologyClass if it has both "id" and "label"
        if "id" in node and "label" in node:
            term_id = node["id"]
            if isinstance(term_id, str) and not _CURIE_PATTERN.match(term_id):
                errors.append(
                    f"Ontology term id '{term_id}' at {path} "
                    f"is not a valid CURIE (expected format PREFIX:localid)"
                )
        for key, value in node.items():
            errors.extend(_check_curie_terms(value, path=f"{path}.{key}"))

    elif isinstance(node, list):
        for i, item in enumerate(node):
            errors.extend(_check_curie_terms(item, path=f"{path}[{i}]"))

    return errors


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


# ---------------------------------------------------------------------------
# CLI entry-point
# ---------------------------------------------------------------------------

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