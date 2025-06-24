import os

from config import ROOT_DIR
from src.external_api import transact_conversion_to_rubles
from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
from src.logging_config import masks_logger, utils_logger
from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_description, filter_by_state, sort_by_date
from src.reading_data_csv_excel import read_transactions_csv, read_transactions_excel
from src.utils import deserialize_info
from src.widget import get_date, mask_account_card


def main_1() -> None:
    """Вывод маски банковской карты и маски банковского счета клиента."""
    card_number = 4276838078111455
    account_number = 88427683807811146790
    # card_number = " "

    try:
        masks_logger.info(f"Получены данные card_number = {card_number}.")
        print("Маска банковской карты:", get_mask_card_number(card_number))
        masks_logger.info(f"Получены данные account_number = {account_number}.")
        print("Маска банковского счета:", get_mask_account(account_number))
    except Exception as e:
        masks_logger.error(f"Неудачная попытка ввода данных: {e}")
        print(f"Error: {e}")


# main_1()


def main_2() -> None:
    """Вывод маски банковской карты или маски банковского счета клиента."""
    account_or_card = "Visa Platinum 7000792289606361"
    # account_or_card = "Счет 73654108430135874305"
    # account_or_card = "Maestro 1596837868705199"
    # account_or_card = "Счет 73654108430135874305"
    # account_or_card = " "

    try:
        print(mask_account_card(account_or_card))
    except ValueError as e:
        print(f"Error: {e}")


# main_2()


def main_3() -> None:
    """Вывод даты в формате 'ДД.ММ.ГГГГ'."""
    date = "2024-03-11T02:26:18.671407"
    # date = "2024/03/11T02:26:18.671407"
    # date = " "
    print(get_date(date))


# main_3()


def main_4() -> None:
    """Вывод списка данных о банковских операциях, отфильтрованных по статусу."""

    state = "CANCELED"
    information = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                   {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                   {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                   {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

    print(filter_by_state(information, state))
    print(filter_by_state(information))


# main_4()


def main_5() -> None:
    """Вывод списка данных о банковских операциях, отсортированных по дате."""

    decrease = False
    information = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                   {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                   {'id': 594226727, 'state': 'CANCELED', 'date': '2019-09-12T21:27:25.241689'},
                   {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

    print(sort_by_date(information, decrease))
    # print(sort_by_date(information))
    print()


# main_5()


def main_6() -> None:
    """Вывод списка транзакций с заданной валютой."""

    target_currency = "USD"
    # target_currency = "руб."

    transactions = ([
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ])

    target_transactions = filter_by_currency(transactions, target_currency)

    for _ in range(4):
        print(next(target_transactions, "End"))


# main_6()


def main_7() -> None:
    """Вывод описания каждой операции транзакций по очереди."""
    transactions = ([
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ])

    descriptions = transaction_descriptions(transactions)

    for _ in range(6):
        print(next(descriptions, "End"))


# main_7()


def main_8() -> None:
    """Вывод номеров банковских карт в формате XXXX XXXX XXXX XXXX,
       сгенерированных в заданном диапазоне."""

    start = 1
    stop = 4

    try:
        card_numbers = card_number_generator(start, stop)

        for _ in range(5):
            print(next(card_numbers, "End"))

    except ValueError as e:
        print(f"Error: {e}")


# main_8()


def main_9() -> None:
    """Вывод из JSON-файла данных о финансовых транзакциях."""
    filepath = os.path.join(ROOT_DIR, r"data/operations.json")

    utils_logger.info(f"Получен путь до JSON-файла {filepath}.")
    print(deserialize_info(filepath))


# main_9()


def main_10() -> None:
    """Вывод суммы транзакции в рублях."""
    # transaction = {
    #     "id": 441945886,
    #     "state": "EXECUTED",
    #     "date": "2019-08-26T10:50:58.294041",
    #     "operationAmount": {
    #         "amount": "31957.58",
    #         "currency": {
    #             "name": "руб.",
    #             "code": "RUB"
    #         }
    #     },
    #     "description": "Перевод организации",
    #     "from": "Maestro 1596837868705199",
    #     "to": "Счет 64686473678894779589"
    # }
    #
    # transaction = {
    #     "id": 41428829,
    #     "state": "EXECUTED",
    #     "date": "2019-07-03T18:35:29.512364",
    #     "operationAmount": {
    #         "amount": "8221.37",
    #         "currency": {
    #             "name": "USD",
    #             "code": "USD"
    #         }
    #     },
    #     "description": "Перевод организации",
    #     "from": "MasterCard 7158300734726758",
    #     "to": "Счет 35383033474447895560"
    # }

    transaction = {
        "id": 441945868,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "EUR",
                "code": "EUR"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }

    print(f"{transact_conversion_to_rubles(transaction)} rub.")


# main_10()


def main_11() -> None:
    """Вывод из CSV-файла данных о финансовых операциях"""
    filepath = os.path.join(ROOT_DIR, "data", "transactions.csv")

    print(read_transactions_csv(filepath))


# main_11()


def main_12() -> None:
    """Вывод из XLSX-файла данных о финансовых операциях"""
    filepath = os.path.join(ROOT_DIR, "data", "transactions_excel.xlsx")

    print(read_transactions_excel(filepath))


# main_12()


def main_13() -> None:
    """Вывод списка данных о банковских операциях по заданному описанию"""
    target_description = "Перевод с карты на карту"
    # transactions = []
    transactions = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]

    print(filter_by_description(transactions, target_description))


main_13()
