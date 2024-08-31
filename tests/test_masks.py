import pytest
from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize('value, expected', [
    ('','Номер карты должен содержать 16 цифр'),
    ('20258963254127569146', 'Номер карты должен содержать 16 цифр'),
    ('2202201598965830','2202 20** **** 5890')
])
def test_card_number(value, expected):
    assert get_mask_card_number(value) == expected


@pytest.mark.parametrize('value, expected', [
    ('','Номер счета должен содержать 18 цифр'),
    ('20258963254127569146', 'Номер счета должен содержать 18 цифр'),
    ('492202201598965830','**5830')
])
def test_account(value, expected):
    assert get_mask_account(value) == expected

