import pytest
from src.widget import get_date, mask_account_card



@pytest.mark.parametrize('value, expected', [
    ('', 'Номер карты или счета должен содержать от 16 цифр')
])
def test_mask_account_card(value, expected):
    assert mask_account_card('Счет 73654108430135874305') == 'Счет **4305'
    assert mask_account_card('20258963254127569146') == '**9146'
    assert mask_account_card('2202201598965830') == '2202 20** **** 5830'
    with pytest.raises(ValueError) as exc_info:
        mask_account_card(value)
    assert str(exc_info.value) == expected



@pytest.mark.parametrize('value, expected', [
    ('', 'Введите дату в формате "ГГГГ-ММ-ДДT02:26:18.671407'),
    ('2000-06-15', 'Введите дату в формате "ГГГГ-ММ-ДДT02:26:18.671407'),
])
def test_get_date(value, expected):
    with pytest.raises(ValueError) as exc_info:
        get_date(value)
    assert str(exc_info.value) == 'Введите дату в формате "ГГГГ-ММ-ДДT02:26:18.671407'
    assert get_date('2024-03-11T02:26:18.671407') == '11.03.2024'
