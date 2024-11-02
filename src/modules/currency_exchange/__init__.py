# src/modules/currency_exchange/__init__.py

import logging
from .exchange_rates import ExchangeRateProvider, CurrencyConverter
from .transaction import TransactionProcessor

# Configure logging for the currency exchange module
logger = logging.getLogger(__name__)

__version__ = "1.0.0"  # Versioning for the module
__all__ = ["ExchangeRateProvider", "CurrencyConverter", "TransactionProcessor", "create_currency_exchange_system"]

def create_currency_exchange_system(api_url="https://api.exchangerate-api.com/v4/latest"):
    """
    Factory method to create a complete currency exchange system.

    Args:
        api_url (str): The API URL for fetching exchange rates.

    Returns:
        dict: A dictionary containing instances of the main classes.
    """
    logger.info("Creating currency exchange system.")
    
    # Create instances of the main classes
    rate_provider = ExchangeRateProvider(api_url=api_url)
    converter = CurrencyConverter(rate_provider=rate_provider)
    transaction_processor = TransactionProcessor(converter=converter)

    # Fetch initial exchange rates
    try:
        rate_provider.fetch_rates()
    except Exception as e:
        logger.error(f"Failed to fetch initial exchange rates: {e}")

    return {
        "rate_provider": rate_provider,
        "converter": converter,
        "transaction_processor": transaction_processor
    }

def configure_logging(level=logging.INFO):
    """
    Configure logging for the currency exchange module.

    Args:
        level (int): The logging level (e.g., logging.DEBUG, logging.INFO).
    """
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=level
    )
    logger.info("Logging configured.")

def display_module_info():
    """Display information about the currency exchange module."""
    logger.info(f"Currency Exchange Module Version: {__version__}")
    logger.info("Available classes: " + ", ".join(__all__))
