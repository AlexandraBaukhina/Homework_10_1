import logging

logger = logging.getLogger('masks')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('logs/masks.log')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    ''' Функция принимает на вход номер карты и возвращает ее маску'''
    # Проверим, что длина номера карты правильная
    logger.info('Проверка длины номера карты')
    if len(card_number) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр")

    # Разделяем номер карты на блоки по 4 цифры
    blocks = [card_number[i: i + 4] for i in range(0, 16, 4)]

    # Формируем маску
    logger.info('Формирование маски номера карты')
    masked_blocks = [
        blocks[0],  # Первые 4 цифры
        blocks[1][:2] + "**",  # Следующие 2 цифры видны, остальное заменено на **
        "****",  # Третий блок полностью заменён на ****
        blocks[3],  # Последние 4 цифры
    ]

    # Объединяем блоки в строку с пробелами
    masked_number = " ".join(masked_blocks)

    logger.info('Возвращаем замаскированный номер карты')
    return masked_number


def get_mask_account(account_number: str) -> str:
    ''' Функция принимает на вход номер счета и возвращает его маску'''
    # Проверим, что длина номера счета правильная
    logger.info('Проверка длины номера счета')
    if len(account_number) != 18:
        raise ValueError("Номер счета должен содержать 18 цифр")

    # Оставляем последние шесть символов номера счета
    acc_num = account_number[-6:]

    # Формируем маску
    logger.info('Формирование маски номера счета')
    masked_number = "**" + acc_num[-4:]

    logger.info('Возвращаем замаскированный номер счета')
    return masked_number
