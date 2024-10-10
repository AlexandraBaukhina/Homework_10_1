def get_transaction_amount(transaction, file_format):
    """
    Конвертирует сумму транзакции в рубли на основе кода валюты
    и формата файла (JSON, CSV, Excel)

    Аргументы:
        transaction (dict or row): Данные транзакции
        file_format (str): Формат файла (JSON, CSV, Excel)
        amount_field (str): Имя поля для суммы в файле
        currency_field (str): Имя поля для валюты в файле
        api_url (str): URL API для извлечения курсов обмена

    Возвращает:
        str: Сумма в рублях
    """

    result_list = []
    for i in transaction:
        if file_format == 'JSON':
            amount = i["operationAmount"]["amount"]
            currency = i["operationAmount"]["currency"]["code"]
        elif file_format == 'CSV':
            amount = i['amount']
            currency = i['currency_code']
        elif file_format == 'EXCEL':
            amount = i['amount']
            currency = i['currency_code']
        else:
            raise ValueError("Неподдерживаемый формат файла")
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={"RUB"}&from={currency}&amount={amount}"

        if currency == "RUB":
            result_list.append(i)
    return result_list
#  result_list = []
#
#   for i in transaction:
#       amount = i["operationAmount"]["amount"]
#       currency = i["operationAmount"]["currency"]["code"]
#       if currency == "RUB":
#         result_list.append(i)
#      else:
#          converted_amount = convert_currency(amount, currency)
#          i['amount'] = converted_amount
#          i['currency'] = 'RUB'
#          result_list.append(i)
#  return result_list
