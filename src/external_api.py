import os

import requests
from dotenv import load_dotenv

load_dotenv()

def transact_conversion_to_rubles(transact: dict) -> float:
    """Конвертирует валюту из USD и EUR в рубли и возвращает сумму транзакции в рублях."""
    valid_for_conversion = ["USD", "EUR"]
    cur_to = "RUB"
    cur_from = transact.get("currency_code")
    amount = transact["amount"]
    url = f"https://api.apilayer.com/exchangerates_data/convert"

    if not transact["currency_code"]: raise KeyError("Некорректные данные")
    if transact["currency_code"] == "RUB": return float(transact["amount"])
    if transact["currency_code"] not in valid_for_conversion: raise ValueError("Некорректные данные")

    params = {
        "to": cur_to,
        "from": cur_from,
        "amount": amount
    }

    headers = {
        "apikey": os.getenv('API_KEY')
    }

    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200: raise Exception("Подключение не удалось")

    try:
        get_data = response.json()
        result = round(get_data["result"], 2)
    except Exception as err:
        print(err)
    else:
        return float(result)
