import logging
from functools import wraps


def log(filename=None):
    """Декоратор для логирования начала, конца выполнения функции,
    её результата и возникших ошибок."""

    # Настройка логирования
    if filename:
        logging.basicConfig(filename=filename, level=logging.INFO,
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    else:
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    logger = logging.getLogger(__name__)

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Логируем начало выполнения функции
            logger.info(f"Начало выполнения функции '{func.__name__}' с аргументами: {args}, {kwargs}")

            try:
                # Выполнение функции
                result = func(*args, **kwargs)

                # Логируем успешное завершение функции
                logger.info(f"Функция '{func.__name__}' завершена успешно. Результат: {result}")

                return result
            except Exception as e:
                # Логируем ошибку
                logger.error(f"Ошибка в функции '{func.__name__}': {e}. Аргументы: {args}, {kwargs}", exc_info=True)
                raise  # Перебрасываем исключение дальше

        return wrapper

    return decorator
