import pytest
from decorators import log

# Функции для тестирования
@log()
def successful_function(a, b):
    return a + b


@log()
def function_with_error(a, b):
    return a / b  # Здесь может произойти деление на ноль


# Тест успешного выполнения функции и вывода в консоль
def test_successful_function(capsys):
    successful_function(2, 3)

    captured = capsys.readouterr()
    assert "Начало выполнения функции 'successful_function'" in captured.out
    assert "Функция 'successful_function' завершена успешно. Результат: 5" in captured.out


# Тест обработки исключений и вывода в консоль
def test_function_with_error(capsys):
    with pytest.raises(ZeroDivisionError):
        function_with_error(1, 0)

    captured = capsys.readouterr()
    assert "Ошибка в функции 'function_with_error': division by zero. Аргументы: (1, 0)" in captured.err


# Тест успешного выполнения функции и записи в файл
def test_successful_function_file_log(tmpdir):
    log_file = tmpdir.join("mylog.txt")
    log_decorator = log(filename=str(log_file))

    @log_decorator
    def another_successful_function(a, b):
        return a * b

    another_successful_function(4, 5)

    with open(log_file, 'r') as f:
        log_contents = f.read()

    assert "Начало выполнения функции 'another_successful_function'" in log_contents
    assert "Функция 'another_successful_function' завершена успешно. Результат: 20" in log_contents


# Тест обработки исключений и записи в файл
def test_function_with_error_file_log(tmpdir):
    log_file = tmpdir.join("error_mylog.txt")
    log_decorator = log(filename=str(log_file))

    @log_decorator
    def function_with_file_error(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        function_with_file_error(1, 0)

    with open(log_file, 'r') as f:
        log_contents = f.read()

    assert "Ошибка в функции 'function_with_file_error': division by zero. Аргументы: (1, 0)" in log_contents
