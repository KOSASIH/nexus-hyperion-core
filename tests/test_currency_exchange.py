# tests/test_currency_exchange.py

import unittest
from src.modules.currency_exchange import CurrencyExchange  # Adjust the import based on your actual module structure

class TestCurrencyExchange(unittest.TestCase):

    def setUp(self):
        self.currency_exchange = CurrencyExchange()

    def test_convert_currency(self):
        # Example test case for currency conversion
        converted_amount = self.currency_exchange.convert_currency(100, 'USD', 'EUR')
        self.assertAlmostEqual(converted_amount, 85.0, places=2)  # Adjust expected value based on actual conversion rate

    def test_get_exchange_rate(self):
        # Example test case for getting exchange rate
        rate = self.currency_exchange.get_exchange_rate('USD', 'EUR')
        self.assertGreater(rate, 0)

if __name__ == '__main__':
    unittest.main()
