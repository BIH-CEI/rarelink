from pyphetools.creation.variant_validator import VariantValidator
from logging import Logger
from rarelink_cdm.v2_0_0_dev0.mappings.redcap import HGVS_VARIABLES, REFERENCE_GENOME_MAPPING
import typer
from rarelink.cli.utils import success_text, error_text

logger = Logger(__name__)   

URL_SCHEME = (
    "https://rest.variantvalidator.org/VariantValidator/variantvalidator/%s/%s%%3A%s/%s?content-type=application%%2Fjson"
)


def validate_and_encode_hgvs(data, transcript_key=None):
    """
    Validate and encode HGVS strings in the data using VariantValidator.

    Args:
        data (dict): Data containing HGVS strings to validate.
        transcript_key (str): Key in the data that contains the transcript information (e.g., 'transcript').

    Returns:
        dict: Data with validation status logged.
    """
    # Fetch genome_build dynamically
    genome_build_field = data.get("loinc_62374_4")  # Assuming this is the field holding REFERENCE_GENOME
    genome_build = REFERENCE_GENOME_MAPPING.get(genome_build_field, None)

    if not genome_build or genome_build not in {"hg19", "hg38"}:
        genome_build = "hg38"

    # Initialize the validator
    validator = VariantValidator(genome_build)

    for variable in HGVS_VARIABLES:
        hgvs_string = data.get(variable)
        if hgvs_string and isinstance(hgvs_string, str) and hgvs_string.strip():
            # Store the original HGVS string for logging purposes
            original_hgvs_string = hgvs_string

            # Extract transcript and HGVS separately
            transcript = None
            if transcript_key and transcript_key in data:
                transcript = data[transcript_key]
            elif ":" in hgvs_string:
                transcript, hgvs_string = hgvs_string.split(":", 1)

            try:
                # Attempt validation
                validator.encode_hgvs(hgvs_string, custom_transcript=transcript)
                success_text(f"✅ Validation succeeded for {original_hgvs_string}")
            except Exception as e:
                error_text(f"⚠️ Validation failed for {original_hgvs_string}: {e}")
        else:
            continue

    return data
