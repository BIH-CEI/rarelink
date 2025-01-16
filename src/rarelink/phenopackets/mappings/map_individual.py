import logging
from phenopackets import Individual, OntologyClass
from rarelink.utils.processor import DataProcessor

logger = logging.getLogger(__name__)

def map_individual(data: dict, processor: DataProcessor) -> Individual:
    """
    Maps patient data to the Individual block using a DataProcessor.

    Args:
        data (dict): Input data from the RareLink-CDM schema (or similar).
        processor (DataProcessor): Handles all data processing logic.

    Returns:
        Individual: A Phenopacket Individual block.
    """
    try:
        # Extract ID
        id_field = processor.get_field(data, "id_field")

        # Date of Birth
        date_of_birth_field = processor.get_field(data, "date_of_birth_field")
        date_of_birth = processor.process_date(date_of_birth_field)

        # Time at Last Encounter
        time_at_last_encounter_field = processor.get_field(
            data, "time_at_last_encounter_field")
        time_at_last_encounter = processor.process_time_element(
            time_at_last_encounter_field)

        # Sex
        sex_field = processor.get_field(data, "sex_field")
        sex_label = processor.fetch_description_from_label_dict("SexAtBirth", sex_field)
        sex = sex_label or "UNKNOWN_SEX"

        # Karyotypic Sex
        karyotypic_sex_field = processor.get_field(data, "karyotypic_sex_field")
        karyotypic_sex_label = processor.fetch_description_from_label_dict(
            "KaryotypicSex", karyotypic_sex_field
        )
        karyotypic_sex = karyotypic_sex_label or "UNKNOWN_KARYOTYPE"

        # Gender
        gender_field = processor.get_field(data, "gender_field")
        if gender_field:
            processed_gender = processor.process_code(gender_field)
            gender_label = processor.fetch_description_from_label_dict(
                "GenderIdentity", gender_field
            )
            gender = OntologyClass(
                id=processed_gender,
                label=gender_label or "Unknown"
            )
        else:
            gender = None

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
