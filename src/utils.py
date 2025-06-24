import json
import os

from src.logging_config import utils_logger


def deserialize_info(filepath: str) -> list[dict]:
    """Преобразование JSON-строки в Python-объекты."""
    try:
        if os.path.getsize(filepath) == 0:
            utils_logger.warning(f"Файл {filepath} пустой.")
            return []

        utils_logger.info(f"Чтение JSON-файла {filepath}.")
        with open(filepath, encoding="utf-8") as f:
            data = json.load(f)

            if not isinstance(data, list):
                utils_logger.warning(f"Файл {filepath} не содержит список.")
                return []

            utils_logger.info(f"JSON-файл {filepath} преобразован в Python-объект.")
            return data

    except FileNotFoundError:
        utils_logger.error(f"Файл {filepath} не найден.")
        return []


def formate_json_data(transactions):
    """Приведение списка транзакций из JSON-файла к единой форме"""
    keys = ["id", "state", "date", "amount", "currency_name", "currency_code", "from", "to", "description"]
    formated_transactions = []

    for trans in transactions:
        trans_dict = {"id": trans["id"], "state": trans["state"], "date": trans["date"],
                      "amount": trans["operationAmount"]["amount"],
                      "currency_name": trans["operationAmount"]["currency"]["name"],
                      "currency_code": trans["operationAmount"]["currency"]["code"], "from": trans["from"],
                      "to": trans["to"], "description": trans["description"]}

        formated_transactions.append(trans_dict)

    return formated_transactions
