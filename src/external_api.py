import os

import requests


def convert_currency(amount, currency):
    """ Функция извлекает обменный курс из API."""

    api_key = os.getenv('API_ACCESS_KEY')  # Replace with your API key
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={"RUB"}&from={currency}&amount={amount}"
    headers = {"apikey": api_key}
    try:
        response = requests.get(url, headers=headers, timeout=5, allow_redirects=False)
        result = response.json()
        print(result)
        return float(result["result"])
    except requests.exceptions.ConnectionError:
        print("Произошла ошибка 'Connection Error'! Проверьте, пожалуйста, Ваше соединение!")
