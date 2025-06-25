import pytest

from src.counters import count_bank_operations


@pytest.mark.parametrize("expected", [
    {
        "Перевод организации": 2,
        "Перевод со счета на счет": 2,
        "Перевод с карты на карту": 1
    }
])
def test_count_bank_operations_success(transactions: list[dict],
                                       transact_descriptions: list,
                                       expected) -> None:
    assert count_bank_operations(transactions, transact_descriptions) == expected


def test_count_bank_operations_space(transactions: list,
                                     transact_descriptions: list) -> None:
    assert count_bank_operations([], transact_descriptions) == {}
