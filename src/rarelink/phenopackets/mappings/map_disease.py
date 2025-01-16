import logging
from phenopackets import Disease, OntologyClass, TimeElement
from rarelink.utils.processor import DataProcessor
from rarelink_cdm.v2_0_0_dev0.mappings.phenopackets import DISEASE_BLOCK

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

def map_disease(element: dict, processor: DataProcessor) -> Disease:
    """
    Maps a single disease element to a Phenopacket Disease block.

    Args:
        element (dict): A single disease element from the input data.
        processor (DataProcessor): Handles data processing and mapping.

    Returns:
        Disease: A Phenopacket Disease block.
    """
    try:
        # Prefer the first non-empty term field
        term_id = processor.prefer_non_empty_field(
            element, processor, DISEASE_BLOCK["term_fields"])
        term_label = processor.fetch_label(term_id)

        term = OntologyClass(
            id=term_id,
            label=term_label or "Unknown"
        )

        # Map onset (prefer date over category)
        onset = map_onset(
            element,
            processor,
            category_field=DISEASE_BLOCK["onset_category_field"],
            date_field=DISEASE_BLOCK["onset_date_field"]
        )

        # Map primary site (if available)
        primary_site_field = processor.get_field
        (element, DISEASE_BLOCK["primary_site_field"])
        primary_site = OntologyClass(
            id=primary_site_field,
            label=processor.fetch_label(primary_site_field)
        ) if primary_site_field else None

        # Map exclusion status
        excluded_field = processor.get_field(
            element, DISEASE_BLOCK["excluded_field"])
        excluded = True if excluded_field and excluded_field.lower() \
            == "hl7fhir_excluded" else False

        return Disease(
            term=term,
            onset=onset,
            excluded=excluded,
            primary_site=primary_site
        )
    except Exception as e:
        logger.error(f"Failed to map disease: {e}")
        raise
