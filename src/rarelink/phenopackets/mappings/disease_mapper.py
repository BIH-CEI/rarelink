# src/rarelink/phenopackets/mappings/disease_mapper.py
from typing import Dict, Any, List, Optional
import logging
from phenopackets import Disease, OntologyClass, TimeElement, Age

from rarelink.utils.field_access import get_multi_instrument_field_value
from rarelink.phenopackets.mappings.base_mapper import BaseMapper

logger = logging.getLogger(__name__)

class DiseaseMapper(BaseMapper[Disease]):
    """
    Mapper for Disease entities in the Phenopacket schema.
    Always returns a list of Disease objects for consistency.
    """
    
    def map(self, data: Dict[str, Any], **kwargs) -> List[Disease]:
        """
        Map data to a list of Disease entities.
        Overrides the base method to ensure a list is always returned.
        
        Args:
            data (Dict[str, Any]): Input data to map
            **kwargs: Additional mapping parameters
                - dob (str, optional): Date of birth for age calculations
            
        Returns:
            List[Disease]: List of mapped Disease entities
        """
        # Set multi_entity to True to ensure _map_multi_entity is called
        self.processor.mapping_config["multi_entity"] = True
        
        # Call the base map method which will call _map_multi_entity
        return super().map(data, **kwargs)
    
    def _map_single_entity(self, data: Dict[str, Any], instruments: List[str], **kwargs) -> Optional[Disease]:
        """
        Map data to a single Disease entity.
        
        Args:
            data (Dict[str, Any]): Input data to map
            instruments (List[str]): List of instruments for field access
            **kwargs: Additional mapping parameters
                - dob (str, optional): Date of birth for age calculations
            
        Returns:
            Optional[Disease]: Mapped Disease entity or None on failure
        """
        dob = kwargs.get('dob')
        
        # Extract term ID from data using multiple field paths
        term_id = None
        for i in range(1, 6):  # Try term_field_1 through term_field_5
            field_key = f"term_field_{i}"
            field_path = self.processor.mapping_config.get(field_key)
            
            if not field_path:
                continue
            
            # Use multi-instrument field access
            term_id = get_multi_instrument_field_value(
                data=data,
                instruments=instruments,
                field_paths=[field_path]
            )
            
            if term_id:
                logger.debug(f"Found disease term ID: {term_id} from {field_key}")
                break
        
        # If no term ID found, return None
        if not term_id:
            logger.debug("No disease term ID found")
            return None
        
        # Process the term ID and get label
        processed_id = self.process_code(term_id)
        term_label = self.fetch_label(term_id) or self.fetch_label(processed_id)
        
        # Create the term OntologyClass
        term = OntologyClass(
            id=processed_id, 
            label=term_label or "Unknown Disease"
        )
        
        # Extract excluded status
        excluded = None
        excluded_field = self.processor.mapping_config.get("excluded_field")
        if excluded_field:
            excluded_value = get_multi_instrument_field_value(
                data=data,
                instruments=instruments,
                field_paths=[excluded_field]
            )
            
            if excluded_value:
                mapped_value = self.fetch_mapping_value(
                    "map_disease_verification_status", excluded_value)
                if mapped_value == "true":
                    excluded = True
                elif mapped_value == "false":
                    excluded = False
        
        # Extract onset
        onset = None
        onset_date_field = self.processor.mapping_config.get("onset_date_field")
        onset_category_field = self.processor.mapping_config.get("onset_category_field")
        
        # For onset lookup, start with the instruments provided by the mapping configuration.
        # Then, if the data has a "patient_demographics_initial_form" key, include it as a fallback.
        onset_instruments = instruments.copy()
        if "patient_demographics_initial_form" in data:
            onset_instruments.append("patient_demographics_initial_form")
        
        if onset_date_field and dob:
            onset_date = get_multi_instrument_field_value(
                data=data,
                instruments=onset_instruments,
                field_paths=[onset_date_field]
            )
            
            if onset_date:
                try:
                    # Format onset_date and dob as strings
                    onset_date_str = onset_date if isinstance(onset_date, str) else str(onset_date)
                    dob_str = dob if isinstance(dob, str) else str(dob)
                    
                    iso_age = self.processor.convert_date_to_iso_age(onset_date_str, dob_str)
                    if iso_age:
                        onset = TimeElement(age=Age(iso8601duration=iso_age))
                except Exception as e:
                    logger.error(f"Error calculating onset age: {e}")
        
        if not onset and onset_category_field:
            onset_category = get_multi_instrument_field_value(
                data=data,
                instruments=onset_instruments,
                field_paths=[onset_category_field]
            )
                
            if onset_category:
                onset_label = self.fetch_label(onset_category, enum_class="AgeAtOnset")
                onset_code = self.process_code(onset_category)
                if onset_label:
                    onset = TimeElement(
                        ontology_class=OntologyClass(
                            id=onset_code, 
                            label=onset_label
                        )
                )
        
        # Extract primary site
        primary_site = None
        primary_site_field = self.processor.mapping_config.get("primary_site_field")
        if primary_site_field:
            primary_site_id = get_multi_instrument_field_value(
                data=data,
                instruments=instruments,
                field_paths=[primary_site_field]
            )
            
            if primary_site_id:
                primary_site_label = self.fetch_label(primary_site_id)
                primary_site = OntologyClass(
                    id=primary_site_id, 
                    label=primary_site_label or "Unknown Site"
                )
        
        # Create the Disease entity
        disease = Disease(
            term=term,
            onset=onset,
            excluded=excluded,
            primary_site=primary_site
        )
        
        logger.debug(f"Created disease: {disease.term.id} - {disease.term.label}")
        return disease
    
    def _map_multi_entity(self, data: Dict[str, Any], instruments: List[str], **kwargs) -> List[Disease]:
        dob = kwargs.get('dob')
        diseases = []
        try:
            # Force instruments to be a list of strings.
            instruments_str = []
            instrument_name = self.processor.mapping_config.get("instrument_name")
            if instrument_name:
                if isinstance(instrument_name, (list, set)):
                    instruments_str = [str(x) for x in instrument_name]
                else:
                    instruments_str = [str(instrument_name)]
            repeat_instrument = self.processor.mapping_config.get("redcap_repeat_instrument")
            if repeat_instrument and repeat_instrument not in instruments_str:
                instruments_str.append(str(repeat_instrument))
            
            logger.debug(f"Looking for disease data using instruments: {instruments_str}")
            
            # CASE 1: Try to find term data in direct top-level sections
            for instrument in instruments_str:
                if instrument in data:
                    logger.debug(f"Found direct top-level section: {instrument}")
                    disease = self._map_single_entity(data, [instrument], dob=dob)
                    if disease:
                        diseases.append(disease)
                        logger.debug(f"Created disease from top-level section: {disease.term.id}")
                        return diseases
            
            # CASE 2: Try repeated_elements if no direct disease found
            if not diseases and "repeated_elements" in data:
                logger.debug(f"Looking in repeated elements for instruments: {instruments_str}")
                repeated_elements = data.get("repeated_elements", [])
                for instrument in instruments_str:
                    disease_elements = [
                        element for element in repeated_elements
                        if element.get("redcap_repeat_instrument") == instrument
                    ]
                    for element in disease_elements:
                        element_data = data.copy()
                        if instrument in element:
                            element_data[instrument] = element[instrument]
                        disease = self._map_single_entity(element_data, [instrument], dob=dob)
                        if disease:
                            diseases.append(disease)
                            logger.debug(f"Added disease from repeated element: {disease.term.id}")
            return diseases
        except Exception as e:
            logger.error(f"Error mapping multiple diseases: {e}")
            import traceback
            logger.debug(traceback.format_exc())
            return []
