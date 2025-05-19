def filter_by_state(operations_information: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Фильтрация списка данных о банковских операциях по статусу"""

    return [inform for inform in operations_information if inform["state"] == state]


def sort_by_date(operations_information: list[dict], decrease: bool = True) -> list[dict]:
    """Сортировка списка данных о банковских операциях по дате"""

    return sorted(operations_information, key=lambda inform: inform['date'], reverse=decrease)
