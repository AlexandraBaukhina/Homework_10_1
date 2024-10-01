import pandas as pd
import csv
import openpyxl


file_path_csv = 'C:/Users/79200/PycharmProjects/transactions.csv'
file_path_excel = 'C:/Users/79200/PycharmProjects/transactions.xlsx'

def read_csv(file_path_csv):
    transactions_csv = pd.read_csv(file_path_csv)
    data_csv = []
    for row in transactions_csv:
        data_csv.append(dict(row))
    return data_csv


def read_excel(file_path_excel):
    wb = openpyxl.load_workbook(file_path_excel)
    sheet = wb.active
    data_excel = []
    headers = [cell.value for cell in sheet[1]]
    for row in sheet.iter_rows(min_row=2, values_only=True):
        data_excel.append(dict(zip(headers, row)))
    return data_excel
