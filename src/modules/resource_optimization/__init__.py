# src/modules/resource_optimization/__init__.py

import logging
import os
import json
from pathlib import Path

# Configure logging for the resource optimization module
logger = logging.getLogger(__name__)

# Load configuration from a JSON file or environment variables
def load_config():
    """Load configuration settings from a JSON file or environment variables."""
    config_path = Path(os.getenv("RESOURCE_OPTIMIZATION_CONFIG", "config.json"))
    if config_path.is_file():
        with open(config_path) as config_file:
            config = json.load(config_file)
            logger.info("Configuration loaded from %s", config_path)
            return config
    else:
        logger.warning("Configuration file not found. Using default settings.")
        return {}

# Global configuration variable
config = load_config()

__version__ = "1.0.0"
__all__ = ["Optimizer", "ConsumptionAnalyzer", "create_resource_optimization_system", "configure_logging"]

def create_resource_optimization_system():
    """
    Factory method to create a resource optimization system.

    Returns:
        dict: A dictionary containing instances of the main classes.
    """
    logger.info("Creating resource optimization system.")
    from .optimizer import Optimizer
    from .consumption_analysis import ConsumptionAnalyzer

    optimizer = Optimizer(config.get("optimizer_settings", {}))
    analyzer = ConsumptionAnalyzer(config.get("analysis_settings", {}))
    return {
        "optimizer": optimizer,
        "analyzer": analyzer
    }

def configure_logging(level=logging.INFO):
    """
    Configure logging for the resource optimization module.

    Args:
        level (int): The logging level (e.g., logging.DEBUG, logging.INFO).
    """
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=level
    )
    logger.info("Logging configured at level: %s", logging.getLevelName(level))

def display_module_info():
    """Display information about the resource optimization module."""
    logger.info(f"Resource Optimization Module Version: {__version__}")
    logger.info("Available classes: " + ", ".join(__all__))

def validate_config(config):
    """
    Validate the loaded configuration.

    Args:
        config (dict): The configuration dictionary.

    Raises:
        ValueError: If the configuration is invalid.
    """
    required_keys = ["optimizer_settings", "analysis_settings"]
    for key in required_keys:
        if key not in config:
            raise ValueError(f"Missing required configuration key: {key}")
    logger.info("Configuration validated successfully.")

# Validate the loaded configuration
try:
    validate_config(config)
except ValueError as e:
    logger.error("Configuration validation failed: %s", e)
    raise

# Initialize the module
logger.info("Resource Optimization Module initialized.")
