from typing import Any, Dict, List, Optional


def filter_by_state(list_of_dict: List[Dict[Any, Any]], state='EXECUTED') -> List[Dict[Any, Any]]:
    ''' Функция принимает список словарей и опционально значение для ключа
state (по умолчанию 'EXECUTED') и возвращает новый список словарей, содержащий только те словари, у которых ключ
state соответствует указанному значению.'''
    filtered_list: List[Dict[Any, Any]] = []

    for dictionary in list_of_dict:
        if dictionary['state'] == state:
            filtered_list.append(dictionary)
        else:
            raise ValueError('Нет такого статуса')
    return filtered_list


def sort_by_date(list_of_dict: List[Dict[Any, Any]], sorting_param: Optional[bool] = False) -> List[Dict[Any, Any]]:
    ''' Функция принимает список словарей и необязательный параметр, задающий порядок сортировки
    (по умолчанию — убывание) и возвращает новый список, отсортированный по дате (date).'''
    sorted_list = sorted(list_of_dict, key=lambda x: x.get('date'), reverse=not sorting_param)
    return sorted_list
