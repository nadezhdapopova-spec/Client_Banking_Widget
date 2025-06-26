from collections import Counter


def count_bank_operations(transactions: list[dict], categories: list) -> dict:
    """Считает количество операций для каждой категории банковских транзакций."""
    descriptions = [transact["description"] for transact in transactions if transact["description"] in categories]

    counted = dict(Counter(descriptions))

    return counted
