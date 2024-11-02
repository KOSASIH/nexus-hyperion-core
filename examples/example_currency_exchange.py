# examples/example_currency_exchange.py

from src.modules.currency_exchange import CurrencyExchange  # Adjust the import based on your actual module structure

def main():
    # Create an instance of the CurrencyExchange class
    currency_exchange = CurrencyExchange()

    # Example currency conversion
    amount = 100  # Amount in USD
    from_currency = 'USD'
    to_currency = 'EUR'

    # Convert currency
    converted_amount = currency_exchange.convert_currency(amount, from_currency, to_currency)
    print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")

    # Get exchange rate
    exchange_rate = currency_exchange.get_exchange_rate(from_currency, to_currency)
    print(f"Exchange Rate from {from_currency} to {to_currency}: {exchange_rate:.4f}")

if __name__ == "__main__":
    main()
