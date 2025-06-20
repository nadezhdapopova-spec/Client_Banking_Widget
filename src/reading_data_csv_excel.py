import pandas as pd


def read_transactions_csv(filepath: str) -> list[dict]:
    """Функция для считывания финансовых операций из CSV-файлов"""
    transactions_reviews = pd.read_csv(filepath, delimiter=";")
    transactions_reviews.set_index(transactions_reviews.id, drop=False, inplace=True)

    trans_reviews_dict = transactions_reviews.to_dict(orient="records")

    return trans_reviews_dict


def read_transactions_excel(filepath: str) -> list[dict]:
    """Функция для считывания финансовых операций из XLSX-файлов"""
    transactions_reviews = pd.read_excel(filepath)
    transactions_reviews.set_index(transactions_reviews.id, drop=False, inplace=True)

    trans_reviews_dict = transactions_reviews.to_dict(orient="records")

    return trans_reviews_dict
