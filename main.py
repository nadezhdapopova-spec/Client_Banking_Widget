from src.masks import get_mask_account, get_mask_card_number


def main() -> None:
    """ Вывод маски банковской карты и маски банковского счета клиента"""
    card_number = 4276838078111455
    account_number = 88427683807811146790
    try:
        print("Маска банковской карты:", get_mask_card_number(card_number))
        print("Маска банковского счета:", get_mask_account(account_number))
    except ValueError as e:
        print(f"Error: {e}")


main()
