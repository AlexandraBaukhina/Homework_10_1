import pandas as pd

transactions_csv = pd.read_csv('C:/Users/79200/PycharmProjects/transactions.csv')
print(transactions_csv)

transactions_excel = pd.read_excel('C:/Users/79200/PycharmProjects/transactions.xlsx')
print(transactions_excel)
