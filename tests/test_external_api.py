from typing import Any
from unittest.mock import Mock, patch

import pytest

from src.external_api import transact_conversion_to_rubles


@patch("src.external_api.os.getenv", return_value="fake_api_key")
@patch("src.external_api.requests.get")
def test_usd_conversion(mock_get: Any, mock_getenv: Any) -> None:
    mock_response = Mock()
    mock_response.json.return_value = {"result": 7900.00}
    mock_response.status_code = 200
    mock_get.return_value = mock_response

    assert transact_conversion_to_rubles(100, "USD") == 7900.00
    mock_get.assert_called_once()
    mock_getenv.assert_called_with("API_KEY")


@patch("src.external_api.os.getenv", return_value="fake_api_key")
@patch("src.external_api.requests.get")
def test_eur_conversion(mock_get: Any, mock_getenv: Any) -> None:
    mock_response = Mock()
    mock_response.json.return_value = {"result": 9001.00}
    mock_response.status_code = 200
    mock_get.return_value = mock_response

    assert transact_conversion_to_rubles(100, "EUR") == 9001.00
    mock_get.assert_called_once()
    mock_getenv.assert_called_with("API_KEY")


def test_conversion_invalid() -> None:
    with pytest.raises(ValueError):
        transact_conversion_to_rubles(100, "CNY")


@patch("src.external_api.requests.get")
def test_usd_conversion_error(mock_get: Any) -> None:
    mock_response = Mock()
    mock_response.json.return_value = {}
    mock_response.status_code = 404
    mock_get.return_value = mock_response

    with pytest.raises(Exception, match="Подключение не удалось"):
        transact_conversion_to_rubles(100, "USD")

    mock_get.assert_called_once()
