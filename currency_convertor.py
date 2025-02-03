import requests


class CurrencyConvertor:
    def __init__(self):
        self.api_url = "https://api.exchangerate-api.com/v4/latest/"

    def convert(self, amount, from_currency, to_currency):
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()

        # Fetch exchange rates from the API
        response = requests.get(f"{self.api_url}{from_currency}")

        if response.status_code != 200:
            raise Exception("Failed to fetch exchange rates.")

        rates = response.json()["rates"]

        if to_currency not in rates:
            raise ValueError(f"Conversion from {from_currency} to {to_currency} is not available.")

        # Perform the conversion
        return amount * rates[to_currency]
