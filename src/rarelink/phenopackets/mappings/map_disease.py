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

def map_disease(disease_data: dict, processor: DataProcessor, mapping_config: dict) -> Disease:
    """
    Maps a single instance of disease data to a Phenopacket Disease block.

    Args:
        disease_data (dict): Input dictionary for the disease.
        processor (DataProcessor): Processor for data retrieval and mapping.
        mapping_config (dict): Configuration for disease fields.

    Returns:
        Disease: A Phenopacket Disease block.
    """
    try:
        # Select the first non-empty term field
        term_id = processor.get_field(
            disease_data, mapping_config["term_fields"])
        if not term_id:
            raise ValueError("No valid disease term found.")

        # Fetch the label for the term
        term_label = processor.fetch_label(term_id)

        # Build the OntologyClass for the disease term
        term = OntologyClass(
            id=term_id,
            label=term_label,
        )

        # Handle onset preference (date over category)
        onset_date = processor.get_field(
            disease_data, mapping_config["onset_date_field"])
        onset_category = processor.get_field(
            disease_data, mapping_config["onset_category_field"])

        onset = None
        if onset_date:
            onset = TimeElement(
                timestamp=processor.process_time_element(onset_date))
        elif onset_category:
            onset_label = processor.fetch_label(onset_category)
            onset = OntologyClass(
                id=onset_category, label=onset_label)

        # Exclude field logic (e.g., disease exclusion)
        excluded_value = processor.get_field(
            disease_data, mapping_config["excluded_field"])
        excluded = processor.fetch_mapping_value(
            "map_excluded", excluded_value) or None

        # Handle primary site
        primary_site_id = processor.get_field(
            disease_data, mapping_config["primary_site_field"])
        primary_site = None
        if primary_site_id:
            primary_site_label = processor.fetch_label(primary_site_id)
            primary_site = OntologyClass(id=primary_site_id, 
                                         label=primary_site_label)

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
    """
    Maps all repeated instances of disease data to Phenopacket Disease blocks.

    Args:
        data (dict): Input data dictionary containing repeated elements.
        processor (DataProcessor): Processor for data retrieval and mapping.
        mapping_config (dict): Configuration for disease fields.

    Returns:
        list: A list of Phenopacket Disease blocks.
    """
    logger.debug("Starting to map diseases...")
    logger.debug(f"Input data: {data}")
    logger.debug(f"Mapping configuration: {mapping_config}")

    repeated_elements = processor.get_field(data, "repeated_elements")
    if not repeated_elements:
        logger.warning("No repeated elements found in the data.")
        return []

    disease_elements = [
        element["disease"] for element in repeated_elements
        if element.get("redcap_repeat_instrument") == "rarelink_5_disease" and "disease" in element
    ]
    logger.debug(f"Filtered disease elements: {disease_elements}")

    diseases = []
    for disease_data in disease_elements:
        try:
            disease = map_disease(disease_data, processor, mapping_config)
            diseases.append(disease)
        except Exception as e:
            logger.warning(f"Failed to map disease block: {e}")
    logger.debug(f"Mapped diseases: {diseases}")
    return diseases
