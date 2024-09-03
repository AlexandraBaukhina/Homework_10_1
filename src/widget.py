import re


def mask_account_card(card_type_and_number: str) -> str:
    ''' Функция принимает на вход номер карты или счета и возвращает строку с замаскированным номером'''

    # Поиск слов и чисел
    card_type = re.findall(r'[A-Za-zА-Яа-я]+', card_type_and_number)
    number = re.findall(r'\d+', card_type_and_number)

    if len(card_type_and_number) < 16:
        raise ValueError("Номер карты или счета должен содержать от 16 цифр")

    # Проверим по длине номера карта или счет
    for num in number:
        if len(num) == 16:
            card_number = num
            # Разделяем номер карты на блоки по 4 цифры
            blocks = [card_number[i: i + 4] for i in range(0, 16, 4)]

            # Формируем маску
            masked_blocks = [
                blocks[0],  # Первые 4 цифры
                blocks[1][:2] + "**",  # Следующие 2 цифры видны, остальное заменено на **
                "****",  # Третий блок полностью заменён на ****
                blocks[3],  # Последние 4 цифры
            ]

            # Объединяем блоки в строку с пробелами
            masked_number = " ".join(masked_blocks)

        elif len(num) > 16:
            account_number = num

            # Оставляем последние шесть символов номера счета
            acc_num = account_number[-6:]

            # Формируем маску
            masked_number = "**" + acc_num[-4:]
        else:
            raise ValueError("Номер карты или счета должен содержать от 16 цифр")

        joined_card_type = ' '.join(card_type)

        if len(card_type) != 0:
            return f'{joined_card_type} {masked_number}'

        return f'{masked_number}'


def get_date(full_date: str) -> str:
    ''' Функция принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ"'''
    if len(full_date) <= 10:
        raise ValueError('Введите дату в формате "ГГГГ-ММ-ДДT02:26:18.671407')
    else:
        date = full_date[:10]
        return f'{date[-2:]}.{date[5:7]}.{date[:4]}'
