import os
from typing import Any

from config import ROOT_DIR
from src.counters import count_bank_operations
from src.external_api import transact_conversion_to_rubles
from src.generators import filter_by_currency, transaction_descriptions
from src.logging_config import setup_logger
from src.processing import filter_by_description, filter_by_state, sort_by_date
from src.reading_data_csv_excel import read_transactions_csv, read_transactions_excel
from src.utils import deserialize_info, formate_json_data
from src.widget import get_date, mask_account_card

FROM_JSON = 1
FROM_CSV = 2
FROM_XLSX = 3
TO_RUBLES = 4
EXIT = 5
MIN_CHOICE = 1
MAX_CHOICE = 5


def main() -> None:
    """Выводит главное меню программы."""

    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n")

    choice = 0

    while choice != EXIT:
        display_menu()
        choice = get_menu_choice()

        transactions = []
        if choice == FROM_JSON:
            transactions = get_inform_from_json()
        elif choice == FROM_CSV:
            transactions = get_inform_from_csv()
        elif choice == FROM_XLSX:
            transactions = get_inform_from_xlsx()
        if choice == TO_RUBLES:
            convert_transact_to_rub()
            continue
        elif choice == EXIT:
            print("Всего доброго!")
            break

        if transactions is []:
            print("Ошибка доступа к данным. Попробуйте обратиться позже.")
        else:
            filtered_transactions = filtered_by_state(transactions)
            target_transactions = filter_by_options(filtered_transactions)
            masked_target_transactions = mask_transactions(target_transactions)
            target_transactions_output(masked_target_transactions)


def display_menu() -> None:
    """Меню получения информации о финансовых транзакциях."""
    print("""Выберите необходимый пункт меню:
            1. Получить информацию о транзакциях из JSON - файла
            2. Получить информацию о транзакциях из CSV - файла
            3. Получить информацию о транзакциях из XLSX - файла
            4. Конвертировать сумму транзакции из USD или EUR в RUB
            5. Выйти из программы""")


def get_menu_choice() -> int:
    """Получает у пользователя пункт меню."""
    choice = int(input(": "))

    while choice not in range(MIN_CHOICE, MAX_CHOICE+1):
        print(f"Допустимые варианты: {MIN_CHOICE} - {MAX_CHOICE}")
        choice = int(input(": "))

    return choice


def get_inform_from_json() -> list[dict]:
    """Получает из JSON-файла данные о финансовых транзакциях."""
    try:
        filepath = os.path.join(ROOT_DIR, r"data/operations.json")
        setup_logger().info(f"Получен путь до JSON-файла {filepath}.")

        transactions = deserialize_info(filepath)
        formated_transactions = formate_json_data(transactions)
    except FileNotFoundError:
        return []
    except ValueError:
        return []
    else:
        return formated_transactions


def get_inform_from_csv() -> list[dict]:
    """Получает из CSV-файла данные о финансовых транзакциях."""
    filepath = os.path.join(ROOT_DIR, "data", "transactions.csv")

    setup_logger().info(f"Получен путь до CSV-файла {filepath}.")
    transactions = read_transactions_csv(filepath)

    return transactions


def get_inform_from_xlsx() -> list[dict]:
    """Получает из XLSX-файла данные о финансовых транзакциях."""
    filepath = os.path.join(ROOT_DIR, "data", "transactions_excel.xlsx")

    setup_logger().info(f"Получен путь до XLSX-файла {filepath}.")
    transactions = read_transactions_excel(filepath)

    return transactions


def convert_transact_to_rub() -> None:
    """Возвращает сумму транзакции USD или EUR в рублях."""
    try:
        amount = float(input("Введите сумму транзакции (пример: 15811.0): "))
        currency = input("Введите код валюты (USD или EUR): ")

        print(f"{transact_conversion_to_rubles(amount, currency)} руб.\n")

    except ValueError:
        print("Введены некорректные данные\n")
    except Exception:
        print("Ошибка доступа. Попробуйте повторить позже\n")


