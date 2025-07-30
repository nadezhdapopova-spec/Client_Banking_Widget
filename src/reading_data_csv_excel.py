import os

import pandas as pd

from src.logging_config import setup_logger


def read_transactions_csv(filepath: str) -> list[dict]:
    """Функция для считывания финансовых операций из CSV-файлов"""
    if not os.path.isfile(filepath):
        setup_logger().error(f"Файл {filepath} не найден.")
        raise FileNotFoundError(f"Файл {filepath} не существует.")

    if os.path.getsize(filepath) == 0:
        setup_logger().warning(f"Файл {filepath} пустой.")
        raise ValueError(f"Файл {filepath} пустой.")

    setup_logger().info(f"Чтение CSV-файла {filepath}.")
    transactions_reviews = pd.read_csv(filepath, delimiter=";")
    transactions_reviews.set_index(transactions_reviews.id, drop=False, inplace=True)

    trans_reviews_dict = transactions_reviews.to_dict(orient="records")

    setup_logger().info(f"CSV-файл {filepath} преобразован в Python-объект.")
    return trans_reviews_dict


def read_transactions_excel(filepath: str) -> list[dict]:
    """Функция для считывания финансовых операций из XLSX-файлов"""
    if not os.path.isfile(filepath):
        setup_logger().error(f"Файл {filepath} не найден.")
        raise FileNotFoundError(f"Файл {filepath} не существует.")

    if os.path.getsize(filepath) == 0:
        setup_logger().warning(f"Файл {filepath} пустой.")
        raise ValueError(f"Файл {filepath} пустой.")

    setup_logger().info(f"Чтение XLSX-файла {filepath}.")
    transactions_reviews = pd.read_excel(filepath)
    transactions_reviews.set_index(transactions_reviews.id, drop=False, inplace=True)

    trans_reviews_dict = transactions_reviews.to_dict(orient="records")

    setup_logger().info(f"XLSX-файл {filepath} преобразован в Python-объект.")
    return trans_reviews_dict
