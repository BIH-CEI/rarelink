import subprocess
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

def validate_linkml_data(schema_path: Path, processed_file: Path) -> bool:
    """
    Validate the processed data against the LinkML schema.

    Args:
        schema_path (Path): Path to the LinkML schema YAML file.
        processed_file (Path): Path to the processed JSON file.

    Returns:
        bool: True if validation is successful, False otherwise.
    """
    try:
        # Resolve to absolute paths
        resolved_schema_path = schema_path.resolve(strict=True)
        resolved_processed_file = processed_file.resolve(strict=True)
        logger.info(f"Resolved schema path: {resolved_schema_path}")
        logger.info(f"Resolved processed file path: {resolved_processed_file}")
        
        # Execute linkml-validate command
        result = subprocess.run(
            [
                "linkml-validate",
                "--schema",
                str(resolved_schema_path),
                str(resolved_processed_file),
            ],
            capture_output=True,
            text=True,
        )

        # Log stdout and stderr for debugging
        logger.debug(f"Validation stdout: {result.stdout}")
        logger.debug(f"Validation stderr: {result.stderr}")

        if result.returncode == 0:
            logger.info("Validation successful.")
            return True
        else:
            logger.error("Validation failed.")
            logger.error(f"Validation stderr: {result.stderr}")
            return False
    except FileNotFoundError as e:
        logger.error(f"File not found: {e}")
        raise RuntimeError(f"File not found: {e}") from e
    except Exception as e:
        logger.error(f"Unexpected error during validation: {e}")
        raise
