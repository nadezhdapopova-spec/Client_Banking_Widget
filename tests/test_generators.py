import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


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


def test_filter_by_currency_invalid(valid_information) -> None:
    generator = filter_by_currency(valid_information, "руб.")
    with pytest.raises(KeyError):
        next(generator, "End")


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


def test_transaction_descriptions_invalid(valid_information) -> None:
    generator = transaction_descriptions(valid_information)
    with pytest.raises(KeyError):
        next(generator, "End")
