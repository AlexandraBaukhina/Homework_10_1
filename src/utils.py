import json
import logging

logger = logging.getLogger('utils')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('logs/utils.log')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

file_path = 'C:/Users/79200/PycharmProjects/Домашка1/data/operations.json'


def read_transactions_from_json(file_path):
    try:
        logger.info(f'Записываем данные в файл {file_path}')
        with open(file_path, 'r', encoding="utf8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                return []
    except FileNotFoundError as e:
        logger.error(f'Произошла ошибка: {e}')
        return []
    except json.JSONDecodeError as e:
        logger.error(f'Произошла ошибка: {e}')
        return []
