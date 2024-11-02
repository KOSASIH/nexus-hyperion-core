# src/main/logger.py

import logging
import os

def setup_logger(log_level="INFO", log_file=None):
    """Set up the logger with specified log level and optional log file."""
    logger = logging.getLogger("NexusHyperion")
    logger.setLevel(log_level)

    # Create a console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)

    # Create a formatter and set it for the console handler
    console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(console_formatter)

    # Add the console handler to the logger
    logger.addHandler(console_handler)

    # If a log file is specified, set up a file handler
    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(log_level)
        file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)

    logger.info("Logger is set up successfully.")
    return logger

def set_log_level(logger, level):
    """Set the logging level for the logger."""
    level = level.upper()
    if level in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
        logger.setLevel(level)
        for handler in logger.handlers:
            handler.setLevel(level)
        logger.info(f"Log level set to {level}.")
    else:
        logger.warning(f"Invalid log level: {level}. Keeping the current level: {logger.level}.")

def log_exception(logger, exception):
    """Log an exception with traceback."""
    logger.error("An exception occurred", exc_info=exception)

# Example usage
if __name__ == "__main__":
    # Setup logger for testing
    logger = setup_logger(log_level=os.getenv("LOG_LEVEL", "INFO"), log_file="nexus_hyperion.log")
    logger.info("This is an info message.")
    logger.debug("This is a debug message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
