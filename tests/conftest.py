import pytest


@pytest.fixture
def valid_information() -> list[dict]:  # Для позитивного тестирования
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


@pytest.fixture
def information_without_executed() -> list[dict]:  # Для позитивного тестирования
    return [{'id': 41428829, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'CANCELED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


@pytest.fixture
def information_without_canceled() -> list[dict]:  # Для позитивного тестирования
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'EXECUTED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'EXECUTED', 'date': '2018-10-14T08:21:33.419441'}]


@pytest.fixture
def information_with_same_dates() -> list[dict]:  # Для позитивного тестирования
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2019-07-03T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2019-07-03T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2019-07-03T08:21:33.419441'}]
