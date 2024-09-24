import os
import requests


def get_exchange_rate(base_currency, target_currency):
    """ Функция извлекает обменный курс из API."""
    api_access_key = os.getenv("API_ACCESS_KEY")
    if not api_access_key:
        raise ValueError("API_ACCESS_KEY environment variable is not set")

    url = f"https://api.apilayer.com/exchangerates_data/{base_currency}?targets={target_currency}&apikey={api_access_key}"
    response = requests.get(url)
    response.raise_for_status()  # Вызываем исключение для кодов типа 4xx или 5xx
    data = response.json()
    if "rates" not in data or target_currency not in data["rates"]:
        raise ValueError(f"Failed to retrieve exchange rate for {base_currency} to {target_currency}")
    rate = data["rates"][target_currency]
    return rate


def convert_currency(amount, base_currency, target_currency):
    """ Функция конвертирует сумму из одной валюты в другую."""
    rate = get_exchange_rate(base_currency, target_currency)
    converted_amount = amount * rate
    return converted_amount