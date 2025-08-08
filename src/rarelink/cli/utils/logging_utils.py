import logging
from pathlib import Path

def setup_logger(
    name: str,
    log_file: Path = None,
    level: int = logging.INFO,
    console: bool = True,
) -> logging.Logger:
    """
    Setup a logger with the specified name, log file, and log level.
    
    Parameters:
        name (str): The name of the logger.
        log_file (Path): File to log messages to. If None, logs only to console.
        level (int): Logging level (e.g., logging.INFO, logging.DEBUG).
        console (bool): Whether to log messages to the console.

    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate logs if logger already has handlers
    if logger.hasHandlers():
        return logger

    # Formatter for log messages
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # Console handler
    if console:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    # File handler
    if log_file:
        log_file.parent.mkdir(parents=True, exist_ok=True) 
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger


def log_info(logger: logging.Logger, message: str):
    """
    Log an info-level message.
    """
    logger.info(message)


def log_warning(logger: logging.Logger, message: str):
    """
    Log a warning-level message.
    """
    logger.warning(message)


def log_error(logger: logging.Logger, message: str):
    """
    Log an error-level message.
    """
    logger.error(message)


def log_exception(logger: logging.Logger, exception: Exception):
    """
    Log an exception with traceback.
    """
    logger.exception(f"An exception occurred: {exception}")
