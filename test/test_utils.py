import pytest
from utils.func import unpacking, get_last, get_filter, get_formatted_data


#@pytest.fixture
test_data = [
      {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-02-26T10:50:58.294041",
        "operationAmount": {
          "amount": "31957.58",
          "currency": {
            "name": "руб.",
            "code": "RUB"
          }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
      },
      {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
          "amount": "8221.37",
          "currency": {
            "name": "USD",
            "code": "USD"
          }
        },
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560"
      },
      {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
          "amount": "9824.07",
          "currency": {
            "name": "USD",
            "code": "USD"
          }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
      },
      {
        "id": 587085106,
        "state": "EXECUTED",
        "date": "2018-03-23T10:45:06.972075",
        "operationAmount": {
          "amount": "48223.05",
          "currency": {
            "name": "руб.",
            "code": "RUB"
          }
        },
        "description": "Открытие вклада",
        "to": "Счет 41421565395219882431"
      },
      {
        "id": 142264268,
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
          "amount": "79114.93",
          "currency": {
            "name": "USD",
            "code": "USD"
          }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"
      },
      {
        "id": 873106923,
        "state": "CANCELED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {
          "amount": "43318.34",
          "currency": {
            "name": "руб.",
            "code": "RUB"
          }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160"
      }
    ]


def test_unpacking():
    url = "https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1677769174003&signature=dSPXH_zkbz8InyyiumNfoTD1aPpC0kwflF-dJh9CWa4&downloadName=operations.json"
    assert unpacking(url) is not None
    url = "https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1677769174003&signature=dSPXH_zkbz8InyyiumNfoTD1aPpC0kwflF-dJh9CWa4&downloadNam=operations.json"
    data, info = unpacking(url)
    assert data is None
    info_warning = info.split()
    assert info_warning[0] == "WARNING:"


def test_get_filter():
    data = get_filter(test_data[0:])
    assert len(data) == 4
    data = get_filter(test_data[0:], True)
    assert len(data) == 3


def test_get_last():
    data = get_last(test_data[0:], 5)
    assert data[0]['date'] == "2019-07-03T18:35:29.512364"
    assert data[1]['date'] == "2019-04-04T23:20:05.206878"
    assert len(get_last(test_data[0:], 5)) == 5
    assert len(get_last(test_data[0:3], 5)) == 3


def test_get_formatted_data():
    data = get_formatted_data(test_data[:2])
    assert len(data) == 2
    assert data[0] == "26.02.2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n31957.58 руб.\n"
