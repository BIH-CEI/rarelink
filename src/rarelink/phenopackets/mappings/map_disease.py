import logging
from phenopackets import Disease, OntologyClass, TimeElement, Age
from rarelink.utils.processor import DataProcessor
from google.protobuf.timestamp_pb2 import Timestamp

logger = logging.getLogger(__name__)

def map_diseases(
    data: dict, 
    processor: DataProcessor,
    dob: str
    ) -> list:
    """
    Maps disease data to the Phenopacket schema Disease block fetching the 
    data elements from the repeated elements in the input data.

    Args:
        data (dict): Input data from the RareLink-CDM schema (or similar).
        processor (DataProcessor): Handles all data processing logic.

    Returns:
        list: A list of Phenopacket Disease blocks.
    """
    
    # Fetching and preparation
    # --------------------------------------------------------------------------
    instrument_name = processor.mapping_config.get("redcap_repeat_instrument")
    try:
        repeated_elements = data.get("repeated_elements", [])
        if not repeated_elements:
            logger.warning("No repeated elements found in the data.")
            return []

        disease_elements = [
            element for element in repeated_elements
            if element.get("redcap_repeat_instrument") == instrument_name
        ]
        
        diseases = []
        for disease_element in disease_elements:
            disease_data = disease_element.get("disease")
            if not disease_data:
                logger.warning("No disease data found in "
                               "this element. Skipping.")
                continue
            
            # Disease.term
            # ------------------------------------------------------------------
            term_id = (
                disease_data.get(processor.mapping_config["term_field_1"]) or
                disease_data.get(processor.mapping_config["term_field_2"]) or
                disease_data.get(processor.mapping_config["term_field_3"]) or
                disease_data.get(processor.mapping_config["term_field_4"]) or
                disease_data.get(processor.mapping_config["term_field_5"])
            )
            term_label = processor.fetch_label(term_id)
            term = OntologyClass(id=term_id, label=term_label)


            # Disease.onset[0..1] ( -> prefer date over category)
            # ------------------------------------------------------------------
            onset_date = disease_data.get(
                processor.mapping_config["onset_date_field"])
            onset_category_field = disease_data.get(
                processor.mapping_config["onset_category_field"])
            onset = None

            if onset_date:
                try:
                    # Validate the onset_date using process_date (this ensures a valid ISO8601 date)
                    _ = processor.process_date(onset_date)
                    
                    # Ensure dob is an ISO8601 string.
                    if not isinstance(dob, str):
                        dob_str = dob.ToDatetime().isoformat()
                    else:
                        dob_str = dob

                    # Calculate the ISO8601 duration using only years and months.
                    iso_age = processor.convert_date_to_iso_age(onset_date, dob_str)
                    # Create the TimeElement with the age element.
                    onset = TimeElement(age=Age(iso8601duration=iso_age))
                except Exception as e:
                    logger.error(f"Error processing onset date for ISO age: {e}")

            if not onset and onset_category_field:
                try:
                    onset_label = processor.fetch_label(
                        onset_category_field, enum_class="AgeAtOnset")
                    onset_category = processor.process_code(
                        onset_category_field)
                    
                    if onset_label:
                        onset = TimeElement(
                            ontology_class=OntologyClass(
                                id=onset_category, label=onset_label)
                        )
                    else:
                        logger.warning(
                            f"No label found for onset category \
                                '{onset_category}'.")
                except Exception as e:
                        logger.error(
                            f"Error processing onset category \
                                '{onset_category}': {e}")
                    
            # Disease.excluded
            # ------------------------------------------------------------------
            excluded_value = disease_data.get(
                processor.mapping_config["excluded_field"])
            excluded = None
            if excluded_value:
                mapped_value = processor.fetch_mapping_value(
                    "map_disease_verification_status", excluded_value)
                logger.debug(f"Excluded value: {excluded_value},\
                                Mapped value: {mapped_value}")
                if mapped_value == "true":
                    excluded = True
                else:
                    excluded = None # default value in Phenopackets

            # Disease.primary_site
            # ------------------------------------------------------------------
            primary_site_id = disease_data.get(
                processor.mapping_config["primary_site_field"])
            primary_site = None
            if primary_site_id:
                primary_site_label = processor.fetch_label(primary_site_id)
                primary_site = OntologyClass(
                    id=primary_site_id, 
                    label=primary_site_label)

            # Create the Disease block
            # ------------------------------------------------------------------
            disease = Disease(
                term=term,
                onset=onset,
                excluded=excluded,
                primary_site=primary_site,
            )

            diseases.append(disease)

        return diseases

    except Exception as e:
        logger.error(f"Failed to map diseases: {e}")
        raise
