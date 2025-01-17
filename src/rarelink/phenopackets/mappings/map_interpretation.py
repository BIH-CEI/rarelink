import logging
from rarelink.utils.processor import DataProcessor
from phenopackets import Interpretation

logger = logging.getLogger(__name__)

def map_interpretations(data: dict, 
                        processor: DataProcessor,
                        subject_id: str) -> dict:
    """
    Maps interpretation details.

    Args:
        data (dict): Input data for interpretation.
        processor (DataProcessor): Handles field processing.

    Returns:
        dict: Mapped interpretation structure.
    """
    instrument_name = processor.mapping_config.get("redcap_repeat_instrument")
    
    try:
        repeated_elements = data.get("repeated_elements", [])
        if not repeated_elements:
            logger.warning("No repeated elements found in the data.")
            return []

        # Filter relevant interpretation elements
        interpretation_elements = [
            element for element in repeated_elements
            if element.get("redcap_repeat_instrument") == instrument_name
        ]
        
        interpretations = []
        
        for interpretation_element in interpretation_elements:
            interpretation_data = interpretation_element.get("genetic_findings")
            if not interpretation_data:
                logger.warning("No interpretation data found in "
                               "this element. Skipping.")
                continue

            # id
            interpretation_id = subject_id
            
            # progress_status
            progress_status_field = interpretation_data.get(
                processor.mapping_config["progress_status_field"])
            progress_status = processor.fetch_mapping_value(
                "map_progress_status", progress_status_field) if \
                    progress_status_field else "UNKNOWN_PROGRESS"
            
            interpretation = Interpretation(
                id=interpretation_id,
                progress_status=progress_status
            )

            interpretations.append(interpretation)
        
        return interpretations
        
    except Exception as e:
        logger.error(f"Error mapping interpretation: {e}")
        raise
