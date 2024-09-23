from external_api import convert_currency


def get_transaction_amount(transaction):
    amount = transaction["amount"]
    currency = transaction["currency"]

    if currency == "RUB":
        return amount
    else:
        converted_amount = convert_currency(amount, currency, "RUB")
        return converted_amount
