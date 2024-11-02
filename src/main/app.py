# src/main/app.py

import logging
import sys
from config import Config
from logger import setup_logger
from modules.risk_assessment.risk_evaluator import RiskEvaluator
from modules.currency_exchange.exchange_rates import CurrencyExchange
from modules.resource_optimization.optimizer import ResourceOptimizer

def initialize_modules(config):
    """Initialize application modules."""
    risk_evaluator = RiskEvaluator(config)
    currency_exchange = CurrencyExchange(config)
    resource_optimizer = ResourceOptimizer(config)
    return risk_evaluator, currency_exchange, resource_optimizer

def perform_risk_assessment(risk_evaluator, entity_id):
    """Perform risk assessment for a given entity."""
    try:
        logger.info(f"Starting risk assessment for entity {entity_id}...")
        risk_score = risk_evaluator.evaluate_risk(entity_id)
        logger.info(f"Risk score for entity {entity_id}: {risk_score}")
        return risk_score
    except Exception as e:
        logger.error(f"Error during risk assessment: {e}")
        return None

def perform_currency_exchange(currency_exchange, from_currency, to_currency, amount):
    """Perform currency exchange."""
    try:
        logger.info(f"Exchanging {amount} {from_currency} to {to_currency}...")
        exchange_result = currency_exchange.exchange(from_currency, to_currency, amount)
        logger.info(f"Exchange result: {exchange_result}")
        return exchange_result
    except Exception as e:
        logger.error(f"Error during currency exchange: {e}")
        return None

def optimize_resources(resource_optimizer, resource_data):
    """Optimize resource allocation."""
    try:
        logger.info("Optimizing resources...")
        optimized_resources = resource_optimizer.optimize(resource_data)
        logger.info(f"Optimized resource allocation: {optimized_resources}")
        return optimized_resources
    except Exception as e:
        logger.error(f"Error during resource optimization: {e}")
        return None

def main():
    # Setup logger
    setup_logger()
    global logger
    logger = logging.getLogger(__name__)

    # Load configuration
    config = Config()
    logger.info("Configuration loaded successfully.")

    # Validate configuration
    if not config.API_KEY or not config.DB_URI:
        logger.critical("API_KEY and DB_URI must be set in the configuration.")
        sys.exit(1)

    # Initialize modules
    risk_evaluator, currency_exchange, resource_optimizer = initialize_modules(config)

    # Example usage of modules
    entity_id = "12345"
    perform_risk_assessment(risk_evaluator, entity_id)

    from_currency = "USD"
    to_currency = "EUR"
    amount = 100
    perform_currency_exchange(currency_exchange, from_currency, to_currency, amount)

    resource_data = {"water": 1000, "energy": 5000}
    optimize_resources(resource_optimizer, resource_data)

if __name__ == "__main__":
    main()
