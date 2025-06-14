import os

import requests
from dotenv import load_dotenv


def transact_conversion_to_rubles(transact: dict) -> float:
    """Конвертирует валюту из USD и EUR в рубли и возвращает сумму транзакции в рублях."""
    valid_for_conversion = ["USD", "EUR"]

    if transact["operationAmount"]["currency"]["code"] in valid_for_conversion:
        cur_to = "RUB"
        cur_from = transact["operationAmount"]["currency"]["code"]
        amount = transact["operationAmount"]["amount"]
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={cur_to}&from={cur_from}&amount={amount}"

        load_dotenv()
        api_key = os.getenv('API_KEY')
        headers = {
            "apikey": api_key
        }

        response = requests.get(url, headers=headers).json()

        result = round(response["result"], 2)

    elif transact["operationAmount"]["currency"]["code"] == "RUB":
        result = transact["operationAmount"]["amount"]

    else:
        raise ValueError("Некорректные данные.")

    return float(result)
