from src.masks import get_mask_account, get_mask_card_number
from src.widget import get_date, mask_account_card


def main_1() -> None:
    """Вывод маски банковской карты и маски банковского счета клиента"""
    card_number = 4276838078111455
    account_number = 88427683807811146790

    try:
        print("Маска банковской карты:", get_mask_card_number(card_number))
        print("Маска банковского счета:", get_mask_account(account_number))
    except ValueError as e:
        print(f"Error: {e}")


main_1()


def main_2() -> None:
    """Вывод маски банковской карты или маски банковского счета клиента"""
    account_or_card = "Visa Platinum 7000792289606361"
    # account_or_card = "Счет 73654108430135874305"
    # account_or_card = "Maestro 1596837868705199"
    # account_or_card = "Счет 73654108430135874305"

    try:
        print(mask_account_card(account_or_card))
    except ValueError as e:
        print(f"Error: {e}")


main_2()


def main_3() -> None:
    """Вывод даты в формате 'ДД.ММ.ГГГГ'"""
    date = "2024-03-11T02:26:18.671407"
    print(get_date(date))


main_3()
