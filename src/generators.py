import os

from config import ROOT_DIR
from src.decorators import log
from mypyc.crash import Iterator


# @log()
@log(filename=os.path.join(ROOT_DIR, r"data/mylog.txt"))
def filter_by_currency(transactions: list[dict], target_currency: str) -> Iterator:
    """Фильтрует транзакции по заданной валюте"""

    filtered_transactions = (transact for transact in transactions if
                             transact["operationAmount"]["currency"]["name"] == target_currency)

    return filtered_transactions


# @log()
@log(filename=os.path.join(ROOT_DIR, r"data/mylog.txt"))
def transaction_descriptions(transactions: list[dict]) -> Iterator:
    """Возвращает описание каждой операции транзакции по очереди"""

    descriptions = (transact["description"] for transact in transactions)

    for desc in descriptions:
        yield desc


# @log()
@log(filename=os.path.join(ROOT_DIR, r"data/mylog.txt"))
def card_number_generator(start: int, stop: int) -> Iterator:
    """Генерирует и возвращает номера банковских карт в заданном диапазоне номеров"""

    if start <= 0 or start > 9999999999999999:
        raise ValueError("Заданы невалидные значения.")

    if stop > 9999999999999999:
        raise ValueError("Заданы невалидные значения.")

    if start > stop:
        raise ValueError("Заданы невалидные значения.")

    card_numbers = (str(num).zfill(16) for num in range(start, stop + 1))

    for card_num in card_numbers:
        yield f"{card_num[:4]} {card_num[4:8]} {card_num[8:12]} {card_num[12:]}"
