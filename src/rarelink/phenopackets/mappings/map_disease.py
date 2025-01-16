import logging
from phenopackets import Disease, OntologyClass, TimeElement
from rarelink.utils.processor import DataProcessor
from google.protobuf.timestamp_pb2 import Timestamp
from rarelink_cdm.v2_0_0_dev0.mappings.phenopackets.mapping_dicts import get_mapping_by_name

logger = logging.getLogger(__name__)

def map_onset(disease_data: dict, processor: DataProcessor, date_field: str, category_field: str) -> TimeElement:
    """
    Maps onset information, preferring the date field over the category field.

    Args:
        disease_data (dict): The input dictionary containing disease data.
        processor (DataProcessor): The data processor for handling fields and mappings.
        date_field (str): Field name for the onset date.
        category_field (str): Field name for the onset category.

    Returns:
        TimeElement: A Phenopacket TimeElement or None if no onset data is available.
    """
    # Attempt to map onset using date
    onset_date = disease_data.get(date_field)
    if onset_date:
        try:
            timestamp = processor.process_date(onset_date)
            return TimeElement(timestamp=timestamp)
        except Exception as e:
            logger.error(f"Error processing onset date '{onset_date}': {e}")

    # Attempt to map onset using category
    onset_category = disease_data.get(category_field)
    if onset_category:
        try:
            category_label = processor.fetch_label(onset_category)
            return TimeElement(
                ontology_class=OntologyClass(id=onset_category, label=category_label)
            )
        except Exception as e:
            logger.error(f"Error processing onset category '{onset_category}': {e}")

    return None

def map_diseases(
    data: dict, 
    processor: DataProcessor) -> list:
    """
    Maps disease data directly using a hardcoded approach for extracting and processing.

    Args:
        data (dict): Input data from the RareLink-CDM schema (or similar).
        processor (DataProcessor): Handles all data processing logic.

    Returns:
        list: A list of Phenopacket Disease blocks.
    """
    try:
        repeated_elements = data.get("repeated_elements", [])
        if not repeated_elements:
            logger.warning("No repeated elements found in the data.")
            return []

        # Filter relevant disease elements
        disease_elements = [
            element for element in repeated_elements
            if element.get("redcap_repeat_instrument") == "rarelink_5_disease"
        ]

        diseases = []
        for disease_element in disease_elements:
            disease_data = disease_element.get("disease")
            if not disease_data:
                logger.warning("No disease data found in this element. Skipping.")
                continue

            # Extract term fields (pick the first non-empty)
            term_id = (
                disease_data.get("snomed_64572001_mondo") or
                disease_data.get("snomed_64572001_ordo") or
                disease_data.get("snomed_64572001_icd10cm") or
                disease_data.get("snomed_64572001_icd11") or
                disease_data.get("snomed_64572001_omim_p")
            )
            if not term_id:
                logger.warning("No valid term ID found for disease. Skipping.")
                continue

            term_label = processor.fetch_label(term_id)
            term = OntologyClass(id=term_id, label=term_label)

            # Handle onset (prefer date over category)
            onset_date = disease_data.get("snomed_298059007")
            onset_category = disease_data.get(processor.process_code("snomed_424850005"))
            onset = None

            if onset_date:
                try:
                    # Process onset_date into a protobuf Timestamp
                    timestamp = processor.process_date(onset_date)
                    if isinstance(timestamp, Timestamp):
                        onset = TimeElement(timestamp=timestamp)
                    else:
                        raise TypeError("Processed date is not a Timestamp object.")
                except Exception as e:
                    logger.error(f"Error processing onset date: {e}")

            elif onset_category:
                try:
                    onset_label = processor.fetch_label(onset_category)
                    onset = TimeElement(
                        ontology_class=OntologyClass(id=onset_category, label=onset_label)
                    )
                except Exception as e:
                    logger.error(f"Error processing onset category: {e}")
                    
            # Fetch excluded field and convert it to a boolean
            excluded_value = disease_data.get("loinc_99498_8")
            excluded = processor.fetch_mapping_value(
                "map_disease_verification_status", excluded_value, to_boolean=True
            )
            # Handle primary site
            primary_site_id = disease_data.get("snomed_363698007")
            primary_site = None
            if primary_site_id:
                primary_site_label = processor.fetch_label(primary_site_id)
                primary_site = OntologyClass(id=primary_site_id, label=primary_site_label)

            # Create the Disease block
            disease = Disease(
                term=term,
                onset=onset,
                excluded=excluded,
                primary_site=primary_site,
            )
            
            if hasattr(disease, "excluded") and disease.excluded is not None:
                disease.excluded = bool(disease.excluded)

            diseases.append(disease)

        return diseases

    except Exception as e:
        logger.error(f"Failed to map diseases: {e}")
        raise
