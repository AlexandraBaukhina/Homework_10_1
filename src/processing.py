import re
from collections import Counter
from typing import Any, Dict, List, Optional


def filter_by_state(list_of_dict: List[Dict[Any, Any]], state='EXECUTED') -> List[Dict[Any, Any]]:
    ''' Функция принимает список словарей и опционально значение для ключа
state (по умолчанию 'EXECUTED') и возвращает новый список словарей, содержащий только те словари, у которых ключ
state соответствует указанному значению.'''
    filtered_list = [dictionary for dictionary in list_of_dict if dictionary['state'] == state]
    if len(filtered_list) == 0:
        raise ValueError('Нет такого статуса')
    return filtered_list


def sort_by_date(list_of_dict: List[Dict[Any, Any]], sorting_param: Optional[bool] = False) -> List[Dict[Any, Any]]:
    ''' Функция принимает список словарей и необязательный параметр, задающий порядок сортировки
    (по умолчанию — убывание) и возвращает новый список, отсортированный по дате (date).'''
    sorted_list = sorted(list_of_dict, key=lambda x: x.get('date'), reverse=not sorting_param)
    return sorted_list


def sort_by_string(list_of_dict: List[Dict[Any, Any]], search_string: str) -> List[Dict[Any, Any]]:
    """ Функция принимает список словарей с данными о банковских операциях и строку поиска,
     а возвращает список словарей, у которых в описании есть данная строка."""
    result = []
    pattern = re.compile(search_string, re.IGNORECASE)
    for operation in list_of_dict:
        if 'description' in operation and pattern.search(operation['description']):
            result.append(operation)
    return result


def sort_by_operation_cathegory(list_of_dict: List[Dict[Any, Any]], list_of_cathegory: List) -> Dict[Any, Any]:
    ''' Функция принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращает словарь, в котором ключи — это названия категорий, а значения — это количество операций
    в каждой категории.'''
    category_counts = Counter()
    for operation in list_of_dict:
        for category in list_of_cathegory:
            if category in operation['description']:
                category_counts[category] += 1
                break
    return dict(category_counts)
