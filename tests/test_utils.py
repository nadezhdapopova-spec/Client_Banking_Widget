from typing import Any
from unittest.mock import mock_open, patch

from src.utils import deserialize_info


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
