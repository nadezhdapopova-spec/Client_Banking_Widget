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
    (4301, "**4301")
])
def test_get_mask_account_success(account_number, expected):
    assert get_mask_account(account_number) == expected
    print(get_mask_account(account_number))


@pytest.mark.parametrize("account_number", [
    (305),
    (12),
    (9),
])
def test_get_mask_account_unacceptable_length(account_number):
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(account_number)
        assert str(exc_info.value) == "Номер счёта должен содержать не менее 4 цифр."


@pytest.mark.parametrize("account_number", [
    ("Ivan654108430135875112"),
    ("Иван88430135876805"),
    (-30135871711),
    (58742.15),
    ("☺4301"),
    ("#73654108430135874305"),
    ("654108430135875112@"),
    (" "),
    ("301358 71711"),
    (" 5874215 "),
    (" 5874215"),
    ("5874215 "),
    (---54108430135874305),
    ("_7365410843_0135874305_"),
    ("/7365410843_0135874305")
])
def test_get_mask_account_unacceptable_symbols(account_number):
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(account_number)
        assert str(exc_info.value) == "Номер счета должен содержать только цифры."
