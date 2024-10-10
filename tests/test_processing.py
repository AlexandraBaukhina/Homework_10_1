import pytest

from src.processing import sort_by_operation_cathegory, filter_by_state, sort_by_date, sort_by_string


def test_filter(list_of_dict_for_test, filtering, bla_filtering, list_of_dict_state):
    with pytest.raises(ValueError) as exc_bla_info:
        filter_by_state(bla_filtering)
    assert str(exc_bla_info.value) == 'Нет такого статуса'
    assert filter_by_state(list_of_dict_for_test) == filtering
    assert filter_by_state(list_of_dict_for_test, state='CANCELED') == list_of_dict_state
    with pytest.raises(ValueError) as exc_zero_info:
        filter_by_state(list_of_dict_for_test, state='0')
    assert str(exc_zero_info.value) == 'Нет такого статуса'


def test_sort(list_of_dict_for_sort_test, sorting, list_of_dict_reverse, list_of_dict_repeat_date,
              list_of_dict_for_sort_repeat_date, bla_sorting_list, bla_sorting):
    assert sort_by_date(list_of_dict_for_sort_test) == sorting
    assert sort_by_date(list_of_dict_for_sort_test, sorting_param=True) == list_of_dict_reverse
    assert sort_by_date(list_of_dict_repeat_date) == list_of_dict_for_sort_repeat_date
    assert sort_by_date(bla_sorting_list) == bla_sorting


@pytest.mark.parametrize("list_of_dict, search_string, expected", [
    ([], 'test', []),  # пустой список
    ([{'id': 1}, {'id': 2}], 'test', []),  # список без описания
    ([{'id': 1, 'description': 'test1'}, {'id': 2, 'description': 'test2'}], 'test3', []),  # список без совпадений
    ([{'id': 1, 'description': 'test1'}, {'id': 2, 'description': 'test2'}], 'test',
     [{'id': 1, 'description': 'test1'}, {'id': 2, 'description': 'test2'}]),  # список с совпадениями
    ([{'id': 1, 'description': 'Test1'}, {'id': 2, 'description': 'test2'}], 'test',
     [{'id': 1, 'description': 'Test1'}, {'id': 2, 'description': 'test2'}]),
    # список с совпадениями, игнорируя регистр
    ([{'id': 1, 'description': 'test1'}, {'id': 2, 'description': 'test2'}, {'id': 3, 'description': 'test3'}], 'test',
     [{'id': 1, 'description': 'test1'}, {'id': 2, 'description': 'test2'}, {'id': 3, 'description': 'test3'}]),
    # список с несколькими совпадениями
])
def test_sort_by_string(list_of_dict, search_string, expected):
    assert sort_by_string(list_of_dict, search_string) == expected


@pytest.mark.parametrize("list_of_dict, list_of_category, expected", [
    ([], ['category1', 'category2'], {}),  # пустой список операций
    ([{'id': 1, 'description': 'test1'}, {'id': 2, 'description': 'test2'}], [], {}),  # пустой список категорий
    ([{'id': 1, 'description': 'test1'}, {'id': 2, 'description': 'test2'}], ['category1', 'category2'], {}),
    # нет совпадений
    ([{'id': 1, 'description': 'category1 test1'}, {'id': 2, 'description': 'test2'}], ['category1', 'category2'],
     {'category1': 1}),  # одно совпадение
    ([{'id': 1, 'description': 'category1 test1'}, {'id': 2, 'description': 'category2 test2'}],
     ['category1', 'category2'], {'category1': 1, 'category2': 1}),  # два совпадения
    ([{'id': 1, 'description': 'category1 test1'}, {'id': 2, 'description': 'category1 test2'},
      {'id': 3, 'description': 'category2 test3'}], ['category1', 'category2'], {'category1': 2, 'category2': 1}),
    # несколько совпадений
])
def test_sort_by_operation_category(list_of_dict, list_of_category, expected):
    assert sort_by_operation_cathegory(list_of_dict, list_of_category) == expected
