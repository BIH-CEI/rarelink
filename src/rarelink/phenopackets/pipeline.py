import typer
from pathlib import Path
from rarelink.phenopackets import (
    create_phenopacket,
    write_phenopackets
)
# from rarelink.phenopackets.validate import validate_phenopackets
import logging

app = typer.Typer()

DEFAULT_OUTPUT_DIR = Path.home() / "Downloads" / "phenopackets"

logger = logging.getLogger(__name__)

def phenopacket_pipeline(input_data: list, output_dir: str, created_by: str):
    """
    Pipeline to process input data, create Phenopackets, and write them to files.

    Args:
        input_data (list): List of dictionaries containing individual records.
        output_dir (str): Directory to save Phenopacket JSON files.
        created_by (str): Name of the creator (for metadata).

    Returns:
        None
    """
    logger.info("Starting the Phenopacket pipeline...")
    
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