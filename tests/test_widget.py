import pytest
from src.widget import mask_account_card, get_date


@pytest.mark.parametrize("card_or_account, expected", [
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
    ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
    ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
    ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
    (" Visa Gold 5999414228426353 ", "Visa Gold 5999 41** **** 6353"),
    ("Счет 73654108430135874305", "Счет **4305"),
    ("Счет 64686894779589", "Счет **9589"),
    ("Счет 5560", "Счет **5560"),
    ("Счет 736541084301358743057365410843013587430573654108430135874305", "Счет **4305"),
    (" Счет 73654108430135874305 ", "Счет **4305")
])
def test_mask_account_card_success(card_or_account: str, expected: str) -> None:
    assert mask_account_card(card_or_account) == expected


@pytest.mark.parametrize("card_or_account", [
    ("Счет 605"),
    ("Счет 14"),
    ("Счет 8"),
])
def test_mask_account_card_invalid_length_account(card_or_account: str) -> None:
    with pytest.raises(ValueError) as exc_info:
        mask_account_card(card_or_account)
    assert str(exc_info.value) == "Номер счёта должен содержать не менее 4 цифр."


@pytest.mark.parametrize("card_or_account", [
    ("Visa Platinum 70007922896063615"),
    ("Visa Classic 7000792289645896063615"),
    ("Maestro 7000792289606361570007922896063615")
])
def test_mask_account_card_invalid_length_card(card_or_account: str) -> None:
    with pytest.raises(ValueError) as exc_info:
        mask_account_card(card_or_account)
    assert str(exc_info.value) == "Номер карты должен содержать 16 цифр."


@pytest.mark.parametrize("card_or_account", [
    ("Maestro -1596837868705199"),
    ("Maestro 15968378687051.99"),
    ("Maestro ---7000792820683"),
    ("Maestro ☺700079221406361"),
    ("Maestro #700079228606361"),
    ("Maestro 700079228606361@"),
    ("Maestro _700722_8960661_"),
    ("Maestro /700079228606361"),
    ("Счет -1596837868705199"),
    ("Счет 15968378687051.99"),
    ("Счет ---7000792820683"),
    ("Счет ☺700079221406361"),
    ("Счет #700079228606361"),
    ("Счет 700079228606361@"),
    ("Счет _700722_8960661_"),
    ("Счет /700079228606361"),
    (" "),
    ("")
])
def test_mask_account_card_invalid_symbols(card_or_account: str) -> None:
    with pytest.raises(ValueError) as exc_info:
        mask_account_card(card_or_account)
    assert str(exc_info.value) == "Обнаружены некорректные символы."
