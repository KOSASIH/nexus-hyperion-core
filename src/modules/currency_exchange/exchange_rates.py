# src/modules/currency_exchange/exchange_rates.py

import requests
import logging
import time
from cachetools import TTLCache, cached

# Configure logging for the exchange rates module
logger = logging.getLogger(__name__)

class ExchangeRateProvider:
    """Class to fetch and manage exchange rates from various sources."""
    
    def __init__(self, api_url="https://api.exchangerate-api.com/v4/latest", cache_ttl=3600):
        """
        Initialize with the API URL and cache settings.

        Args:
            api_url (str): The API URL for fetching exchange rates.
            cache_ttl (int): Time-to-live for cached rates in seconds.
        """
        self.api_url = api_url
        self.rates = {}
        self.cache = TTLCache(maxsize=100, ttl=cache_ttl)  # Cache for exchange rates
        logger.info("ExchangeRateProvider initialized with API URL: %s", api_url)

    @cached(cache=lambda self: self.cache)
    def fetch_rates(self, base_currency="USD"):
        """Fetch exchange rates from the API and cache them."""
        logger.info("Fetching exchange rates for base currency: %s", base_currency)
        try:
            response = requests.get(f"{self.api_url}/{base_currency}")
            response.raise_for_status()
            data = response.json()
            self.rates = data['rates']
            logger.info("Exchange rates fetched successfully.")
        except requests.RequestException as e:
            logger.error("Error fetching exchange rates: %s", e)
            raise

    def get_rate(self, from_currency, to_currency):
        """Get the exchange rate from one currency to another."""
        if not self.rates:
            logger.warning("Exchange rates not fetched. Fetching now...")
            self.fetch_rates()
        
        rate = self.rates.get(to_currency)
        if rate is None:
            logger.error("Exchange rate not found for %s to %s.", from_currency, to_currency)
            raise ValueError(f"Exchange rate not found for {from_currency} to {to_currency}.")
        
        logger.info("Exchange rate from %s to %s: %s", from_currency, to_currency, rate)
        return rate

class CurrencyConverter:
    """Class to convert amounts between currencies."""
    
    def __init__(self, rate_provider: ExchangeRateProvider):
        """Initialize with an ExchangeRateProvider instance."""
        self.rate_provider = rate_provider
        logger.info("CurrencyConverter initialized.")

    def convert(self, amount, from_currency, to_currency):
        """Convert an amount from one currency to another."""
        logger.info("Converting %s %s to %s.", amount, from_currency, to_currency)
        rate = self.rate_provider.get_rate(from_currency, to_currency)
        converted_amount = amount * rate
        logger.info("Converted amount: %s %s", converted_amount, to_currency)
        return converted_amount
