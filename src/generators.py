from mypyc.crash import Iterator

def filter_by_currency(transactions: list[dict], target_currency: str) -> Iterator:
    """Фильтрация транзакций по заданной валюте"""

    filtered_transactions = (cur for cur in transactions if
                             cur["operationAmount"]["currency"]["name"] == target_currency)
    for transaction in filtered_transactions:
        yield transaction
