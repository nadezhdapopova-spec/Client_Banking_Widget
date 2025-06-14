import json
import os


def deserialize_info(filepath: str) -> list[dict]:
    """Преобразование JSON-строки в Python-объекты"""
    if os.path.getsize(filepath) == 0:
        return []

    try:
        with open(filepath, encoding="utf-8") as f:
            data = json.load(f)

            if not isinstance(data, list):
                return []

            return data

    except FileNotFoundError:
        return []
