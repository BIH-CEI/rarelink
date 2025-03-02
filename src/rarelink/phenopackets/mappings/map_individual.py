import logging
from phenopackets import Individual, OntologyClass, VitalStatus, TimeElement, Age
from rarelink.utils.processor import DataProcessor

logger = logging.getLogger(__name__)

def map_individual(data: dict, 
                   processor: DataProcessor, 
                   vital_status: VitalStatus = None) -> Individual:
    """
    Maps patient data to the Individual block using a DataProcessor.

    Args:
        data (dict): Input data from the RareLink-CDM schema (or similar).
        processor (DataProcessor): Handles all data processing logic.

    Returns:
        Individual: A Phenopacket Individual block.
    """
    # Single instance data
    # --------------------------------------------------------------------------
    try:
    # Individual data fields
    # --------------------------------------------------------------------------
        # ID
        id_field = processor.get_field(data, "id_field")

        # Date of Birth
        date_of_birth_field = processor.get_field(data, "date_of_birth_field")
        date_of_birth = processor.process_date(date_of_birth_field)

        # Time at Last Encounter
        time_at_last_encounter_field = processor.get_field(
            data, "time_at_last_encounter_field"
        )
        
        time_at_last_encounter = None
        if date_of_birth_field and time_at_last_encounter_field:
            try:
                iso_age = processor.convert_date_to_iso_age(
                    time_at_last_encounter_field, 
                    date_of_birth_field)
                time_at_last_encounter = TimeElement(age=Age(
                    iso8601duration=iso_age))
            except Exception as e:
                logger.error(f"Error calculating time at last encounter: {e}")

        # Sex
        sex_field = processor.get_field(data, "sex_field")
        sex = processor.fetch_mapping_value("map_sex", sex_field) or "UNKNOWN_SEX"

        # Karyotypic Sex
        karyotypic_sex_field = processor.get_field(data, "karyotypic_sex_field")
        karyotypic_sex = processor.fetch_mapping_value(
            "map_karyotypic_sex", karyotypic_sex_field
        ) or "UNKNOWN_KARYOTYPE"

        # Gender
        gender_field = processor.get_field(data, "gender_field")
        if gender_field:
            processed_gender = processor.process_code(gender_field)
            gender_label = processor.fetch_label(
                gender_field, enum_class="GenderIdentity"
            )
            gender = OntologyClass(
                id=processed_gender,
                label=gender_label or "Unknown"
            )
        else:
            gender = None

        # Taxonomy - assuming human as default
        taxonomy = OntologyClass(
            id="NCBITaxon:9606",
            label="Homo sapiens"
        )

        # Creating the Individual block
        # ----------------------------------------------------------------------
        individual = Individual(
            id=id_field,
            date_of_birth=date_of_birth,
            time_at_last_encounter=time_at_last_encounter,
            sex=sex,
            karyotypic_sex=karyotypic_sex,
            gender=gender,
            vital_status=vital_status,
            taxonomy=taxonomy,
        )

        logger.info(f"Successfully mapped individual: {individual}")
        return individual

    except Exception as e:
        logger.error(f"Failed to map individual: {e}")
        raise
