import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency_usd(transactions: list[dict],
                                filtered_transactions_usd: list[dict]) -> None:
    generator = filter_by_currency(transactions, "USD")
    assert next(generator, "End") == filtered_transactions_usd[0]
    assert next(generator, "End") == filtered_transactions_usd[1]
    assert next(generator, "End") == filtered_transactions_usd[2]
    assert next(generator, "End") == "End"


def test_filter_by_currency_rub(transactions: list[dict],
                                filtered_transactions_rub: list[dict]) -> None:
    generator = filter_by_currency(transactions, "руб.")
    assert next(generator, "End") == filtered_transactions_rub[0]
    assert next(generator, "End") == filtered_transactions_rub[1]
    assert next(generator, "End") == "End"
    assert next(generator, "End") == "End"


def test_filter_by_currency_no_current_transact(filtered_transactions_rub: list[dict]) -> None:
    generator = filter_by_currency(filtered_transactions_rub, "USD")
    assert next(generator, "End") == "End"
    assert next(generator, "End") == "End"


def test_filter_by_currency_space_list() -> None:
    generator = filter_by_currency([], "руб.")
    assert next(generator, "End") == "End"
    assert next(generator, "End") == "End"


# def test_filter_by_currency_invalid(valid_information: list[dict]) -> None:
#     generator = filter_by_currency(valid_information, "руб.")
#     with pytest.raises(KeyError):
#         next(generator, "End")


def test_transaction_descriptions(transactions: list[dict],
                                  transact_descriptions: list[str]) -> None:
    generator = transaction_descriptions(transactions)
    assert next(generator, "End") == transact_descriptions[0]
    assert next(generator, "End") == transact_descriptions[1]
    assert next(generator, "End") == transact_descriptions[2]
    assert next(generator, "End") == transact_descriptions[3]
    assert next(generator, "End") == transact_descriptions[4]
    assert next(generator, "End") == "End"


def test_transaction_descriptions_usd(filtered_transactions_usd: list[dict],
                                      transact_descriptions: list[str]) -> None:
    generator = transaction_descriptions(filtered_transactions_usd)
    assert next(generator, "End") == transact_descriptions[0]
    assert next(generator, "End") == transact_descriptions[1]
    assert next(generator, "End") == transact_descriptions[3]
    assert next(generator, "End") == "End"


def test_transaction_descriptions_space() -> None:
    generator = transaction_descriptions([])
    assert next(generator, "End") == "End"
    assert next(generator, "End") == "End"


def test_transaction_descriptions_invalid(valid_information: list[dict]) -> None:
    generator = transaction_descriptions(valid_information)
    with pytest.raises(KeyError):
        next(generator, "End")


def test_card_number_generator_valid_small_num() -> None:
    generator = card_number_generator(1, 4)
    assert next(generator, "End") == "0000 0000 0000 0001"
    assert next(generator, "End") == "0000 0000 0000 0002"
    assert next(generator, "End") == "0000 0000 0000 0003"
    assert next(generator, "End") == "0000 0000 0000 0004"
    assert next(generator, "End") == "End"


def test_card_number_generator_valid_num() -> None:
    generator = card_number_generator(123456789110, 123456789113)
    assert next(generator, "End") == "0000 1234 5678 9110"
    assert next(generator, "End") == "0000 1234 5678 9111"
    assert next(generator, "End") == "0000 1234 5678 9112"
    assert next(generator, "End") == "0000 1234 5678 9113"
    assert next(generator, "End") == "End"


def test_card_number_generator_valid_big_num() -> None:
    generator = card_number_generator(9999999999999999, 9999999999999999)
    assert next(generator, "End") == "9999 9999 9999 9999"
    assert next(generator, "End") == "End"


def test_card_number_generator_invalid_stop() -> None:
    generator = card_number_generator(9999999999999999, 9999999999999995)
    with pytest.raises(ValueError):
        next(generator, "End")


def test_card_number_generator_invalid_start_null() -> None:
    generator = card_number_generator(0, 5)
    with pytest.raises(ValueError):
        next(generator, "End")


def test_card_number_generator_invalid_big_num() -> None:
    generator = card_number_generator(12345678123456781, 12345678123456783)
    with pytest.raises(ValueError):
        next(generator, "End")


def test_card_number_generator_invalid_big_stop() -> None:
    generator = card_number_generator(9999999999999999, 10000000000000000)
    with pytest.raises(ValueError):
        next(generator, "End")


def test_card_number_generator_invalid_nums() -> None:
    generator = card_number_generator(5, 1)
    with pytest.raises(ValueError):
        next(generator, "End")
