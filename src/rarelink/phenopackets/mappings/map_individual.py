# src/rarelink/phenopackets/mappings/map_individual.py
import logging
from phenopackets import Individual, OntologyClass, VitalStatus, TimeElement, Age
from rarelink.utils.processor import DataProcessor
from phenopackets.schema.v2 import VitalStatus as VitalStatusEnum  # Import enum directly

logger = logging.getLogger(__name__)

def map_individual(data: dict, 
                   processor: DataProcessor, 
                   vital_status: VitalStatus = None) -> Individual:
    """
    Maps patient data to the Individual block using a DataProcessor.
    Enhanced to properly handle vital status using direct enum values.

    Args:
        data (dict): Input data from any schema.
        processor (DataProcessor): Handles all data processing logic.
        vital_status (VitalStatus, optional): Pre-constructed vital status.

    Returns:
        Individual: A Phenopacket Individual block.
    """
    try:
        # Individual data fields
        # --------------------------------------------------------------------------
        # ID
        id_field = processor.get_field(data, "id_field")

        # Date of Birth
        date_of_birth_field = processor.get_field(data, "date_of_birth_field")
        date_of_birth = processor.date_to_timestamp(date_of_birth_field)

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

        # Handle vital status directly with enum value
        # --------------------------------------------
        # Since we know UNKNOWN_STATUS is not working correctly through the normal
        # VitalStatus constructor, we'll create the VitalStatus with a direct enum value
        # which is more reliable for protobuf serialization
        
        # Define enum mapping
        status_enum_map = {
            "UNKNOWN_STATUS": VitalStatusEnum.Status.UNKNOWN_STATUS,
            "ALIVE": VitalStatusEnum.Status.ALIVE,
            "DECEASED": VitalStatusEnum.Status.DECEASED
        }
        
        # Use existing vital status or create a new one with UNKNOWN_STATUS
        if vital_status is None:
            logger.debug("Creating new VitalStatus with UNKNOWN_STATUS")
            # Create VitalStatus with explicit enum value
            vital_status = VitalStatus(status="UNKNOWN_STATUS")
            vital_status.status = status_enum_map["UNKNOWN_STATUS"]
        elif not vital_status.status:
            logger.debug("Setting existing VitalStatus to UNKNOWN_STATUS")
            vital_status.status = status_enum_map["UNKNOWN_STATUS"]
            
        logger.debug(f"Final vital status: {vital_status}")

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

        logger.info(f"Successfully mapped individual: {individual.id}")
        return individual

    except Exception as e:
        logger.error(f"Failed to map individual: {e}")
        raise