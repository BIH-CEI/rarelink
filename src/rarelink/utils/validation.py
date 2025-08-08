from pyphetools.creation.variant_validator import VariantValidator
from logging import Logger
from rarelink_cdm import import_from_latest
import typer
import io
import logging
from contextlib import redirect_stdout
import subprocess
from pathlib import Path
from rarelink.cli.utils.string_utils import success_text, error_text


logger = Logger(__name__)   

URL_SCHEME = (
    "https://rest.variantvalidator.org/VariantValidator/variantvalidator/%s/%s%%3A%s/%s?content-type=application%%2Fjson"

)

logger = logging.getLogger(__name__)

try:
    redcap = import_from_latest("mappings.redcap")
    HGVS_VARIABLES = getattr(redcap, "HGVS_VARIABLES")
    REFERENCE_GENOME_MAPPING = getattr(redcap, "REFERENCE_GENOME_MAPPING")
except Exception as e:
    logger.warning(f"Falling back to built-in defaults; could not import latest redcap mappings: {e}")
    # Sensible built-ins if you want a fallback:
    HGVS_VARIABLES = ["loinc_48004_6", "loinc_69548_6"]  # ← example placeholders
    REFERENCE_GENOME_MAPPING = {"LA30124-3": "hg19", "LA26806-2": "hg38"}  # ← example placeholders

def validate_and_encode_hgvs(
    data: dict,
    transcript_key: str = None,
    variables: list[str] = None
    
) -> dict:
    """
    Validate and encode HGVS strings in a (possibly nested) record using VariantValidator.
    Additionally, count and record the number of attempted validations, successes,
    and failures. The summary is attached to the record under the key
    '_hgvs_validation_summary'.

    Args:
        data (dict): Data (a single record) potentially containing HGVS strings.
        transcript_key (str): Key in each dict that contains transcript information.
        variables (list[str]): List of keys to treat as HGVS strings. Defaults to HGVS_VARIABLES.

    Returns:
        dict: The original record (modified in place) with an added '_hgvs_validation_summary' field.
    """
    # Use the provided list or fall back to the module‐level constant
    hgvs_vars = variables or HGVS_VARIABLES

    # Determine genome build from top‐level field if present
    genome_build_field = data.get("loinc_62374_4")
    genome_build = REFERENCE_GENOME_MAPPING.get(genome_build_field, None)
    if genome_build not in {"hg19", "hg38"}:
        genome_build = "hg38"
    validator = VariantValidator(genome_build)

    # Counters
    validations_attempted = 0
    successes = 0
    failures = 0
    failure_details: list[dict] = []

    def _walk(obj: any, parent: dict | None = None):
        nonlocal validations_attempted, successes, failures

        # If it's a dict, check for any HGVS keys, then recurse
        if isinstance(obj, dict):
            for key, val in obj.items():
                if key in hgvs_vars and isinstance(val, str) and val.strip():
                    validations_attempted += 1
                    original = val
                    # try to pull transcript
                    transcript = None
                    if transcript_key and transcript_key in obj:
                        transcript = obj[transcript_key]
                    elif ":" in val:
                        t, rest = val.split(":", 1)
                        transcript, val = t, rest

                    try:
                        f = io.StringIO()
                        with redirect_stdout(f):
                            validator.encode_hgvs(val, custom_transcript=transcript)
                        successes += 1
                        success_text(f"✅ Validation succeeded for {original}")
                    except Exception as e:
                        failures += 1
                        failure_details.append({"variable": key, "error": str(e)})
                        error_text(f"⚠️ Validation failed for {original}: {e}")
                        typer.echo(
                            f"Tried to validate {key} with HGVS: {val}, "
                            f"transcript: {transcript}, genome build: {genome_build}"
                        )

                # recurse into nested dicts/lists
                _walk(val, parent=obj)

        # If it's a list, walk each element
        elif isinstance(obj, list):
            for item in obj:
                _walk(item, parent=obj)

    # Start walking the full record
    _walk(data)

    data["_hgvs_validation_summary"] = {
        "validations_attempted": validations_attempted,
        "successes": successes,
        "failures": failures,
        "failure_details": failure_details,
    }
    return data


def validate_linkml_data(schema_path: Path, processed_file: Path) -> bool:
    """
    Validate the processed data against the LinkML schema.

    Args:
        schema_path (Path): Path to the LinkML schema YAML file.
        processed_file (Path): Path to the processed JSON file.

    Returns:
        bool: True if validation is successful, False otherwise.
    """
    try:
        # Resolve to absolute paths
        resolved_schema_path = schema_path.resolve(strict=True)
        resolved_processed_file = processed_file.resolve(strict=True)
        logger.info(f"Resolved schema path: {resolved_schema_path}")
        logger.info(f"Resolved processed file path: {resolved_processed_file}")
        
        # Execute linkml-validate command
        result = subprocess.run(
            [
                "linkml-validate",
                "--schema",
                str(resolved_schema_path),
                str(resolved_processed_file),
            ],
            capture_output=True,
            text=True,
        )

        # Log stdout and stderr for debugging
        logger.debug(f"Validation stdout: {result.stdout}")
        logger.debug(f"Validation stderr: {result.stderr}")

        if result.returncode == 0:
            logger.info("Validation successful.")
            return True
        else:
            logger.error("Validation failed.")
            logger.error(f"Validation stderr: {result.stderr}")
            return False
    except FileNotFoundError as e:
        logger.error(f"File not found: {e}")
        raise RuntimeError(f"File not found: {e}") from e
    except Exception as e:
        logger.error(f"Unexpected error during validation: {e}")
        raise
