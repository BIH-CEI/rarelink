from typing import Dict, Any, Optional
import logging
from phenopackets import Individual, OntologyClass

from rarelink.phenopackets.mappings.base_mapper import BaseMapper

logger = logging.getLogger(__name__)

class IndividualMapper(BaseMapper[Individual]):
    """
    Mapper for Individual entities in the Phenopacket schema.
    Maps patient data to the Individual block.
    """
    
    def _map_single_entity(self, data: Dict[str, Any], instruments: list, **kwargs) -> Optional[Individual]:
        """
        Map data to a single Individual entity.
        
        Args:
            data (Dict[str, Any]): Input data to map
            instruments (list): List of instruments for field access
            **kwargs: Additional mapping parameters
                - vital_status (VitalStatus, optional): Pre-constructed vital status
            
        Returns:
            Optional[Individual]: Mapped Individual entity or None on failure
        """
        try:
            # Extract vital status from kwargs if provided
            vital_status = kwargs.get('vital_status')
            
            # Individual data fields
            # ID
            id_field = self.get_field(data, "id_field", instruments)
            if not id_field:
                logger.debug("No ID field found")
                return None

            # Date of Birth
            date_of_birth_field = self.get_field(data, "date_of_birth_field", instruments)
            date_of_birth = self.processor.date_to_timestamp(date_of_birth_field)

            # Time at Last Encounter
            time_at_last_encounter_field = self.get_field(
                data, "time_at_last_encounter_field", instruments
            )
            
            time_at_last_encounter = None
            if date_of_birth_field and time_at_last_encounter_field:
                try:
                    iso_age = self.processor.convert_date_to_iso_age(
                        time_at_last_encounter_field, 
                        date_of_birth_field)
                    if iso_age:
                        from phenopackets import TimeElement, Age
                        time_at_last_encounter = TimeElement(age=Age(
                            iso8601duration=iso_age))
                except Exception as e:
                    logger.error(f"Error calculating time at last encounter: {e}")

            # Sex
            sex_field = self.get_field(data, "sex_field", instruments)
            sex = self.fetch_mapping_value("map_sex", sex_field) or "UNKNOWN_SEX"

            # Karyotypic Sex
            karyotypic_sex_field = self.get_field(data, "karyotypic_sex_field", instruments)
            karyotypic_sex = self.fetch_mapping_value(
                "map_karyotypic_sex", karyotypic_sex_field
            ) or "UNKNOWN_KARYOTYPE"

            # Gender
            gender_field = self.get_field(data, "gender_field", instruments)
            gender = None
            if gender_field:
                processed_gender = self.process_code(gender_field)
                gender_label = self.fetch_label(
                    gender_field, enum_class="GenderIdentity"
                )
                gender = OntologyClass(
                    id=processed_gender,
                    label=gender_label or "Unknown"
                )

            # Taxonomy - assuming human as default
            taxonomy = OntologyClass(
                id="NCBITaxon:9606",
                label="Homo sapiens"
            )

            # Creating the Individual block
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

            return individual
            
        except Exception as e:
            logger.error(f"Error mapping individual: {e}")
            import traceback
            logger.debug(traceback.format_exc())
            return None
    
    def _map_multi_entity(self, data: Dict[str, Any], instruments: list, **kwargs) -> list:
        """
        Map data to multiple Individual entities.
        
        Note: Individual mappers typically return just a single entity, but this
        method is required by the BaseMapper interface. It will wrap the single
        entity in a list if successful.
        
        Args:
            data (Dict[str, Any]): Input data to map
            instruments (list): List of instruments for field access
            **kwargs: Additional mapping parameters
            
        Returns:
            list: List containing a single mapped Individual or empty list on failure
        """
        # For Individual, we expect just a single entity
        individual = self._map_single_entity(data, instruments, **kwargs)
        
        if individual:
            return [individual]
        return []