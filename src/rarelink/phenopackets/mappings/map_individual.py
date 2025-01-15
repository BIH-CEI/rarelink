import logging
from phenopackets import Individual, OntologyClass
from rarelink.utils.processing.dates.timestamp import date_to_timestamp
from rarelink.utils.processing.codes.process_redcap_code import process_redcap_code
from rarelink_cdm.v2_0_0_dev0.mappings.phenopackets.mapping_dicts import get_mapping_by_name

logger = logging.getLogger(__name__)

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
        id_field = data.get(mapping_config["id_field"], None)

        # Date of Birth
        date_of_birth_field = data.get(
            mapping_config["date_of_birth_field"], None)
        date_of_birth = date_to_timestamp(
            date_of_birth_field) if date_of_birth_field else None

        # Time at Last Encounter
        time_at_last_encounter_field = data.get(
            mapping_config["time_at_last_encounter_field"], None)
        time_at_last_encounter = date_to_timestamp(
            time_at_last_encounter_field) if time_at_last_encounter_field else None

        # Sex
        sex_field = data.get(mapping_config["sex_field"], None)
        sex = get_mapping_by_name("map_sex").get(sex_field, "UNKNOWN_SEX")

        # Karyotypic Sex
        karyotypic_sex_field = data.get(
            mapping_config["karyotypic_sex_field"], None)
        karyotypic_sex = get_mapping_by_name(
            "map_karyotypic_sex").get(karyotypic_sex_field, "UNKNOWN_KARYOTYPE")

        # Gender
        gender_field = data.get(mapping_config["gender_field"], None)
        gender = process_redcap_code(
            gender_field, "SNOMEDCT") if gender_field else None

        # Taxonomy (assume human as default)
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
