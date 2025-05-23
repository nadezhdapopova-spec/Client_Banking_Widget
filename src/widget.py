from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_or_account: str) -> str:
    """
    Функция для получения маски номера банковского счёта в формате **XXXX
    или маски номера банковской карты в формате XXXX XX** **** XXXX
    """
    if not card_or_account.replace(" ", "").isalnum():
        raise ValueError("Обнаружены некорректные символы.")

    number = ""
    title = ""

    card_or_account = card_or_account.strip()

    for symbol in card_or_account:
        if symbol.isdigit():
            number += symbol
        else:
            title += symbol

    if "Счет" in card_or_account:
        return f"{title}{get_mask_account(int(number))}"
    else:
        return f"{title}{get_mask_card_number(int(number))}"


def get_date(date: str) -> str:
    """
    Функция для преобразования даты в формат 'ДД.ММ.ГГГГ'
    """
    return f"{date[8:10]}.{date[5:7]}.{date[:4]}"
