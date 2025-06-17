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
