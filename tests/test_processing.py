import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize("state, expected", [
    ("EXECUTED",
    [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]),
    ("CANCELED",
    [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}])
])
def test_filter_by_state_success(valid_information: list[dict], state: str ,expected: list[dict]) -> None:
    assert filter_by_state(valid_information, state) == expected


@pytest.mark.parametrize("expected", [
    [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
])
def test_filter_by_state_without_state(valid_information: list[dict],
                                       expected: list[dict],
                                       state: str="EXECUTED",) -> None:
    assert filter_by_state(valid_information, state) == expected


@pytest.mark.parametrize("state, expected", [
    ("EXECUTED",
     [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
      {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
      {'id': 594226727, 'state': 'EXECUTED', 'date': '2018-09-12T21:27:25.241689'},
      {'id': 615064591, 'state': 'EXECUTED', 'date': '2018-10-14T08:21:33.419441'}]),
    ("CANCELED", [])
])
def test_filter_by_state_without_canceled(information_without_canceled: list[dict],
                                 state: str,
                                 expected: list[dict]) -> None:
    assert filter_by_state(information_without_canceled, state) == expected


@pytest.mark.parametrize("state, expected", [
    ("EXECUTED", []),
    ("CANCELED",
     [{'id': 41428829, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'},
      {'id': 939719570, 'state': 'CANCELED', 'date': '2018-06-30T02:08:58.425572'},
      {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
      {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}])
])
def test_filter_by_state_without_executed(information_without_executed: list[dict],
                                 state: str,
                                 expected: list[dict]) -> None:
    assert filter_by_state(information_without_executed, state) == expected


@pytest.mark.parametrize("invalid_information, state, expected", [
    ([{'id': 41428829, 'state': '', 'date': '2019-07-03T18:35:29.512364'},
      {'id': 41428829, 'state': '', 'date': '2019-07-03T18:35:29.512364'}], "EXECUTED", []),
    ([{'id': 41428829, 'state': '####', 'date': '2019-07-03T18:35:29.512364'},], "EXECUTED", []),
    ([{'id': 41428829, 'state': 12345, 'date': '2019-07-03T18:35:29.512364'},], "EXECUTED", []),
    ([{'id': 41428829, 'state': "hello", 'date': '2019-07-03T18:35:29.512364'},], "CANCELED", []),
    ([{'id': 41428829, 'state': "CANCELED_CANCELED", 'date': '2019-07-03T18:35:29.512364'},], "CANCELED", []),
    ([{'id': 41428829, 'state': "canceled", 'date': '2019-07-03T18:35:29.512364'},], "CANCELED", [])
])
def test_filter_by_state_invalid(invalid_information: list[dict],
                                 state: str,
                                 expected: list) -> None:
    assert filter_by_state(invalid_information, state) == expected
