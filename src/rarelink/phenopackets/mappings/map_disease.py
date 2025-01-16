import logging
from phenopackets import Disease, OntologyClass, TimeElement
from rarelink.utils.processor import DataProcessor

logger = logging.getLogger(__name__)

def map_onset(data: dict, processor: DataProcessor, category_field: str, date_field: str) -> TimeElement:
    """
    Maps onset information, preferring the date field over the category field.

    Args:
        data (dict): The input data dictionary.
        processor (DataProcessor): Handles field retrieval.
        category_field (str): Field path for the onset category.
        date_field (str): Field path for the onset date.

    Returns:
        TimeElement: A Phenopacket TimeElement block or None.
    """
    onset_date = processor.get_field(data, date_field)
    if onset_date:
        return TimeElement(
            timestamp=processor.process_time_element(onset_date)
        )
    
    onset_category = processor.get_field(data, category_field)
    if onset_category:
        return TimeElement(
            description=onset_category
        )
    return None

logger = logging.getLogger(__name__)

def map_disease(data: dict, processor: DataProcessor, mapping_config: dict) -> Disease:
    """
    Maps a single disease entry to a Phenopacket Disease block.

    Args:
        data (dict): Input dictionary containing the disease data.
        processor (DataProcessor): Processor for field mapping.
        mapping_config (dict): Configuration for disease fields.

    Returns:
        Disease: A Phenopacket Disease block.
    """
    try:
        # Term field logic
        term_id = processor.prefer_non_empty_field(data, mapping_config["term_fields"])
        if not term_id:
            raise ValueError("No valid disease term found.")
        term_label = processor.fetch_label(term_id)
        term = OntologyClass(id=term_id, label=term_label)

        # Onset logic (date prioritized over category)
        onset_date = data.get(mapping_config["onset_date_field"])
        onset_category = data.get(mapping_config["onset_category_field"])
        onset = None
        if onset_date:
            onset = TimeElement(timestamp=processor.process_time_element(onset_date))
        elif onset_category:
            onset_label = processor.fetch_label(onset_category)
            onset = OntologyClass(id=onset_category, label=onset_label)

        # Exclusion logic
        excluded_value = data.get(mapping_config["excluded_field"])
        excluded = processor.fetch_mapping_value(
            "map_excluded", excluded_value) or None
        
        # Primary site logic
        primary_site_id = data.get(mapping_config["primary_site_field"])
        primary_site = None
        if primary_site_id:
            primary_site_label = processor.fetch_label(primary_site_id)
            primary_site = OntologyClass(id=primary_site_id, label=primary_site_label)

        # Construct and return the Disease block
        return Disease(
            term=term,
            onset=onset,
            excluded=excluded,
            primary_site=primary_site,
        )
    except Exception as e:
        logger.error(f"Error mapping disease: {e}")
        raise



def map_diseases(data: dict, processor: DataProcessor, mapping_config: dict) -> list:
    logger.debug("Starting to map diseases...")
    repeated_elements = data.get("repeated_elements", [])
    diseases = []

    for element in repeated_elements:
        if element.get("redcap_repeat_instrument") == "rarelink_5_disease":
            disease_data = element.get("disease", {})
            try:
                # Fetch the term ID
                term_id = processor.prefer_non_empty_field(disease_data, mapping_config["term_fields"])
                if not term_id:
                    raise ValueError("No valid disease term found.")
                term_label = processor.fetch_label(term_id)

                # Fetch the onset
                onset = map_onset(
                    disease_data,
                    processor,
                    mapping_config["onset_category_field"],
                    mapping_config["onset_date_field"]
                )

                # Handle exclusion and primary site
                excluded = processor.get_field(disease_data, mapping_config["excluded_field"]) == "hl7fhir_excluded"
                primary_site_id = processor.get_field(disease_data, mapping_config["primary_site_field"])
                primary_site = OntologyClass(
                    id=primary_site_id,
                    label=processor.fetch_label(primary_site_id)
                ) if primary_site_id else None

                # Construct the Disease block
                diseases.append(Disease(
                    term=OntologyClass(id=term_id, label=term_label),
                    onset=onset,
                    excluded=excluded,
                    primary_site=primary_site,
                ))
            except Exception as e:
                logger.warning(f"Failed to map disease: {e}")

    return diseases
