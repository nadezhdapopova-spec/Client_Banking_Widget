from typing import Any
from unittest.mock import patch

import pandas as pd
import pytest

from src.reading_data_csv_excel import read_transactions_csv, read_transactions_excel

@patch("src.reading_data_csv_excel.os.path.getsize", return_value=123)
@patch("src.reading_data_csv_excel.os.path.isfile", return_value=True)
@patch("src.reading_data_csv_excel.pd.read_csv")
def test_read_transactions_csv(mock_read_csv: Any, mock_getsize: Any, mock_isfile: Any) -> None:
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


@patch("src.reading_data_csv_excel.os.path.getsize", return_value=0)
@patch("src.reading_data_csv_excel.os.path.isfile", return_value=True)
@patch("src.reading_data_csv_excel.pd.read_csv")
def test_read_transactions_csv_empty(mock_read_csv: Any, mock_getsize: Any, mock_isfile: Any) -> None:
    fake_df = pd.DataFrame([{}])
    mock_read_csv.return_value = fake_df

    with pytest.raises(ValueError):
        read_transactions_csv("fake/path.csv")

    mock_getsize.assert_called_once()


@patch("src.reading_data_csv_excel.os.path.getsize", return_value=123)
@patch("src.reading_data_csv_excel.os.path.isfile", return_value=False)
@patch("src.reading_data_csv_excel.pd.read_csv")
def test_read_transactions_csv_not_file(mock_read_csv: Any, mock_getsize: Any, mock_isfile: Any) -> None:
    fake_df = pd.DataFrame([{}])
    mock_read_csv.return_value = fake_df

    with pytest.raises(FileNotFoundError):
        read_transactions_csv("fake/path.csv")


@patch("src.reading_data_csv_excel.os.path.getsize", return_value=123)
@patch("src.reading_data_csv_excel.os.path.isfile", return_value=True)
@patch("src.reading_data_csv_excel.pd.read_excel")
def test_read_transactions_excel(mock_read_excel: Any, mock_getsize: Any, mock_isfile: Any) -> None:
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


@patch("src.reading_data_csv_excel.os.path.getsize", return_value=0)
@patch("src.reading_data_csv_excel.os.path.isfile", return_value=True)
@patch("src.reading_data_csv_excel.pd.read_excel")
def test_read_transactions_excel_empty(mock_read_excel: Any, mock_getsize: Any, mock_isfile: Any) -> None:
    fake_df = pd.DataFrame([{}])
    mock_read_excel.return_value = fake_df

    with pytest.raises(ValueError):
        read_transactions_csv("fake/path.excel")

    mock_getsize.assert_called_once()


@patch("src.reading_data_csv_excel.os.path.getsize", return_value=123)
@patch("src.reading_data_csv_excel.os.path.isfile", return_value=False)
@patch("src.reading_data_csv_excel.pd.read_excel")
def test_read_transactions_excel_not_file(mock_read_excel: Any, mock_getsize: Any, mock_isfile: Any) -> None:
    fake_df = pd.DataFrame([{}])
    mock_read_excel.return_value = fake_df

    with pytest.raises(FileNotFoundError):
        read_transactions_excel("fake/path.excel")
