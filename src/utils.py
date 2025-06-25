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


def formate_json_data(transactions: list[dict]) -> list[dict]:
    """Приведение списка транзакций из JSON-файла к единой форме"""
    formated_transactions = []
    for trans in transactions:
        trans_dict = {"id": trans.get("id"),
                      "state": trans.get("state"),
                      "date": trans.get("date"),
                      "amount": trans.get("operationAmount", {}).get("amount"),
                      "currency_name": trans.get("operationAmount", {}).get("currency", {}).get("name"),
                      "currency_code": trans.get("operationAmount", {}).get("currency", {}).get("code"),
                      "from": trans.get("from"),
                      "to": trans.get("to"),
                      "description": trans.get("description")}

        formated_transactions.append(trans_dict)

    return formated_transactions
