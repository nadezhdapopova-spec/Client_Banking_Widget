import os

from config import ROOT_DIR
from src.decorators import log
from src.logging_config import setup_logger


# @log()
@log(filename=os.path.join(ROOT_DIR, r"data/mylog.txt"))
def get_mask_card_number(card_number: int | str) -> str:
    """
    Функция для получения маски номера банковской карты
    в формате XXXX XX** **** XXXX
    """
    card_symbols = str(card_number)

    if len(card_symbols) != 16:
        setup_logger().error(f"Номер карты {card_number} имеет недопустимую длину.")
        raise ValueError("Номер карты должен содержать 16 цифр.")
    if not card_symbols.isdigit():
        setup_logger().error(f"Номер карты {card_number} имеет недопустимые символы.")
        raise ValueError("Номер карты должен содержать только цифры.")

    setup_logger().info(f"Маска для номера карты {card_number} создана.")
    return f"{card_symbols[:4]} {card_symbols[4:6]}** **** {card_symbols[-4:]}"


# @log()
@log(filename=os.path.join(ROOT_DIR, r"data/mylog.txt"))
def get_mask_account(account_number: int | str) -> str:
    """Функция для получения маски номера банковского счёта в формате **XXXX"""
    account_symbols = str(account_number)

    if len(account_symbols) < 4:
        setup_logger().error(f"Номер счёта {account_number} имеет недопустимую длину.")
        raise ValueError("Номер счёта должен содержать не менее 4 цифр.")

    if not account_symbols.isdigit():
        setup_logger().error(f"Номер счёта {account_number} имеет недопустимые символы.")
        raise ValueError("Номер счета должен содержать только цифры.")

    setup_logger().info(f"Маска для номера счёта {account_number} создана.")
    return f"**{account_symbols[-4:]}"
