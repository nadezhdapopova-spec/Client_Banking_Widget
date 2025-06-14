from typing import Any
from unittest.mock import Mock, patch

import pytest

from src.external_api import transact_conversion_to_rubles


def test_rub_conversion() -> None:
    transact = {
        "operationAmount": {
            "amount": 10000.5,
            "currency": {
                "code": "RUB"
            }
        }
    }

    assert transact_conversion_to_rubles(transact) == 10000.5


@patch("os.getenv", return_value="fake_api_key")
@patch("requests.get")
def test_usd_conversion(mock_get: Any, mock_getenv: Any) -> None:
    mock_response = Mock()
    mock_response.json.return_value = {"result": 7900.00}
    mock_get.return_value = mock_response

    transact = {
        "operationAmount": {
            "amount": 100,
            "currency": {
                "code": "USD"
            }
        }
    }

    assert transact_conversion_to_rubles(transact) == 7900.00
    mock_get.assert_called_once()
    mock_getenv.assert_called_with("API_KEY")


@patch("os.getenv", return_value="fake_api_key")
@patch("requests.get")
def test_eur_conversion(mock_get: Any, mock_getenv: Any) -> None:
    mock_response = Mock()
    mock_response.json.return_value = {"result": 9001.00}
    mock_get.return_value = mock_response

    transact = {
        "operationAmount": {
            "amount": 100,
            "currency": {
                "code": "EUR"
            }
        }
    }

    assert transact_conversion_to_rubles(transact) == 9001.00
    mock_get.assert_called_once()
    mock_getenv.assert_called_with("API_KEY")


def test_conversion_invalid() -> None:
    transact = {
        "operationAmount": {
            "amount": 100,
            "currency": {
                "code": "CNY"
            }
        }
    }

    with pytest.raises(ValueError):
        transact_conversion_to_rubles(transact)


def test_conversion_without_value() -> None:
    transact = {
        "operationAmount": {
            "amount": 100,
            "currency": {
                "code": ""
            }
        }
    }

    with pytest.raises(KeyError):
        transact_conversion_to_rubles(transact)


def test_conversion_space() -> None:
    transact: dict = {}

    with pytest.raises(KeyError):
        transact_conversion_to_rubles(transact)
