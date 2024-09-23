import os
import requests

def get_exchange_rate(base_currency, target_currency):
    api_access_key = os.getenv("API_ACCESS_KEY")
    url = f"https://api.apilayer.com/exchangerates_data/{base_currency}?targets={target_currency}&apikey={api_access_key}"
    response = requests.get(url)
    data = response.json()
    rate = data["rates"][target_currency]
    return rate

def convert_currency(amount, base_currency, target_currency):
    rate = get_exchange_rate(base_currency, target_currency)
    converted_amount = amount * rate
    return converted_amount
