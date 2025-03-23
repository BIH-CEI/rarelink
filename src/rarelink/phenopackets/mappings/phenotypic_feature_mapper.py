from typing import Dict, Any, Optional, List, Callable
import logging
from phenopackets import PhenotypicFeature, OntologyClass, TimeElement, Evidence

from rarelink.phenopackets.mappings.base_mapper import BaseMapper
from rarelink.utils.processor import DataProcessor
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
    Supports multiple instruments and data models including infections and conditions.
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
        
        # Add default configuration for RareLink CDM if not specified
        if "redcap_repeat_instrument" not in self.processor.mapping_config:
            self.processor.mapping_config["redcap_repeat_instrument"] = "rarelink_6_2_phenotypic_feature"
        
        # Add default field mappings if not in configuration
        if "type_field" not in self.processor.mapping_config:
            self.processor.mapping_config["type_field"] = "snomedct_8116006"
        
        if "onset_date_field" not in self.processor.mapping_config:
            self.processor.mapping_config["onset_date_field"] = "snomedct_8116006_onset"
            
        if "resolution_field" not in self.processor.mapping_config:
            self.processor.mapping_config["resolution_field"] = "snomedct_8116006_resolut"
            
        if "evidence_field" not in self.processor.mapping_config:
            self.processor.mapping_config["evidence_field"] = "phenotypicfeature_evidence"
        

 
        
        # Call the base map method which will call _map_multi_entity
        return super().map(data, **kwargs)
    
    def _map_single_entity(self, data: Dict[str, Any], instruments: List[str], **kwargs) -> Optional[PhenotypicFeature]:
        """
        Map data to a single PhenotypicFeature entity.
        Note: This method is required by the BaseMapper interface but not directly used
        since we always return multiple entities.
        
        Args:
            data (Dict[str, Any]): Input data to map
            instruments (List[str]): List of instruments for field access
            **kwargs: Additional mapping parameters
                - dob (str, optional): Date of birth for age calculations
            
        Returns:
            Optional[PhenotypicFeature]: None as this mapper always returns multiple entities
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
            
        Returns:
            List[PhenotypicFeature]: List of mapped PhenotypicFeature entities
        """
        dob = kwargs.get('dob')
        features = []
        
        try:
            # Store all instruments in the mapping config for field access
            self.processor.mapping_config["all_instruments"] = instruments
            
            # Make sure the RareLink phenotypic feature instrument is included
            rarelink_instrument = "rarelink_6_2_phenotypic_feature"
            if rarelink_instrument not in instruments:
                instruments.append(rarelink_instrument)
                
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
                logger.debug(f"Found {len(features)} features with direct approach")
                return features
                
            # Check if this is a direct single instrument configuration
            current_instrument = self.processor.mapping_config.get("current_instrument") or self.processor.mapping_config.get("redcap_repeat_instrument")
            if current_instrument:
                logger.info(f"Processing single instrument: {current_instrument}")
                data_model = self._determine_data_model(current_instrument)
                logger.debug(f"Using data model: {data_model} with instrument: {current_instrument}")
                
                # Choose the type extractor based on the model
                type_extractor = self._get_type_extractor_for_model(data_model)
                
                # Map features for this instrument
                if current_instrument not in instruments:
                    instruments.append(current_instrument)
                
                features = self._map_features_for_instrument(data, current_instrument, type_extractor, dob, instruments)
                logger.debug(f"Found {len(features)} features for instrument {current_instrument}")
                return features
            
            # Handle multiple instruments case
            # First, check if we have instrument-specific configs
            instrument_configs = self.processor.mapping_config.get("instrument_configs", {})
            if instrument_configs:
                logger.debug(f"Using instrument-specific configs for {len(instrument_configs)} instruments")
                
                for instrument_name, config in instrument_configs.items():
                    # Skip if instrument is not in our instruments list
                    if instrument_name not in instruments:
                        continue
                        
                    # Create a new processor with this config
                    instrument_processor = DataProcessor(mapping_config={
                        **self.processor.mapping_config,  # Base config
                        **config,                       # Instrument-specific overrides
                        "redcap_repeat_instrument": instrument_name,
                        "current_instrument": instrument_name,
                        "all_instruments": instruments
                    })
                    
                    # Copy over enum classes
                    for prefix, enum_class in getattr(self.processor, "enum_classes", {}).items():
                        instrument_processor.add_enum_class(prefix, enum_class)
                    
                    # Create a temporary mapper for this processor
                    temp_mapper = PhenotypicFeatureMapper(instrument_processor)
                    
                    # Map features for this instrument
                    instrument_features = temp_mapper._map_multi_entity(data, instruments, dob=dob)
                    features.extend(instrument_features)
                    
                return features
            
            # If no instrument-specific configs, process all instruments with the current processor
            for instrument_name in instruments:
                data_model = self._determine_data_model(instrument_name)
                type_extractor = self._get_type_extractor_for_model(data_model)
                
                # Map features for this instrument
                instrument_features = self._map_features_for_instrument(data, instrument_name, type_extractor, dob, instruments)
                features.extend(instrument_features)
                logger.debug(f"Added {len(instrument_features)} features from instrument {instrument_name}")
                
            logger.debug(f"Total phenotypic features mapped: {len(features)}")
            return features
                
        except Exception as e:
            logger.error(f"Error mapping phenotypic features: {e}")
            import traceback
            logger.debug(traceback.format_exc())
            return []
    
    def _map_features_for_instrument(
        self, 
        data: Dict[str, Any], 
        instrument_name: str,
        type_extractor: Callable,
        dob: str,
        all_instruments: List[str]
    ) -> List[PhenotypicFeature]:
        """
        Map features for a specific instrument using the given type extractor.
        
        Args:
            data (Dict[str, Any]): Input data to map
            instrument_name (str): Name of the instrument
            type_extractor (Callable): Function to extract type values
            dob (str): Date of birth for age calculations
            all_instruments (List[str]): List of all instruments for field lookup
            
        Returns:
            List[PhenotypicFeature]: List of mapped PhenotypicFeature entities
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
            # Extract type values using the provided extractor
            type_values = type_extractor(element, self.processor, all_instruments)
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
                                    # Ensure each feature has only the appropriate modifiers
                                    # This is especially important for multi-onset features
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
            
        Returns:
            Optional[PhenotypicFeature]: The created feature or None on failure
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
            excluded = self._extract_excluded_status(feature_data, all_instruments)
            onset = self._extract_onset(feature_data, dob, all_instruments)
            resolution = self._extract_resolution(feature_data, dob, all_instruments)
            severity = self._extract_severity(feature_data, all_instruments)
            evidence = self._extract_evidence(feature_data, all_instruments)
            
            # Extract modifiers with feature_type to ensure proper scoping
            modifiers = self._extract_modifiers(feature_data, feature_type, all_instruments)
            
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
                )[0]  # Return the first feature - multi_onset_adapter will be called again for each date
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
    
    def _extract_excluded_status(
        self, 
        data: Dict[str, Any],
        all_instruments: Optional[List[str]] = None
    ) -> Optional[bool]:
        """Extract excluded status from data"""
        excluded = None
        field = self.processor.mapping_config.get("excluded_field")
        if field:
            val = None
            
            # Try multi-instrument lookup if available
            if all_instruments:
                val = get_multi_instrument_field_value(
                    data=self.processor.mapping_config.get('full_data', {}),
                    instruments=all_instruments,
                    field_paths=[field]
                )
            
            # If not found, use direct field access
            if val is None:
                val = data.get(field)
            
            if val:
                mapped = self.fetch_mapping_value("phenotypic_feature_status", val)
                if mapped == "true":
                    excluded = True
                elif mapped == "false":
                    excluded = False
        return excluded
    
    def _extract_onset(
        self, 
        data: Dict[str, Any],
        dob: Optional[str] = None,
        all_instruments: Optional[List[str]] = None
    ) -> Optional[TimeElement]:
        """Extract onset from data"""
        if not dob:
            return None
            
        onset = None
        field = self.processor.mapping_config.get("onset_date_field")
        alt_field = self.processor.mapping_config.get("onset_age_field")
        
        if field:
            val = None
            
            # Try multi-instrument lookup if available
            if all_instruments:
                val = get_multi_instrument_field_value(
                    data=self.processor.mapping_config.get('full_data', {}),
                    instruments=all_instruments,
                    field_paths=[field]
                )
            
            # If not found, use direct field access
            if val is None:
                val = data.get(field)
            
            if val:
                onset = create_time_element(val, dob, self.processor)
        
        if not onset and alt_field:
            alt_val = None
            
            # Try multi-instrument lookup if available
            if all_instruments:
                alt_val = get_multi_instrument_field_value(
                    data=self.processor.mapping_config.get('full_data', {}),
                    instruments=all_instruments,
                    field_paths=[alt_field]
                )
            
            # If not found, use direct field access
            if alt_val is None:
                alt_val = data.get(alt_field)
            
            if alt_val:
                label = self.fetch_label(alt_val, enum_class="AgeOfOnset")
                pid = self.process_code(alt_val)
                if label:
                    onset = TimeElement(ontology_class=OntologyClass(id=pid, label=label))
        
        return onset
    
    def _extract_resolution(
        self, 
        data: Dict[str, Any],
        dob: Optional[str] = None,
        all_instruments: Optional[List[str]] = None
    ) -> Optional[TimeElement]:
        """Extract resolution from data"""
        if not dob:
            return None
            
        resolution = None
        field = self.processor.mapping_config.get("resolution_field")
        
        if field:
            val = None
            
            # Try multi-instrument lookup if available
            if all_instruments:
                val = get_multi_instrument_field_value(
                    data=self.processor.mapping_config.get('full_data', {}),
                    instruments=all_instruments,
                    field_paths=[field]
                )
            
            # If not found, use direct field access
            if val is None:
                val = data.get(field)
            
            if val:
                resolution = create_time_element(val, dob, self.processor)
        
        return resolution
    
    def _extract_severity(
        self, 
        data: Dict[str, Any],
        all_instruments: Optional[List[str]] = None
    ) -> Optional[OntologyClass]:
        """Extract severity from data"""
        severity = None
        field = self.processor.mapping_config.get("severity_field")
        
        if field:
            val = None
            
            # Try multi-instrument lookup if available
            if all_instruments:
                val = get_multi_instrument_field_value(
                    data=self.processor.mapping_config.get('full_data', {}),
                    instruments=all_instruments,
                    field_paths=[field]
                )
            
            # If not found, use direct field access
            if val is None:
                val = data.get(field)
            
            if val:
                sid = self.process_code(val)
                label = self.fetch_label(val, enum_class="PhenotypeSeverity")
                if label:
                    severity = OntologyClass(id=sid, label=label)
        
        return severity
    
    def _extract_evidence(
        self, 
        data: Dict[str, Any],
        all_instruments: Optional[List[str]] = None
    ) -> Optional[List[Evidence]]:
        """Extract evidence from data"""
        evidence_list = None
        field = self.processor.mapping_config.get("evidence_field")
        
        if field:
            val = None
            
            # Try multi-instrument lookup if available
            if all_instruments:
                val = get_multi_instrument_field_value(
                    data=self.processor.mapping_config.get('full_data', {}),
                    instruments=all_instruments,
                    field_paths=[field]
                )
            
            # If not found, use direct field access
            if val is None:
                val = data.get(field)
            
            if val:
                eid = self.process_code(val)
                label = self.fetch_label(val)
                evidence = Evidence(evidence_code=OntologyClass(id=eid, label=label or "Unknown Evidence"))
                evidence_list = [evidence]
        
        return evidence_list
    
    def _extract_modifiers(
        self, 
        data: Dict[str, Any],
        feature_type: str = None,
        all_instruments: Optional[List[str]] = None
    ) -> List[OntologyClass]:
        """
        Extract modifiers that are specific to the current feature instance.
        This method strictly scopes modifiers to prevent cross-contamination.
        """
        modifiers = []
        
        # Get data model type
        data_model = self.processor.mapping_config.get("data_model", "")
        
        # Get current instance information
        current_instance = None
        current_instrument = None
        
        # For RareLink CDM data model
        if data_model == "" or data_model == "rarelink_cdm":
            # Extract modifiers for RareLink CDM model
            
            # 1. First get the current instance and instrument
            if 'redcap_repeat_instance' in data:
                current_instance = data.get('redcap_repeat_instance')
            else:
                # Try to get it from the context
                for element in self.processor.mapping_config.get('full_data', {}).get('repeated_elements', []):
                    if 'phenotypic_feature' in element and any(
                        feature_type == element['phenotypic_feature'].get('snomedct_8116006', '')
                        for feature_type in [feature_type]
                    ):
                        current_instance = element.get('redcap_repeat_instance')
                        current_instrument = element.get('redcap_repeat_instrument')
                        break
            
            # 2. Now extract modifiers specifically for this instance
            if current_instance is not None:
                full_data = self.processor.mapping_config.get('full_data', {})
                
                # Look for the correct element in repeated_elements
                for element in full_data.get('repeated_elements', []):
                    if (element.get('redcap_repeat_instance') == current_instance and
                        (element.get('redcap_repeat_instrument') == 'rarelink_6_2_phenotypic_feature' or
                        element.get('redcap_repeat_instrument') == current_instrument)):
                        
                        # Get the phenotypic feature data
                        phenotypic_feature = element.get('phenotypic_feature', {})
                        
                        # Extract temporal pattern modifier
                        temp_pattern_field = self.processor.mapping_config.get("modifier_temp_pattern_field", "hp_0011008")
                        if temp_pattern_field in phenotypic_feature and phenotypic_feature[temp_pattern_field]:
                            tp_val = phenotypic_feature[temp_pattern_field]
                            tp_id = self.process_code(tp_val)
                            tp_label = self.fetch_label(tp_val, enum_class="TemporalPattern")
                            if tp_label:
                                modifiers.append(OntologyClass(id=tp_id, label=tp_label))
                        
                        # Extract modifiers from specific fields
                        modifier_fields = [
                            ("modifier_field_1", "hp_0012823_hp1"),
                            ("modifier_field_2", "hp_0012823_hp2"),
                            ("modifier_field_3", "hp_0012823_hp3"),
                            ("modifier_field_4", "hp_0012823_ncbitaxon"),
                            ("modifier_field_5", "hp_0012823_snomed")
                        ]
                        
                        for config_key, field_name in modifier_fields:
                            field = self.processor.mapping_config.get(config_key, field_name)
                            if field in phenotypic_feature and phenotypic_feature[field]:
                                val = phenotypic_feature[field]
                                if val:
                                    mid = self.process_code(val)
                                    label = self.fetch_label(val)
                                    if label:
                                        modifiers.append(OntologyClass(id=mid, label=label))
                        
                        # We found our instance, no need to continue searching
                        break
            
            # If no modifiers found through the strict instance method, try the direct field approach
            # but only if data appears to be from the phenotypic feature itself, not a parent element
            if not modifiers and 'snomedct_8116006' in data:
                # Extract temporal pattern modifier
                temp_pattern_field = self.processor.mapping_config.get("modifier_temp_pattern_field", "hp_0011008")
                if temp_pattern_field in data and data[temp_pattern_field]:
                    tp_val = data[temp_pattern_field]
                    tp_id = self.process_code(tp_val)
                    tp_label = self.fetch_label(tp_val, "TemporalPattern")
                    if tp_label:
                        modifiers.append(OntologyClass(id=tp_id, label=tp_label))
                
                # Extract modifiers from specific fields
                for i in range(1, 6):
                    field_key = f"modifier_field_{i}"
                    field = self.processor.mapping_config.get(field_key)
                    if field and field in data and data[field]:
                        val = data[field]
                        if val:
                            mid = self.process_code(val)
                            label = self.fetch_label(val)
                            if label:
                                modifiers.append(OntologyClass(id=mid, label=label))
        
        # CIEINR data model handling
        elif data_model in ["infections", "conditions"]:
            # Add temporal pattern if present
            temp_pattern_field = self.processor.mapping_config.get("modifier_temp_pattern_field", "")
            if temp_pattern_field and temp_pattern_field in data and data[temp_pattern_field]:
                tp_val = data[temp_pattern_field]
                tp_id = self.process_code(tp_val)
                tp_label = self.fetch_label(tp_val, "TemporalPattern")
                if tp_label:
                    modifiers.append(OntologyClass(id=tp_id, label=tp_label))
            
            # Add type-specific category as a modifier if it's different from the feature type
            category_field = "type_of_infection" if data_model == "infections" else "type_of_condition"
            if category_field in data and data[category_field]:
                cat_val = data[category_field]
                if cat_val != feature_type:  # Only add if different from the feature
                    cat_id = self.process_code(cat_val)
                    cat_label = self.fetch_label(cat_val)
                    if cat_label:
                        modifiers.append(OntologyClass(id=cat_id, label=cat_label))
            
            # For infections model, add organism modifiers
            if data_model == "infections":
                # Check organism fields
                organism_fields = [
                    ("causing_agent_viral", True),
                    ("causing_agent_bacterial", True),
                    ("causing_agent_mycotic", True),
                    ("causing_agent", False)  # False means it's not an index
                ]
                
                for field, is_index in organism_fields:
                    if field in data and data[field]:
                        org_val = data[field]
                        # Skip numeric values which may be enum indexes
                        if is_index and (isinstance(org_val, (int, float)) or 
                                        (isinstance(org_val, str) and org_val.isdigit())):
                            continue
                        
                        org_id = self.process_code(org_val)
                        org_label = self.fetch_label(org_val)
                        if org_label:
                            modifiers.append(OntologyClass(id=org_id, label=org_label))
            
            # For conditions model, add specific modifiers for this feature type
            elif data_model == "conditions":
                # Extract the type base (without prefix)
                type_base = feature_type.split(":")[-1] if ":" in feature_type else feature_type
                type_base = type_base.split("_")[-1] if "_" in type_base else type_base
                
                # Check for fields with pattern hp_XXXXX_modifier where XXXXX matches the feature type
                for key, value in data.items():
                    if key.endswith("_modifier") and value:
                        # Check if the key contains the feature type or is directly related to this feature
                        if (feature_type in key or type_base in key or
                            # For specific known mappings
                            (feature_type == "HP:0012539" and key == "hp_0012539_modifier") or
                            (feature_type == "HP:0012189" and key == "hp_0012189_modifier") or
                            (feature_type == "HP:0005523" and key == "hp_0005523_modifier")):
                            
                            mod_id = self.process_code(value)
                            mod_label = self.fetch_label(value)
                            if mod_label:
                                modifiers.append(OntologyClass(id=mod_id, label=mod_label))
        
        return modifiers
    
    def _determine_data_model(self, instrument_name: str) -> str:
        """Determine the data model based on the instrument name"""
        # Check for explicitly defined model in the configuration
        explicit_model = self.processor.mapping_config.get("data_model")
        if explicit_model:
            logger.debug(f"Using explicitly defined data model: {explicit_model}")
            return explicit_model
        
        # Check for multiple type fields which suggests a multi-field form
        has_multiple_type_fields = any(f"type_field_{i}" in self.processor.mapping_config for i in range(2, 20))
        
        # Check instrument name patterns
        is_infection = (
            "infection" in instrument_name.lower() or 
            instrument_name == "infections_initial_form"
        )
        
        is_condition = (
            "systemic" in instrument_name.lower() or
            "organ_specific" in instrument_name.lower() or
            "condition" in instrument_name.lower() or
            "patients_systemic_or_organ_specific_conditions" == instrument_name
        )
        
        # Determine model based on checks
        if is_infection:
            return "infections"
        elif is_condition:
            return "conditions"
        elif has_multiple_type_fields:
            # If multiple type fields but not identified as infections or conditions,
            # default to multi-field type
            return "multi_field"
        else:
            return "rarelink_cdm"
    
    def _get_type_extractor_for_model(self, data_model: str) -> Callable:
        """Get the appropriate type extractor for the data model"""
        if data_model == "infections":
            return self._get_infection_types
        elif data_model == "conditions":
            return self._get_condition_types
        else:
            return self._get_single_type
    
    def _get_single_type(self, data: Dict[str, Any], processor: DataProcessor, all_instruments: List[str] = None) -> List[str]:
        """Extract a single type value from data"""
        # Check for specific type fields
        type_values = []
        
        # Check if we have type fields defined
        type_fields = processor.mapping_config.get("type_fields", [])
        if type_fields:
            # If we have explicitly defined type fields, use those
            for field in type_fields:
                value = data.get(field)
                if value:
                    logger.debug(f"Found value '{value}' for explicit type field '{field}'")
                    type_values.append(value)
            
            if type_values:
                return type_values
        
        # If no explicit type fields or no values found, try the type_field
        type_field = processor.mapping_config.get("type_field", "snomedct_8116006")
        if not type_field:
            logger.debug("No type field configured")
            return []
        
        value = None
        
        # Try multi-instrument lookup first if available
        if all_instruments:
            value = get_multi_instrument_field_value(
                data=processor.mapping_config.get('full_data', {}),
                instruments=all_instruments,
                field_paths=[type_field]
            )
        
        # If not found or multi-instrument lookup not available, use direct field access
        if value is None:
            value = data.get(type_field)
        
        if not value:
            # Try type_field_2, type_field_3, etc. if defined
            for i in range(2, 20):  # Check up to type_field_19
                field_key = f"type_field_{i}"
                if field_key in processor.mapping_config:
                    field = processor.mapping_config[field_key]
                    value = data.get(field)
                    if value:
                        logger.debug(f"Found value {value} for field {field}")
                        return [value]
            
            logger.debug(f"No value found for type field '{type_field}' or alternates")
            return []
        
        logger.debug(f"Found type value: {value}")
        return [value]
    
    def _get_infection_types(self, data: Dict[str, Any], processor: DataProcessor, all_instruments: List[str] = None) -> List[str]:
        """
        Extract infection type values from the data.
        Handles fields for different types of infections.
        
        Args:
            data (Dict[str, Any]): The data element to extract from
            processor (DataProcessor): The data processor with configuration
            all_instruments (List[str], optional): List of all instruments for field lookup
            
        Returns:
            List[str]: A list of infection type values
        """
        # Define infection type fields to check
        infection_type_fields = processor.mapping_config.get("type_fields", [
            "snomedct_61274003",   # Opportunistic infections
            "snomedct_21483005",   # CNS infections
            "snomedct_81745001",   # Eye infections
            "snomedct_385383008",  # ENT infections
            "snomedct_127856007",  # Skin/soft tissue
            "snomedct_110522009",  # Bone/joint
            "snomedct_20139000",   # Respiratory
            "snomedct_303699009",  # GI
            "snomedct_21514008",   # GU
            "snomedct_31099001",   # Systemic
            "other_infection_hpo",
            "other_infection_mondo"
        ])
        
        # Storage for found type values
        type_values = []
        
        # Check each field directly in the data
        if isinstance(data, dict):
            for field in infection_type_fields:
                if field in data and data[field]:
                    value = data[field]
                    logger.debug(f"Found field '{field}' with value '{value}'")
                    
                    if isinstance(value, str) and (
                        value.startswith("hp_") or 
                        value.startswith("mondo_") or 
                        value.startswith("snomedct_") or
                        ":" in value
                    ):
                        logger.debug(f"Found valid infection type value '{value}' for field '{field}'")
                        type_values.append(value)
                    else:
                        logger.debug(f"ERROR: Value '{value}' for field '{field}' is not a valid type code")
        
        return type_values
    
    def _get_condition_types(self, data: Dict[str, Any], processor: DataProcessor, all_instruments: List[str] = None) -> List[str]:
        """
        Extract condition type values from the data.
        Handles fields for different types of conditions.
        
        Args:
            data (Dict[str, Any]): The data element to extract from
            processor (DataProcessor): The data processor with configuration
            all_instruments (List[str], optional): List of all instruments for field lookup
            
        Returns:
            List[str]: A list of condition type values
        """
        # Define condition type fields to check
        condition_type_fields = processor.mapping_config.get("type_fields", [
            "snomedct_128477000",  # Systemic condition
            "snomedct_95320005",   # Allergy
            "snomedct_118938008",  # Neoplasm
            "snomedct_50043002",   # Endocrine disorder
            "snomedct_49601007",   # Cardiovascular disorder
            "mondo_0005570",       # Autoimmune disorder
            "snomedct_928000",     # Gastrointestinal disorder
            "snomedct_119292006",  # Genitourinary disorder
            "snomedct_362969004",  # Metabolic disorder
            "snomedct_42030000",   # Renal system disorder
            "snomedct_55342001",   # Skeletal disorder
            "snomedct_85828009",   # Trauma
            "hp_0025142",          # Constitutional symptom
            "snomedct_5294002",    # Developmental delay
            "condition_other_hp"
        ])
        
        # Storage for found type values
        type_values = []
        
        # Check each field directly in the data
        if isinstance(data, dict):
            for field in condition_type_fields:
                if field in data and data[field]:
                    value = data[field]
                    logger.debug(f"Found field '{field}' with value '{value}'")
                    
                    if isinstance(value, str) and (
                        value.startswith("hp_") or 
                        value.startswith("mondo_") or 
                        value.startswith("snomedct_") or
                        ":" in value
                    ):
                        logger.debug(f"Found valid condition type value '{value}' for field '{field}'")
                        type_values.append(value)
                    else:
                        logger.debug(f"ERROR: Value '{value}' for field '{field}' is not a valid type code")
        
        return type_values