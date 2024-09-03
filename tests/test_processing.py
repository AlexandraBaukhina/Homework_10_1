import pytest
from src.processing import filter_by_state, sort_by_date


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
