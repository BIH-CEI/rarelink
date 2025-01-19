import subprocess
from pathlib import Path
from typing import Tuple, List, Union
import logging

logger = logging.getLogger(__name__)

def validate_phenopackets(path: Path) -> Union[Tuple[bool, str], List[Tuple[bool, str]]]:
    """
    Validates a phenopacket file or directory of phenopackets using the `phenopacket-tools` CLI.

    Args:
        path (Path): Path to a phenopacket file or directory of phenopackets.

    Returns:
        Union[Tuple[bool, str], List[Tuple[bool, str]]]: Validation results.
            - Single file: (bool, str) - Success/Failure and details.
            - Directory: List of (bool, str) for each file.
    
    Raises:
        ValueError: If the path is invalid or contains no valid phenopackets.
    """
    logger.info("Starting validation of phenopackets...")

    if not path.exists():
        raise ValueError(f"Path {path} does not exist.")
    
    if path.is_file():
        if path.suffix == ".json":
            return _validate_single_phenopacket(path)
        else:
            raise ValueError(f"File {path} is not a valid JSON file.")
    elif path.is_dir():
        results = []
        for file_path in path.glob("*.json"):
            results.append(_validate_single_phenopacket(file_path))
        
        if not results:
            raise ValueError(f"Directory {path} does not contain any JSON files.")
        
        logger.info(f"Validation completed: {len(results)} files validated.")
        return results
    else:
        raise ValueError(f"Path {path} is neither a file nor a directory.")

def _validate_single_phenopacket(file_path: Path) -> Tuple[bool, str]:
    """
    Validates a single phenopacket using the `phenopacket-tools` CLI.

    Args:
        file_path (Path): Path to a single phenopacket file.

    Returns:
        Tuple[bool, str]: Validation result (Success/Failure) and details.
    """
    command = f"phenopacket-tools validate {file_path}"
    try:
        logger.info(f"Validating {file_path}...")
        output = subprocess.check_output(command, shell=True, text=True)
        logger.info(f"Validation output for {file_path}:\n{output}")
        return True, output
    except subprocess.CalledProcessError as e:
        logger.error(f"Validation failed for {file_path}:\n{e.output}")
        return False, e.output

if __name__ == "__main__":
    import argparse
    import sys

    logging.basicConfig(level=logging.INFO)

    parser = argparse.ArgumentParser(
        description="Validate a phenopacket file or directory of phenopackets."
    )
    parser.add_argument(
        "path", 
        type=Path, 
        help="Path to the phenopacket file or directory to validate."
    )
    args = parser.parse_args()

    try:
        results = validate_phenopackets(args.path)
        if isinstance(results, list):
            for success, details in results:
                if not success:
                    logger.error(details)
        elif not results[0]:
            logger.error(results[1])
    except ValueError as ve:
        logger.error(str(ve))
        sys.exit(1)
