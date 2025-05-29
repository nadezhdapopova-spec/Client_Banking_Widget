from mypyc.crash import Iterator


def filter_by_currency(transactions: list[dict], target_currency: str) -> Iterator:
    """Фильтрует транзакции по заданной валюте"""

    filtered_transactions = (desc for desc in transactions if
                             desc["operationAmount"]["currency"]["name"] == target_currency)

    return filtered_transactions


def transaction_descriptions(transactions: list[dict]) -> Iterator:
    """Возвращает описание каждой операции транзакции по очереди"""

    descriptions = (desc["description"] for desc in transactions)

    for desc in descriptions:
        yield desc


# def card_number_generator():
#