def filtered_by_state(transactions: list[dict]) -> Any:
    """Получает у пользователя статус для отбора финансовых транзакций."""
    states = ("EXECUTED", "CANCELED", "PENDING")
    state = ""

    print("Введите статус, по которому необходимо выполнить фильтрацию")
    while state not in states:
        print(f"Доступные для фильтрации статусы: {", ".join(states)}")
        state = input(": ").upper()

    filtered_transactions = filter_by_state(transactions, state)

    print(f"Операции отфильтрованы по статусу {state}")

    return filtered_transactions


def filter_by_options(filtered_transactions: list[dict]) -> list[dict]:
    """Получает у пользователя дополнительные параметры для отбора финансовых транзакций."""
    filtered_transactions = list(filtered_transactions)

    by_date = input("Отсортировать операции по дате? Да/Нет: ")
    if by_date.lower() == "да":
        filtered_transactions = sorting_by_date(filtered_transactions)

    else:
        for transact in filtered_transactions:
            try:
                if isinstance(transact["date"], str):
                    transact["date"] = get_date(transact["date"])

            except KeyError:
                filtered_transactions.remove(transact)
                continue
            except ValueError:
                filtered_transactions.remove(transact)
                continue


    by_currency = input("Выводить только рублевые транзакции? Да/Нет: ")
    if by_currency.lower() == "да":
        filtered_transactions = list(filter_by_currency(filtered_transactions, "руб."))

    by_description = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ")
    if by_description.lower() == "да":
        filtered_transactions = filtration_by_description(filtered_transactions)

    return filtered_transactions


def sorting_by_date(filtered_transactions: list[dict]) -> Any:
    """Возвращает список финансовых транзакций, отсортированный по дате."""
    decrease = int(input("Отсортировать по возрастанию (нажмите 1) или по убыванию (нажмите 2)?: "))

    if decrease == 1:
        return sort_by_date(filtered_transactions, False)
    else:
        return sort_by_date(filtered_transactions)


def filtration_by_description(filtered_transactions: list[dict]) -> list[dict]:
    """Возвращает список финансовых транзакций, отфильтрованный по описанию."""
    print("Возможные варианты описания:")
    descriptions = transaction_descriptions(filtered_transactions)
    print(*descriptions, sep="\n")

    target_description = input("Введите слово из описания: ")
    filtered_transactions = filter_by_description(filtered_transactions, target_description)

    return filtered_transactions


def mask_transactions(target_transactions: list[dict]) -> list[dict]:
    """Возвращает список финансовых транзакций c масками номеров банковских карт и счетов"""
    target_transactions = list(target_transactions)

    for transact in target_transactions:
        try:
            transact["from"] = mask_account_card(transact["from"]) if transact["from"] else "None"
            transact["to"] = mask_account_card(transact["to"])

        except KeyError:
            target_transactions.remove(transact)
            continue
        except ValueError:
            target_transactions.remove(transact)
            continue

    return target_transactions


def target_transactions_output(target_transactions: list[dict]) -> None:
    """Выводит итоговый список финансовых транзакций."""
    categories = [transact["description"] for transact in target_transactions]
    categories_counter = count_bank_operations(target_transactions, categories)

    target_transactions = list(target_transactions)

    if len(target_transactions) == 0:
        print("\nНе найдено ни одной транзакции, подходящей под ваши условия фильтрации\n")

    else:
        print("\nРаспечатываю итоговый список транзакций...\n")
        print(f"Всего банковских операций в выборке: {len(target_transactions)}\n")
        print("Из них: ")
        for key, value in categories_counter.items():
            print(f"{key}: {value}")

        print()

        for transact in target_transactions:
            transact["date"] = get_date(transact["date"])
            print(f"{transact["date"]} {transact["description"]}")
            print(f"{transact["from"]} -> {transact["to"]}")
            print(f"Сумма: {transact["amount"]} {transact["currency_code"]}")
            print()


main()
