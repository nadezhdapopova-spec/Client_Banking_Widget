import pytest
from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize("account_number, expected", [
    ("73654108430135874305", "**4305"),
    (736541084301358743057365410843013587430573654108430135874305, "**4305"),
    (73654108430135874305, "**4305"),
    (654108430135875112, "**5112"),
    (88430135876805, "**6805"),
    (30135871711, "**1711"),
    (5874215, "**4215"),
    (4301, "**4301"),
    (99999999999999999999, "**9999"),
    (10000000000000000000, "**0000")
])
def test_get_mask_account_success(account_number, expected):
    assert get_mask_account(account_number) == expected


@pytest.mark.parametrize("account_number", [
    (305),
    (12),
    (9),
    ()
])
def test_get_mask_account_unacceptable_length(account_number):
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(account_number)
        assert str(exc_info.value) == "Номер счёта должен содержать не менее 4 цифр."


@pytest.mark.parametrize("account_number", [
    (-30135871711),
    (58742.15),
    (---54108430135874305),
    ("Ivan654108430135875112"),
    ("Иван88430135876805"),
    ("☺4301"),
    ("#73654108430135874305"),
    ("654108430135875112@"),
    (" "),
    ("301358 71711"),
    (" 5874215 "),
    (" 5874215"),
    ("5874215 "),
    ("_7365410843_0135874305_"),
    ("/7365410843_0135874305")
])
def test_get_mask_account_unacceptable_symbols(account_number):
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(account_number)
        assert str(exc_info.value) == "Номер счета должен содержать только цифры."


@pytest.mark.parametrize("card_number, expected", [
    ("7970002289606361", "7970 00** **** 6361"),
    (7000792289606361, "7000 79** **** 6361"),
    (8150502982606163, "8150 50** **** 6163"),
    (9999999999999999, "9999 99** **** 9999"),
    (1000000000000000, "1000 00** **** 0000")
])
def test_get_mask_card_number_success(card_number, expected):
    assert get_mask_card_number(card_number) == expected
    print(get_mask_card_number(card_number))


@pytest.mark.parametrize("card_number", [
    (79700022896063613),
    (797000228960636797000228960636797000228960636),
    (797000228960636),
    (79700022896063),
    (7970002289606),
    (797000228960),
    (79700022896),
    (7970002289),
    (797000228),
    (79700022),
    (7970002),
    (797000),
    (79700),
    (7970),
    (797),
    (79),
    (7),
    ()
])
def test_get_mask_card_number_unacceptable_length(card_number):
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(card_number)
        assert str(exc_info.value) == "Номер карты должен содержать 16 цифр."


@pytest.mark.parametrize("card_number", [
    (-7000792289606361),
    (700079228960.6361),
    (---7000792289606361),
    ("Ivan7000792289606361"),
    ("Иван7000792289606361"),
    ("☺7000792289606361"),
    ("#7000792289606361"),
    ("7000792289606361@"),
    (" "),
    ("7000 7922 896063 61"),
    (" 7000792289606361 "),
    (" 7000792289606361"),
    ("7000792289606361 "),
    ("_70007922_89606361_"),
    ("/7000792289606361")
])
def test_get_mask_card_number_unacceptable_symbols(card_number):
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(card_number)
        assert str(exc_info.value) == "Номер карты должен содержать только цифры."
