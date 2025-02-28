import signal
import typer
from pathlib import Path
from rarelink.phenopackets import (
    create_phenopacket,
    write_phenopackets
)
import logging

app = typer.Typer()

DEFAULT_OUTPUT_DIR = Path.home() / "Downloads" / "phenopackets"
logger = logging.getLogger(__name__)

class TimeoutException(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutException("Pipeline processing exceeded the one-hour timeout limit.")

def phenopacket_pipeline(input_data: list, output_dir: str, created_by: str, timeout: int = 3600):
    """
    Pipeline to process input data, create Phenopackets, and write them to files.

    Args:
        input_data (list): List of dictionaries containing individual records.
        output_dir (str): Directory to save Phenopacket JSON files.
        created_by (str): Name of the creator (for metadata).
        timeout (int): Timeout in seconds (default is 3600 seconds = 1 hour).

    Returns:
        None
    """
    logger.info("Starting the Phenopacket pipeline...")

    # Set up the alarm signal for the timeout.
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(timeout)

    try:
        # Create Phenopackets
        phenopackets = []
        for record in input_data:
            try:
                phenopacket = create_phenopacket(record, created_by)
                phenopackets.append(phenopacket)
                print(f" ... created Phenopacket for record id={record['record_id']}")
            except Exception as e:
                print(f"ERROR creating Phenopacket for record id={record['record_id']} - {e}")

        # Write Phenopackets to files
        logger.info("Writing Phenopackets to files...")
        write_phenopackets(phenopackets, output_dir)
        logger.info("Phenopacket pipeline completed successfully.")
    except TimeoutException as te:
        logger.error(f"Timeout occurred: {te}")
        print(f"WARNING: Processing timed out after {timeout/3600} hour(s).")
        raise
    finally:
        # Disable the alarm
        signal.alarm(0)
