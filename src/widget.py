from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_or_account: str) -> str:
    """
    Функция для получения маски номера банковского счёта в формате **XXXX
    или маски номера банковской карты в формате XXXX XX** **** XXXX
    """
    if not card_or_account.replace(" ", "").isalnum():
        raise ValueError("Обнаружены некорректные символы")
    if "Счет" in card_or_account:
        account_number = ""
        for symbol in card_or_account:
            if symbol.isdigit():
                account_number += symbol
        return f"Счет {get_mask_account(int(account_number))}"
    else:
        card_number = ""
        card_name = ""
        for symbol in card_or_account:
            if symbol.isdigit():
                card_number += symbol
            else:
                card_name += symbol
        return f"{card_name}{get_mask_card_number(int(card_number))}"
