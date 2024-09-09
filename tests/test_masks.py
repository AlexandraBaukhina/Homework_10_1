import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize('value, expected', [
    ('', 'Номер карты должен содержать 16 цифр'),
    ('20258963254127569146', 'Номер карты должен содержать 16 цифр')
])
def test_card_number(value, expected):
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(value)
    assert str(exc_info.value) == 'Номер карты должен содержать 16 цифр'
    assert get_mask_card_number('2202201598965830') == '2202 20** **** 5830'


@pytest.mark.parametrize('value, expected', [
    ('', 'ValueError: Номер счета должен содержать 18 цифр'),
    ('20258963254127569146', 'ValueError: Номер счета должен содержать 18 цифр')
])
def test_account(value, expected):
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(value)
    assert str(exc_info.value) == 'Номер карты должен содержать 16 цифр'
    assert get_mask_account('492202201598965830') == '**5830'
