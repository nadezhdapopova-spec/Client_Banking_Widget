from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
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


def main_4() -> None:
    """Вывод списка данных о банковских операциях, отфильтрованных по статусу"""

    state = "CANCELED"
    information = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                   {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                   {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                   {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

    print(filter_by_state(information, state))
    print(filter_by_state(information))


main_4()


def main_5() -> None:
    """Вывод списка данных о банковских операциях, отсортированных по дате"""

    decrease = False
    information = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                   {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                   {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                   {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

    print(sort_by_date(information, decrease))
    print(sort_by_date(information))


main_5()
