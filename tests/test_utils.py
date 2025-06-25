from typing import Any
from unittest.mock import mock_open, patch

import pytest

from src.utils import deserialize_info, formate_json_data


@patch("os.path.getsize", return_value=123)
@patch("builtins.open", new_callable=mock_open, read_data='[{"key": "value"}]')
def test_deserialize_info_valid(mock_file: Any, mock_getsize: Any) -> None:
    result = deserialize_info("fake_path_test.json")
    assert result == [{"key": "value"}]
    mock_file.assert_called_once_with("fake_path_test.json", encoding="utf-8")


@patch("os.path.getsize", return_value=0)
def test_deserialize_info_empty_file(mock_getsize: Any) -> None:
    result = deserialize_info("fake_path_test.json")
    assert result == []
    mock_getsize.assert_called_once()


@patch("os.path.getsize", return_value=123)
@patch("builtins.open", new_callable=mock_open, read_data='{"not": "a list"}')
def test_deserialize_info_not_list(mock_file: Any, mock_getsize: Any) -> None:
    result = deserialize_info("fake_path_test.json")
    assert result == []
    mock_getsize.assert_called_once()


@patch("os.path.getsize", return_value=123)
@patch("builtins.open", side_effect=FileNotFoundError)
def test_file_not_found_on_open(mock_file: Any, mock_getsize: Any) -> None:
    result = deserialize_info("not_exist.json")
    assert result == []


def test_formate_json_data_success(transactions_from_json: list[dict],
                                   transactions_formated_from_json: list[dict]) -> None:
    assert formate_json_data(transactions_from_json) == transactions_formated_from_json


def test_formate_json_data_space() -> None:
    assert formate_json_data([]) == []


@pytest.mark.parametrize("transactions_list, expected", [
    ([
         {
             "id": 441945886,
             "state": "EXECUTED",
             "date": "2019-08-26T10:50:58.294041",
             "operationAmount": {
                 "amount": "31957.58",
                 "currency": {
                     "name": "руб.",
                     "code": "RUB"
                 }
             },
             "from": "Maestro 1596837868705199",
             "to": "Счет 64686473678894779589"
         }
     ],
        [
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "amount": "31957.58",
                "currency_name": "руб.",
                "currency_code": "RUB",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589",
                "description": None
            }
        ])
])
def test_formate_json_data_invalid(transactions_list: list[dict],
                                   expected: list[dict]) -> None:
    assert formate_json_data(transactions_list) == expected
