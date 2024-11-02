# src/modules/currency_exchange/transaction.py

import logging
from .exchange_rates import CurrencyConverter

# Configure logging for the transaction module
logger = logging.getLogger(__name__)

class TransactionProcessor:
    """Class to process currency exchange transactions."""
    
    def __init__(self, converter: CurrencyConverter):
        """Initialize with a CurrencyConverter instance."""
        self.converter = converter
        logger.info("TransactionProcessor initialized.")

    def process_transaction(self, amount, from_currency, to_currency):
        """
        Process a single currency exchange transaction.

        Args:
            amount (float): The amount to convert.
            from_currency (str): The currency to convert from.
            to_currency (str): The currency to convert to.

        Returns:
            dict: A dictionary containing transaction details or error information.
        """
        logger.info("Processing transaction: %s %s to %s.", amount, from_currency, to_currency)
        try:
            converted_amount = self.converter.convert(amount, from_currency, to_currency)
            transaction_details = {
                "original_amount": amount,
                "from_currency": from_currency,
                "to_currency": to_currency,
                "converted_amount": converted_amount,
                "status": "success"
            }
            logger.info("Transaction successful: %s", transaction_details)
            return transaction_details
        except Exception as e:
            logger.error("Transaction failed: %s", e)
            return {"error": str(e), "status": "failed"}

    def process_batch_transactions(self, transactions):
        """
        Process a batch of currency exchange transactions.

        Args:
            transactions (list): A list of transaction dictionaries, each containing
                                 'amount', 'from_currency', and 'to_currency'.

        Returns:
            list: A list of dictionaries containing transaction results.
        """
        logger.info("Processing batch transactions.")
        results = []
        for transaction in transactions:
            result = self.process_transaction(
                transaction['amount'],
                transaction['from_currency'],
                transaction['to_currency']
            )
            results.append(result)
        logger.info("Batch processing complete. Results: %s", results)
        return results

    def log_transaction(self, transaction_details):
        """
        Log transaction details to a file or database.

        Args:
            transaction_details (dict): The details of the transaction to log.
        """
        # Here you can implement logging to a file or database
        logger.info("Logging transaction: %s", transaction_details)
        # For demonstration, we will just log to console
        print(f"Transaction logged: {transaction_details}")

    def process_and_log_transaction(self, amount, from_currency, to_currency):
        """
        Process a transaction and log the details.

        Args:
            amount (float): The amount to convert.
            from_currency (str): The currency to convert from.
            to_currency (str): The currency to convert to.

        Returns:
            dict: A dictionary containing transaction details or error information.
        """
        transaction_details = self.process_transaction(amount, from_currency, to_currency)
        self.log_transaction(transaction_details)
        return transaction_details
