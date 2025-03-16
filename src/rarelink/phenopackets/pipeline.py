import typer
from pathlib import Path
from typing import Dict, Any, Optional

from rarelink.phenopackets import (
    create_phenopacket
)
import logging

app = typer.Typer()

DEFAULT_OUTPUT_DIR = Path.home() / "Downloads" / "phenopackets"
logger = logging.getLogger(__name__)

class TimeoutException(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutException("Pipeline processing exceeded the one-hour timeout limit.")

def phenopacket_pipeline(
    input_data: list, 
    output_dir: str, 
    created_by: str, 
    mapping_configs: Optional[Dict[str, Any]] = None,
    timeout: int = 3600
):
    """
    Pipeline to process input data, create Phenopackets, and write them to files.

    Args:
        input_data (list): List of dictionaries containing individual records.
        output_dir (str): Directory to save Phenopacket JSON files.
        created_by (str): Name of the creator (for metadata).
        mapping_configs (dict, optional): Mapping configurations for Phenopacket creation.
        timeout (int): Timeout in seconds (default is 3600 seconds = 1 hour).

    Returns:
        List: A list of created Phenopacket objects.
    """
    import signal
    import logging

    logger = logging.getLogger(__name__)

    class TimeoutException(Exception):
        pass

    def timeout_handler(signum, frame):
        raise TimeoutException("Pipeline processing exceeded the one-hour timeout limit.")

    # Set up the alarm signal for the timeout
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(timeout)

    try:
        # Create Phenopackets
        phenopackets = []
        failed_records = []

        for record in input_data:
            try:
                # Use mapping_configs if provided
                phenopacket = create_phenopacket(
                    data=record, 
                    created_by=created_by,
                    mapping_configs=mapping_configs
                )
                phenopackets.append(phenopacket)
                print(f" ... created Phenopacket for record id={record.get('record_id', 'unknown')}")
            except Exception as e:
                print(f"ERROR creating Phenopacket for record id={record.get('record_id', 'unknown')} - {e}")
                failed_records.append({
                    'record': record,
                    'error': str(e)
                })

        # Write Phenopackets to files
        from rarelink.phenopackets import write_phenopackets
        logger.info("Writing Phenopackets to files...")
        write_phenopackets(phenopackets, output_dir)
        logger.info("Phenopacket pipeline completed successfully.")

        # Log summary of processing
        logger.info(f"Total records processed: {len(input_data)}")
        logger.info(f"Successful Phenopackets: {len(phenopackets)}")
        logger.info(f"Failed records: {len(failed_records)}")

        # Optionally, log details of failed records
        if failed_records:
            logger.warning("Details of failed records:")
            for fail in failed_records:
                logger.warning(f"Record ID: {fail['record'].get('record_id', 'unknown')}")
                logger.warning(f"Error: {fail['error']}")

        return phenopackets

    except TimeoutException as te:
        logger.error(f"Timeout occurred: {te}")
        print(f"WARNING: Processing timed out after {timeout/3600} hour(s).")
        raise
    finally:
        # Disable the alarm
        signal.alarm(0)