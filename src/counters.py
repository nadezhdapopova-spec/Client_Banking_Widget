from collections import Counter


def count_bank_operations(transactions:list[dict], categories:list)->dict:
    descriptions = [transact["description"] for transact in transactions if transact["description"] in categories]

    counted = dict(Counter(descriptions))

    return counted
