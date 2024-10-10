import openpyxl
import pandas as pd

file_path_csv = 'C:/Users/79200/PycharmProjects/Домашка1/data/transactions.csv'
file_path_excel = 'C:/Users/79200/PycharmProjects/Домашка1/data/transactions_excel.xlsx'


def read_csv(file_path_csv):
    with open(file_path_csv, encoding='utf-8') as f:
        transactions_csv = pd.read_csv(f, delimiter=';')
        fieldnames = ['id', 'state', 'date', 'amount', 'currency_name', 'currency_code', 'from', 'to', 'description']
        # next(transactions_csv)
        # writer = csv.DictWriter(file_path_csv, fieldnames=fieldnames)
        data_csv = transactions_csv.to_dict(orient="records")
        print(transactions_csv)
        # data_csv = {}
        # for row in transactions_csv:
        #    data_csv[row] = ''

        #   print(row)
        # for column, value in row.items():  # consider .iteritems() for Python 2
        #   data_csv.setdefault(column, []).append(value)
        print(data_csv)

        # data_csv.append(dict(row))
        return data_csv


def read_excel(file_path_excel):
    wb = openpyxl.load_workbook(file_path_excel)
    sheet = wb.active
    data_excel = []
    headers = [cell.value for cell in sheet[1]]
    for row in sheet.iter_rows(min_row=2, values_only=True):
        data_excel.append(dict(zip(headers, row)))
    return data_excel
