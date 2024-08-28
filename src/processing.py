from typing import Dict, List, Optional


def filter_by_state(list_of_dict: List[Dict], state='EXECUTED') -> List[Dict]:
    ''' Функция принимает список словарей и опционально значение для ключа
state (по умолчанию 'EXECUTED') и возвращает новый список словарей, содержащий только те словари, у которых ключ
state соответствует указанному значению.'''
    new_list_of_dict: List[Dict] = [{}]

    for dictionary in list_of_dict:
        if dictionary['state'] == state:
            new_list_of_dict.append(dictionary)
    return new_list_of_dict


def sort_by_date(list_of_dict: List[Dict], sorting_param: Optional[bool] = False) -> List[Dict]:
    ''' Функция принимает список словарей и необязательный параметр, задающий порядок сортировки
    (по умолчанию — убывание) и возвращает новый список, отсортированный по дате (date).'''
    new_list_of_dict = sorted(list_of_dict, key=lambda x: x.get('date'), reverse=not sorting_param)
    return new_list_of_dict
