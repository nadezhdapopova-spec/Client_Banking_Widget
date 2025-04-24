def get_mask_card_number(card_number: int) -> str:
    """
    Функция для получения маски номера банковской карты
    в формате XXXX XX** **** XXXX
    """
    card_symbols = str(card_number)
    if len(card_symbols) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр.")
    if not card_symbols.isdigit():
        raise ValueError("Номер карты должен содержать только цифры.")
    return f"{card_symbols[:4]} {card_symbols[4:6]}** **** {card_symbols[-4:]}"


def get_mask_account(account_number: int) -> str:
    """
    Функция для получения маски номера банковского счёта в формате **XXXX
    """
    account_symbols = str(account_number)
    if len(account_symbols) < 4:
        raise ValueError("Номер счёта должен содержать не менее 4 цифр.")
    if not account_symbols.isdigit():
        raise ValueError("Номер счета должен содержать только цифры.")
    return f"**{account_symbols[-4:]}"
