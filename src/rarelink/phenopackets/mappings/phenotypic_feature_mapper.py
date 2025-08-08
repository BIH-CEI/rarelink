from typing import Dict, Any, Optional, List
import logging
from phenopackets import PhenotypicFeature, OntologyClass, TimeElement, Evidence

from rarelink.phenopackets.mappings.base_mapper import BaseMapper
from rarelink.utils.field_access import get_multi_instrument_field_value

from rarelink.phenopackets.adapter.multi_onset import multi_onset_adapter
from rarelink.phenopackets.mappings.utils.common_utils import (
    create_ontology_class,
    create_time_element,
    get_data_elements
)

logger = logging.getLogger(__name__)

class PhenotypicFeatureMapper(BaseMapper[PhenotypicFeature]):
    """
    Mapper for PhenotypicFeature entities in the Phenopacket schema.
    Always returns a list of PhenotypicFeature objects for consistency.
    Supports multiple instruments and data models through configurable mapping blocks.
    """
    
    def map(self, data: Dict[str, Any], **kwargs) -> List[PhenotypicFeature]:
        """
        Map data to a list of PhenotypicFeature entities.
        Overrides the base method to ensure a list is always returned.
        
        Args:
            data (Dict[str, Any]): Input data to map
            **kwargs: Additional mapping parameters
                - dob (str, optional): Date of birth for age calculations
            
        Returns:
            List[PhenotypicFeature]: List of mapped PhenotypicFeature entities
        """
        # Set multi_entity to True to ensure _map_multi_entity is called
        self.processor.mapping_config["multi_entity"] = True
        
        # Store the full data for multi-instrument field access
        self.processor.mapping_config['full_data'] = data
        
        # Call the base map method which will call _map_multi_entity
        return super().map(data, **kwargs)
    
    def _map_single_entity(self, data: Dict[str, Any], instruments: List[str], **kwargs) -> Optional[PhenotypicFeature]:
        """
        Map data to a single PhenotypicFeature entity.
        Note: This method is required by the BaseMapper interface but not directly used
        since we always return multiple entities.
        """
        logger.warning("PhenotypicFeatureMapper._map_single_entity called, but this mapper returns multiple entities")
        return None
    
    def _map_multi_entity(self, data: Dict[str, Any], instruments: List[str], **kwargs) -> List[PhenotypicFeature]:
        """
        Map data to multiple PhenotypicFeature entities.
        
        Args:
            data (Dict[str, Any]): Input data to map
            instruments (List[str]): List of instruments for field access
            **kwargs: Additional mapping parameters
                - dob (str, optional): Date of birth for age calculations
        """
        dob = kwargs.get('dob')
        features = []
        
        try:
            # Store all instruments in the mapping config for field access
            self.processor.mapping_config["all_instruments"] = instruments
            
            # Add default RareLink instrument if not specified (for backward compatibility)
            self._add_default_instruments(instruments)
            
            # First check rarelink specific direct approach
            if self._is_rarelink_compatible():
                rarelink_features = self._map_rarelink_features(data, instruments, dob)
                if rarelink_features:
                    return rarelink_features
            
            # Get the data model from configuration
            data_model = self.processor.mapping_config.get("data_model", "")
            
            # Current instrument
            current_instrument = self._get_current_instrument()
            
            if current_instrument:
                logger.info(f"Processing single instrument: {current_instrument}")
                
                # Map features for this instrument using data model's type extractor
                features = self._map_features_for_instrument(
                    data, 
                    current_instrument,
                    data_model,
                    dob, 
                    instruments
                )
                
                logger.debug(f"Found {len(features)} features for instrument {current_instrument}")
                return features
            
            # Process each instrument in the list
            for instrument_name in instruments:
                # Skip empty or dummy instruments
                if not instrument_name or instrument_name == "__dummy__":
                    continue
                
                instrument_features = self._map_features_for_instrument(
                    data,
                    instrument_name,
                    data_model,
                    dob,
                    instruments
                )
                
                features.extend(instrument_features)
                logger.debug(f"Added {len(instrument_features)} features from instrument {instrument_name}")
                
            logger.debug(f"Total phenotypic features mapped: {len(features)}")
            return features
                
        except Exception as e:
            logger.error(f"Error mapping phenotypic features: {e}")
            import traceback
            logger.debug(traceback.format_exc())
            return []
    
    def _add_default_instruments(self, instruments: List[str]) -> None:
        """Add default instruments for backward compatibility"""
        rarelink_instrument = "rarelink_6_2_phenotypic_feature"
        if rarelink_instrument not in instruments:
            instruments.append(rarelink_instrument)
        
        # Add default field mappings for RareLink CDM if not specified
        if self._is_rarelink_compatible() and "type_field" not in self.processor.mapping_config:
            self.processor.mapping_config["type_field"] = "snomedct_8116006"
            self.processor.mapping_config["onset_date_field"] = "snomedct_8116006_onset"
            self.processor.mapping_config["resolution_field"] = "snomedct_8116006_resolut"
            self.processor.mapping_config["evidence_field"] = "phenotypicfeature_evidence"
    
    def _is_rarelink_compatible(self) -> bool:
        """Check if mapper is in RareLink compatibility mode"""
        return (
            "data_model" not in self.processor.mapping_config or 
            self.processor.mapping_config.get("data_model", "") in ["", "rarelink_cdm"]
        )
    
    def _get_current_instrument(self) -> Optional[str]:
        """Get the current instrument from configuration"""
        return (
            self.processor.mapping_config.get("current_instrument") or
            self.processor.mapping_config.get("redcap_repeat_instrument")
        )
    
    def _map_rarelink_features(self, data: Dict[str, Any], instruments: List[str], dob: str) -> List[PhenotypicFeature]:
        """Map features using RareLink CDM specific approach"""
        features = []
        rarelink_instrument = "rarelink_6_2_phenotypic_feature"
        
        # Direct check for the rarelink repeated elements
        if "repeated_elements" in data:
            logger.debug("Checking repeated_elements for phenotypic features")
            for element in data["repeated_elements"]:
                if element.get("redcap_repeat_instrument") == rarelink_instrument:
                    # Get the phenotypic feature data
                    phenotypic_feature = element.get("phenotypic_feature")
                    if phenotypic_feature:
                        # Get the feature type
                        type_field = self.processor.mapping_config.get("type_field")
                        feature_type = phenotypic_feature.get(type_field)
                        
                        if feature_type:
                            # Create the feature
                            feature = self._create_phenotypic_feature(feature_type, phenotypic_feature, dob, instruments)
                            if feature:
                                features.append(feature)
                                logger.debug(f"Added feature: {feature.type.id} - {feature.type.label}")
        
        # If we found features with the direct approach, return them
        if features:
            logger.debug(f"Found {len(features)} features with RareLink direct approach")
            return features
        
        return []
    
    def _map_features_for_instrument(
        self, 
        data: Dict[str, Any], 
        instrument_name: str,
        data_model: str,
        dob: str,
        all_instruments: List[str]
    ) -> List[PhenotypicFeature]:
        """
        Map features for a specific instrument.
        
        Args:
            data (Dict[str, Any]): Input data to map
            instrument_name (str): Name of the instrument
            data_model (str): Data model identifier
            dob (str): Date of birth for age calculations
            all_instruments (List[str]): List of all instruments for field lookup
        """
        features = []
        
        # Get the data elements for this instrument
        data_elements = get_data_elements(data, instrument_name)
        if not data_elements:
            logger.debug(f"No data elements found for instrument: {instrument_name}")
            return []
        
        logger.debug(f"Found {len(data_elements)} data elements for instrument: {instrument_name}")
        
        # Process each element
        for element in data_elements:
            # Extract type values based on configuration
            type_values = self._extract_type_values(element, data_model, all_instruments)
            
            if not type_values:
                logger.debug("No type values found in element")
                continue
            
            # Process each type value
            for type_value in type_values:
                try:
                    # Check for multi-onset support
                    multi_onset = self.processor.mapping_config.get("multi_onset", False)
                    onset_fields = self.processor.mapping_config.get("onset_date_fields", [])
                    
                    if multi_onset and onset_fields:
                        logger.debug(f"Processing multi-onset for type {type_value}")
                        
                        # Extract all onset dates from the element
                        onset_dates = []
                        for field in onset_fields:
                            field_name = field.split(".")[-1] if "." in field else field
                            if field_name in element and element[field_name]:
                                onset_dates.append((field_name, element[field_name]))
                        
                        logger.debug(f"Found {len(onset_dates)} onset dates for type {type_value}")
                        
                        if onset_dates:
                            # Create a feature for each date
                            for field_name, date_value in onset_dates:
                                # Create a modified element with only this date
                                modified_element = element.copy()
                                
                                # Set all other date fields to empty
                                for other_field, _ in onset_dates:
                                    if other_field != field_name:
                                        modified_element[other_field] = ""
                                
                                # Create the feature with just this date
                                feature = self._create_phenotypic_feature(type_value, modified_element, dob, all_instruments)
                                if feature:
                                    features.append(feature)
                                    logger.debug(f"Added feature with onset date {date_value} for type {type_value}")
                        else:
                            # No dates, create a single feature
                            feature = self._create_phenotypic_feature(type_value, element, dob, all_instruments)
                            if feature:
                                features.append(feature)
                                logger.debug(f"Added single feature (no dates) for type {type_value}")
                    else:
                        # Standard single feature creation
                        feature = self._create_phenotypic_feature(type_value, element, dob, all_instruments)
                        if feature:
                            features.append(feature)
                            logger.debug(f"Added standard feature for type {type_value}")
                except Exception as e:
                    logger.error(f"Error processing type {type_value}: {str(e)}")
                    import traceback
                    logger.debug(traceback.format_exc())
        
        return features
    
    def _extract_type_values(self, data: Dict[str, Any], data_model: str, all_instruments: List[str]) -> List[str]:
        """
        Extract type values based on the data model configuration.
        
        Args:
            data (Dict[str, Any]): The data element
            data_model (str): Data model identifier
            all_instruments (List[str]): List of all instruments for field lookup
            
        Returns:
            List[str]: List of type values
        """
        # Check if we have type fields defined
        type_fields = self.processor.mapping_config.get("type_fields", [])
        
        # Storage for found type values
        type_values = []
        
        # If type_fields is explicitly defined, use them
        if type_fields:
            for field in type_fields:
                value = data.get(field)
                if value:
                    type_values.append(value)
            
            if type_values:
                return type_values
        
        # If no explicit type fields or no values found, try numbered fields
        for i in range(1, 20):  # Try type_field_1 through type_field_19
            field_key = f"type_field_{i}"
            if field_key in self.processor.mapping_config:
                field = self.processor.mapping_config[field_key]
                value = data.get(field)
                if value:
                    type_values.append(value)
        
        # If we found values from numbered fields, return them
        if type_values:
            return type_values
        
        # Try the primary type_field as fallback
        type_field = self.processor.mapping_config.get("type_field")
        if type_field:
            value = None
            
            # Try multi-instrument lookup if available
            if all_instruments:
                value = get_multi_instrument_field_value(
                    data=self.processor.mapping_config.get('full_data', {}),
                    instruments=all_instruments,
                    field_paths=[type_field]
                )
            
            # If not found or multi-instrument lookup not available, use direct field access
            if value is None:
                value = data.get(type_field)
            
            if value:
                type_values.append(value)
        
        return type_values
    
    def _create_phenotypic_feature(
        self, 
        feature_type: str, 
        feature_data: Dict[str, Any],
        dob: Optional[str] = None,
        all_instruments: Optional[List[str]] = None
    ) -> Optional[PhenotypicFeature]:
        """
        Create a PhenotypicFeature object from the provided data.
        Uses strict instance-based scoping to prevent modifier cross-contamination.
        
        Args:
            feature_type (str): Type value
            feature_data (Dict[str, Any]): Feature data
            dob (str, optional): Date of birth for age calculations
            all_instruments (List[str], optional): List of all instruments for field lookup
        """
        try:
            # Process type ID and label
            type_id = self.process_code(feature_type)
            type_label = self.fetch_label(feature_type)
            
            logger.debug(f"Creating feature for type: {feature_type} -> {type_id} ({type_label})")
            
            type_obj = create_ontology_class(type_id, type_label, "Unknown Phenotypic Feature")
            
            # Store the current instance in the processor config for reference
            if 'redcap_repeat_instance' in feature_data:
                self.processor.mapping_config['current_instance'] = feature_data.get('redcap_repeat_instance')
            
            # Extract feature properties with strict instance scoping
            excluded = self._extract_excluded_status(feature_data)
            onset = self._extract_onset(feature_data, dob)
            resolution = self._extract_resolution(feature_data, dob)
            severity = self._extract_severity(feature_data)
            evidence = self._extract_evidence(feature_data)
            
            # Extract modifiers using feature_type and data model
            modifiers = self._extract_modifiers(feature_data, feature_type)
            
            # Debug output to verify modifier scoping
            if modifiers:
                logger.debug(f"Feature {feature_type} has {len(modifiers)} modifiers: " + 
                            ", ".join([f"{m.id} ({m.label})" for m in modifiers]))
            
            # Check if multi-onset is enabled
            if self.processor.mapping_config.get("multi_onset", False):
                logger.debug(f"Multi-onset enabled for type {feature_type}")
                
                # Use the multi_onset_adapter to create multiple features if needed
                return multi_onset_adapter(
                    mapping_func=lambda t, d, p, b: PhenotypicFeature(
                        type=type_obj,
                        excluded=excluded,
                        onset=onset,
                        resolution=resolution,
                        severity=severity,
                        evidence=evidence,
                        modifiers=modifiers if modifiers else None
                    ),
                    feature_type=feature_type,
                    feature_data=feature_data,
                    processor=self.processor,
                    dob=dob
                )[0]  # Return the first feature
            else:
                # Create a standard single feature
                logger.debug(f"Creating standard single feature for type {feature_type}")
                return PhenotypicFeature(
                    type=type_obj,
                    excluded=excluded,
                    onset=onset,
                    resolution=resolution,
                    severity=severity,
                    evidence=evidence,
                    modifiers=modifiers if modifiers else None
                )
        except Exception as e:
            logger.error(f"Error creating phenotypic feature: {e}")
            import traceback
            logger.debug(traceback.format_exc())
            return None
    
    def _extract_excluded_status(self, feature_data: Dict[str, Any]) -> Optional[bool]:
        """
        Extract a Boolean 'excluded' status strictly from the local row's data.
        """
        excluded = None
        field = self.processor.mapping_config.get("excluded_field")
        if not field:
            return None
        
        # Only check local row
        val = feature_data.get(field)
        if val:
            mapped = self.fetch_mapping_value("phenotypic_feature_status", val)
            if mapped == "true":
                excluded = True
            elif mapped == "false":
                excluded = False
        return excluded

        
    def _extract_onset(self, 
                       feature_data: Dict[str, Any], 
                       dob: Optional[str] = None,
                       all_instruments: Optional[List[str]] = None
                        ) -> Optional[TimeElement]:
        """
        Simplified onset extraction:
        1) If onset_date_field can be parsed, return Age-based onset
        2) Else if onset_age_field is an HPO code, return a code-based onset
        3) Otherwise return None
        """
        from phenopackets import TimeElement, Age, OntologyClass

        if not dob:
            logger.debug("[_extract_onset] No DOB available, returning None.")
            return None

        date_field = self.processor.mapping_config.get("onset_date_field")      # e.g. "snomedct_8116006_onset"
        code_field = self.processor.mapping_config.get("onset_age_field")       # e.g. "hp_0003674"

        # 1) Try date_field first
        if date_field:
            date_str = feature_data.get(date_field)  # just read directly from the sub-dict
            logger.debug(f"[_extract_onset] Checking date_field={date_field}, value={date_str}")
            if date_str:
                iso_age = self.processor.convert_date_to_iso_age(date_str, dob)
                logger.debug(f"[_extract_onset] convert_date_to_iso_age => {iso_age}")
                if iso_age:
                    # Return a TimeElement with Age
                    return TimeElement(age=Age(iso8601duration=iso_age))

        # 2) Fallback to code_field
        if code_field:
            code_val = feature_data.get(code_field)
            logger.debug(f"[_extract_onset] Checking code_field={code_field}, value={code_val}")
            if code_val:
                code_id = self.process_code(code_val)
                code_label = self.fetch_label(code_val, enum_class="AgeOfOnset")
                logger.debug(f"[_extract_onset] fallback code => {code_id}, label => {code_label}")
                if code_label:
                    return TimeElement(ontology_class=OntologyClass(id=code_id, label=code_label))

        # 3) None if we can’t parse date or code
        logger.debug("[_extract_onset] No onset date or code found; returning None.")
        return None


        
    def _extract_resolution(self,
                            feature_data: Dict[str, Any],
                            dob: Optional[str] = None) -> Optional[TimeElement]:
        """
        Extract resolution date strictly from the local row's data, then
        convert it into a TimeElement based on DOB.
        """
        if not dob:
            return None
        
        field = self.processor.mapping_config.get("resolution_field")
        if not field:
            return None

        val = feature_data.get(field)  # local row only
        if not val:
            return None

        # Use your existing create_time_element or convert_date_to_iso_age
        return create_time_element(val, dob, self.processor)

    
    def _extract_severity(self, feature_data: Dict[str, Any]) -> Optional[OntologyClass]:
        """
        Extract severity strictly from the local row's data.
        """
        from phenopackets import OntologyClass

        field = self.processor.mapping_config.get("severity_field")
        if not field:
            return None
        
        val = feature_data.get(field)  # local row only
        if not val:
            return None

        sid = self.process_code(val)
        label = self.fetch_label(val, enum_class="PhenotypeSeverity")
        if label:
            return OntologyClass(id=sid, label=label)
        return None
        
    def _extract_evidence(self, feature_data: Dict[str, Any]) -> Optional[List[Evidence]]:
        """
        Extract 'evidence' strictly from the local row's data.
        """
        from phenopackets import Evidence, OntologyClass

        evidence_list = None
        field = self.processor.mapping_config.get("evidence_field")
        if not field:
            return None
        
        val = feature_data.get(field)  # local row only
        if val:
            eid = self.process_code(val)
            label = self.fetch_label(val)
            ev_obj = Evidence(evidence_code=OntologyClass(id=eid, label=label or "Unknown Evidence"))
            evidence_list = [ev_obj]
        return evidence_list

    
    def _extract_modifiers(
        self,
        feature_data: Dict[str, Any],
        feature_type: Optional[str] = None
    ) -> List[OntologyClass]:
        """
        Extract modifiers strictly from the current row's data (feature_data),
        so that each repeated element can have distinct modifiers.
        """
        from phenopackets import OntologyClass

        modifiers = []
        modifier_ids = set()  # Avoid duplicates
        data_model = self.processor.mapping_config.get("data_model", "")

        def add_modifier(id_value: str, label: Optional[str]):
            # Only add if this ID hasn't been used yet
            if id_value and id_value not in modifier_ids:
                modifiers.append(OntologyClass(id=id_value, label=label or "Unknown Modifier"))
                modifier_ids.add(id_value)

        # 1) Temporal Pattern field
        temp_pattern_field = self.processor.mapping_config.get("modifier_temp_pattern_field")
        if temp_pattern_field:
            tp_val = feature_data.get(temp_pattern_field)
            if tp_val:
                tp_id = self.process_code(tp_val)
                tp_label = self.fetch_label(tp_val, enum_class="TemporalPattern")
                if tp_label:
                    add_modifier(tp_id, tp_label)

        # 2) Up to 9 generic modifier fields
        for i in range(1, 10):
            field_key = f"modifier_field_{i}"
            field_name = self.processor.mapping_config.get(field_key)
            if field_name:
                val = feature_data.get(field_name)
                if val:
                    mid = self.process_code(val)
                    label = self.fetch_label(val)
                    if label:
                        add_modifier(mid, label)

        # 3) Data‐model‐specific logic: "infections"
        if data_model == "infections":
            # Possibly check local fields like causing_agent_viral, etc.
            organism_fields = ["causing_agent_viral", "causing_agent_bacterial", "causing_agent_mycotic"]
            for org_field in organism_fields:
                if org_field in feature_data and feature_data[org_field]:
                    org_val = feature_data[org_field]
                    # Skip numeric values which might be enumerations
                    if not isinstance(org_val, (int, float)) and not (isinstance(org_val, str) and org_val.isdigit()):
                        org_id = self.process_code(org_val)
                        org_label = self.fetch_label(org_val)
                        if org_label:
                            add_modifier(org_id, org_label)

        # 4) Data‐model‐specific logic: "conditions"
        elif data_model == "conditions":
            # For each local field, if it ends with "_modifier" and matches feature_type, add it
            for key, val in feature_data.items():
                if key.endswith("_modifier") and val:
                    type_base = feature_type.split(":")[-1] if (feature_type and ":" in feature_type) else feature_type
                    if type_base and "_" in type_base:
                        type_base = type_base.split("_")[-1]

                    if feature_type and (feature_type in key or (type_base and type_base in key)):
                        mod_id = self.process_code(val)
                        mod_label = self.fetch_label(val)
                        if mod_label:
                            add_modifier(mod_id, mod_label)

        # 5) RareLink or other data_model
        #    If you need to do anything special for data_model == "" or "rarelink_cdm",
        #    do that here. Right now, we simply pass.

        return modifiers
