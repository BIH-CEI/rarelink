from pyphetools.creation.variant_validator import VariantValidator
from logging import Logger
from rarelink_cdm.v2_0_0_dev1.mappings.redcap import HGVS_VARIABLES, REFERENCE_GENOME_MAPPING
import typer
import io
from contextlib import redirect_stdout
from rarelink.cli.utils import success_text, error_text

logger = Logger(__name__)   

URL_SCHEME = (
    "https://rest.variantvalidator.org/VariantValidator/variantvalidator/%s/%s%%3A%s/%s?content-type=application%%2Fjson"
)

def validate_and_encode_hgvs(data, transcript_key=None):
    """
    Validate and encode HGVS strings in a single record using VariantValidator.
    Additionally, count and record the number of attempted validations, successes,
    and failures. The summary is attached to the record under the key
    '_hgvs_validation_summary'.

    Args:
        data (dict): Data (a single record) containing HGVS strings.
        transcript_key (str): Key in the data that contains transcript information.

    Returns:
        dict: The original record with an added '_hgvs_validation_summary' field.
    """


    genome_build_field = data.get("loinc_62374_4")  # Field holding REFERENCE_GENOME
    genome_build = REFERENCE_GENOME_MAPPING.get(genome_build_field, None)
    if not genome_build or genome_build not in {"hg19", "hg38"}:
        genome_build = "hg38"

    validator = VariantValidator(genome_build)

    validations_attempted = 0
    successes = 0
    failures = 0
    failure_details = []  # List of dicts { variable, error }

    for variable in HGVS_VARIABLES:
        hgvs_string = data.get(variable)
        if hgvs_string and isinstance(hgvs_string, str) and hgvs_string.strip():
            validations_attempted += 1
            original_hgvs = hgvs_string
            transcript = None
            if transcript_key and transcript_key in data:
                transcript = data[transcript_key]
            elif ":" in hgvs_string:
                parts = hgvs_string.split(":", 1)
                transcript, hgvs_string = parts[0], parts[1]
            try:
                f = io.StringIO()
                with redirect_stdout(f):
                    validator.encode_hgvs(hgvs_string, custom_transcript=transcript)
                successes += 1
                success_text(f"✅ Validation succeeded for {original_hgvs}")
            except Exception as e:
                failures += 1
                failure_details.append({ "variable": variable, "error": str(e) })
                error_text(f"⚠️ Validation failed for {original_hgvs}: {e}")
                typer.echo(
                    f"Tried to validate {variable} with HGVS: {hgvs_string}, "
                    f"transcript: {transcript}, genome build: {genome_build}"
                )
    data["_hgvs_validation_summary"] = {
        "validations_attempted": validations_attempted,
        "successes": successes,
        "failures": failures,
        "failure_details": failure_details,
    }
    return data