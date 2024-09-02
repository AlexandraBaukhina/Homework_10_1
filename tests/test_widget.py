import pytest
from src.widget import get_date, mask_account_card


@pytest.mark.parametrize('value, expected', [
    ('', 'Номер карты или счета должен содержать от 16 цифр'),
    ('2202201598965830', '2202 20** **** 5890'),
    ('20258963254127569146', '**5830'),
    ('Счет 73654108430135874305', 'Счет **4305')
])
def test_mask_account_card(value, expected):
    assert mask_account_card(value) == expected


@pytest.mark.parametrize('value, expected', [
    ('', 'Введите дату в формате "ГГГГ-ММ-ДДT02:26:18.671407'),
    ('2000-06-15', 'Введите дату в формате "ГГГГ-ММ-ДДT02:26:18.671407'),
    ('2024-03-11T02:26:18.671407', '11.03.2024'),
])
def test_get_date(value, expected):
    assert get_date(value) == expected
