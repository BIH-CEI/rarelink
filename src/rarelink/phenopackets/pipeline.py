# src/rarelink/phenopackets/pipeline.py
import typer
from pathlib import Path
from typing import Dict, Any, Optional
import logging
import signal
import json
import os

from rarelink.phenopackets import (
    create_phenopacket
)

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
    timeout: int = 3600,
    debug: bool = False
):
    """
    Enhanced pipeline to process input data, create Phenopackets, and write them to files.
    Now handles different data models through flexible mapping configurations.

    Args:
        input_data (list): List of dictionaries containing individual records.
        output_dir (str): Directory to save Phenopacket JSON files.
        created_by (str): Name of the creator (for metadata).
        mapping_configs (dict, optional): Mapping configurations for Phenopacket creation.
        timeout (int): Timeout in seconds (default is 3600 seconds = 1 hour).
        debug (bool): Enable debug mode for verbose logging

    Returns:
        List: A list of created Phenopacket objects.
    """
    # Set up logging level based on debug flag
    if debug:
        logging.getLogger('rarelink').setLevel(logging.DEBUG)
    else:
        logging.getLogger('rarelink').setLevel(logging.INFO)

    # Set up the alarm signal for the timeout
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(timeout)

    try:
        # Validate mapping_configs
        if not mapping_configs:
            raise ValueError("Mapping configurations are required")
            
        # Create directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

        # Create Phenopackets
        phenopackets = []
        failed_records = []
        total_records = len(input_data)

        for i, record in enumerate(input_data):
            try:
                print(f"Processing record {i+1}/{total_records} (id={record.get('record_id', 'unknown')})")
                
                # Use mapping_configs if provided
                phenopacket = create_phenopacket(
                    data=record, 
                    created_by=created_by,
                    mapping_configs=mapping_configs,
                    debug=debug
                )
                
                phenopackets.append(phenopacket)
                print(f" ... created Phenopacket for record id={record.get('record_id', 'unknown')}")
            except Exception as e:
                print(f"ERROR creating Phenopacket for record id={record.get('record_id', 'unknown')} - {e}")
                failed_records.append({
                    'record_id': record.get('record_id', 'unknown'),
                    'error': str(e)
                })
                
                # Log additional debug info
                if debug:
                    logger.debug(f"Record structure: {json.dumps(record, default=str, indent=2)[:1000]}...")

        # Write Phenopackets to files
        from rarelink.phenopackets import write_phenopackets
        logger.info("Writing Phenopackets to files...")
        write_phenopackets(phenopackets, output_dir)
        logger.info("Phenopacket pipeline completed successfully.")

        # Optionally, log details of failed records
        if failed_records:
            logger.warning("Details of failed records:")
            for fail in failed_records:
                logger.warning(f"Record ID: {fail['record_id']}")
                logger.warning(f"Error: {fail['error']}")

            # Write failure report to file for easier debugging
            failure_file = os.path.join(output_dir, "failures.json")
            with open(failure_file, 'w') as f:
                json.dump(failed_records, f, indent=2)
            logger.info(f"Failure report written to {failure_file}")

        return phenopackets
    
    except TimeoutException as te:
        logger.error(f"Timeout occurred: {te}")
        print(f"WARNING: Processing timed out after {timeout/3600} hour(s).")
        raise
    finally:
        # Disable the alarm
        signal.alarm(0)