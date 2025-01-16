import logging
from phenopackets import Individual, OntologyClass, TimeElement
from rarelink.utils.processing.dates.timestamp import date_to_timestamp
from rarelink.utils.processing.codes.process_redcap_code import process_redcap_code
from rarelink_cdm.v2_0_0_dev0.mappings.phenopackets.mapping_dicts import get_mapping_by_name
from rarelink.utils.processing.codes.fetch_displays import fetch_label_directly
from rarelink.utils.loading import get_nested_field

logger = logging.getLogger(__name__)


def wrap_in_time_element(timestamp):
    """
    Wraps a Protobuf `Timestamp` in a Phenopacket `TimeElement`.

    Args:
        timestamp (Timestamp): A Protobuf Timestamp object.

    Returns:
        TimeElement: A Phenopacket TimeElement wrapping the given Timestamp.
    """
    if timestamp is None:
        return None
    return TimeElement(timestamp=timestamp)

def map_individual(data: dict, mapping_config: dict) -> Individual:
    """
    Maps patient data to the Individual block based on the provided mapping configuration.

    Args:
        data (dict): Input data from the RareLink-CDM schema (or similar).
        mapping_config (dict): Configuration defining how to map input fields.

    Returns:
        Individual: A Phenopacket Individual block.
    """
    try:
        # Extract ID
        id_field = get_nested_field(data, mapping_config["id_field"])

        # Date of Birth
        date_of_birth_field = get_nested_field(data, mapping_config["date_of_birth_field"])
        date_of_birth = date_to_timestamp(date_of_birth_field)

        # Time at Last Encounter
        time_at_last_encounter_field = get_nested_field(data, mapping_config["time_at_last_encounter_field"])
        time_at_last_encounter = wrap_in_time_element(date_to_timestamp(time_at_last_encounter_field))

        # Sex
        sex_field = get_nested_field(data, mapping_config["sex_field"])
        sex = get_mapping_by_name("map_sex").get(sex_field, "UNKNOWN_SEX")

        # Karyotypic Sex
        karyotypic_sex_field = get_nested_field(data, mapping_config["karyotypic_sex_field"])
        karyotypic_sex = get_mapping_by_name("map_karyotypic_sex").get(karyotypic_sex_field, "UNKNOWN_KARYOTYPE")

        # Gender
        gender_field = get_nested_field(data, mapping_config["gender_field"])
        if gender_field:
            processed_gender = process_redcap_code(gender_field)
            
            # Fetch the label for the processed code
            gender_label = fetch_label_directly(processed_gender)
            logger.debug(f"Fetched label for gender field: {gender_label}")

            gender = OntologyClass(
                id=processed_gender,
                label=gender_label or "Unknown"
            )
        else:
            gender = None
            logger.debug("Gender field is missing or empty, set to None.")
            
        taxonomy = OntologyClass(
            id="NCBITaxon:9606",
            label="Homo sapiens"
        )

        # Create the Individual block
        individual = Individual(
            id=id_field,
            date_of_birth=date_of_birth,
            time_at_last_encounter=time_at_last_encounter,
            sex=sex,
            karyotypic_sex=karyotypic_sex,
            gender=gender,
            taxonomy=taxonomy,
        )

        logger.info(f"Successfully mapped individual: {individual}")
        return individual

    except Exception as e:
        logger.error(f"Failed to map individual: {e}")
        raise