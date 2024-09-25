from external_api import convert_currency


def get_transaction_amount(transaction):
    amount = transaction["operationAmount"]["amount"]
    currency = transaction["operationAmount"]["currency"]["code"]

    if currency == "RUB":
        return float(amount)
    else:
        converted_amount = convert_currency(amount, currency, "RUB")
        return converted_amount
