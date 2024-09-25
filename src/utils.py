import json
import logging


logger = logging.getLogger('utils')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('logs/utils.log')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def read_transactions_from_json(file_path):
    try:
        logger.info(f'Записываем данные в файл {file_path}')
        with open(file_path, 'r') as file:
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
