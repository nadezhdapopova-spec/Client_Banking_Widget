from typing import Any

import pandas as pd

from unittest.mock import patch

from src.reading_data_csv_excel import read_transactions_csv, read_transactions_excel


@patch("src.reading_data_csv_excel.pd.read_csv")
def test_read_transactions_csv(mock_read_csv: Any) -> None:
    fake_df = pd.DataFrame([
        {"id": 1, "value": "A"},
        {"id": 2, "value": "B"},
    ])

    mock_read_csv.return_value = fake_df

    result = read_transactions_csv("fake/path.csv")

    expected = [
        {"id": 1, "value": "A"},
        {"id": 2, "value": "B"}
    ]

    assert result == expected
    mock_read_csv.assert_called_once_with("fake/path.csv", delimiter=";")


@patch("src.reading_data_csv_excel.pd.read_excel")
def test_read_transactions_excel(mock_read_excel: Any) -> None:
    fake_df = pd.DataFrame([
        {"id": 1, "value": "A"},
        {"id": 2, "value": "B"},
    ])

    mock_read_excel.return_value = fake_df

    result = read_transactions_excel("fake/path.xlsx")

    expected = [
        {"id": 1, "value": "A"},
        {"id": 2, "value": "B"}
    ]

    assert result == expected
    mock_read_excel.assert_called_once_with("fake/path.xlsx")
