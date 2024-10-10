from datetime import datetime

from src import widget
from src.processing import filter_by_state, sort_by_date, sort_by_string
from src.transaction import get_transaction_amount
from src.transactions2 import read_csv, read_excel, file_path_csv, file_path_excel
from src.utils import read_transactions_from_json, file_path


def main():
    print('''Привет! Добро пожаловать в программу работы 
с банковскими транзакциями. 
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла''')
    print()
    user_input_1 = input()
    print()
    transactions_from_file = []
    if user_input_1 == '1':
        print('Для обработки выбран JSON-файл.')
        file_format = 'JSON'
        transactions_from_file = read_transactions_from_json(file_path)
    elif user_input_1 == '2':
        print('Для обработки выбран CSV-файл.')
        file_format = 'CSV'
        transactions_from_file = read_csv(file_path_csv)
    elif user_input_1 == '3':
        print('Для обработки выбран XLSX-файл.')
        file_format = 'EXCEL'
        transactions_from_file = read_excel(file_path_excel)

    print()
    print('''Введите статус, по которому необходимо выполнить фильтрацию. 
    Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING''')
    print()
    while True:
        user_input_2 = input().upper()  # конвертируем ввод пользователя в верхний регистр
        state_for_filtering = ['EXECUTED', 'CANCELED', 'PENDING']
        if user_input_2 in state_for_filtering:
            filtered_list = filter_by_state(transactions_from_file, user_input_2)
            break
        else:
            print()
            print(f'Статус операции "{user_input_2}" недоступен. Пожалуйста, введите корректный статус.'
                  f' Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING')
            print()
    print()
    print(f'Операции отфильтрованы по статусу "{user_input_2}"')

    print()
    print('Отсортировать операции по дате? Да/Нет')
    print()
    user_input_3 = input().lower()  # конвертируем ввод пользователя в нижний регистр
    if user_input_3 == 'да' or user_input_3 == '':
        print()
        print('Отсортировать по возрастанию или по убыванию?')
        print()
        user_input_4 = input().lower()  # конвертируем ввод пользователя в нижний регистр
        if user_input_4 == 'по убыванию' or user_input_4 == '':
            filtered_list = sort_by_date(filtered_list)
        elif user_input_4 == 'по возрастанию':
            filtered_list = sort_by_date(filtered_list, sorting_param=True)
        print(filtered_list)
    print()
    print('Выводить только рублевые транзакции? Да/Нет')
    print()
    user_input_5 = input().lower()  # конвертируем ввод пользователя в нижний регистр
    if user_input_5 == 'да' or user_input_5 == '':
        filtered_list = get_transaction_amount(filtered_list, file_format)
    elif user_input_5 == 'нет':
        # если пользователь вводит "Нет", то список остается без изменений
        pass
    print(filtered_list)
    print()
    print('Отфильтровать список транзакций по определенному слову в описании? Да/Нет')
    print()
    user_input_6 = input().lower()  # конвертируем ввод пользователя в нижний регистр
    if user_input_6 == 'да':
        print()
        user_input_7 = input("Введите слово для сортировки: ")
        filtered_list = sort_by_string(filtered_list, user_input_7)
        print(filtered_list)
    print()
    print("Распечатываю итоговый список транзакций...")
    print()
    if not filtered_list:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print("Всего банковских операций в выборке:", len(filtered_list))
        for operation in filtered_list:
            date_string = operation['date']
            if 'Z' in date_string:  # проверяем, есть ли в строке даты 'Z' в конце
                date_format = '%Y-%m-%dT%H:%M:%SZ'
            else:
                date_format = '%Y-%m-%dT%H:%M:%S.%f'

            try:
                date_object = datetime.strptime(date_string, date_format)
                formatted_date = date_object.strftime('%d.%m.%Y')  # форматируем дату как дд.мм.гггг
                print(f"{formatted_date} {operation['description']}")

                if "Перевод" in operation['description']:
                    print(widget.mask_account_card(operation['from']), " -> ",
                          widget.mask_account_card(operation['to']))
                elif "Открытие" in operation['description']:
                    print(widget.mask_account_card(operation['to']))
                # print("Сумма:", external_api.convert_currency(operation, operation), "руб.")
                print()
            except ValueError as e:
                print(e)


if __name__ == "__main__":
    print(main())
