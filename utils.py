import requests
import json
from config import keys


class ConvertionError(Exception):
    pass


class CriptoConverter():
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionError('Базовая и котируемая валюта совпадают.')
        try:
            quote_ticker = keys[quote]
        except:
            raise ConvertionError(f'Не удалось обработать валюту {quote}.')
        try:
            base_ticker = keys[base]
        except:
            raise ConvertionError(f'Не удалось обработать валюту {base}.')
        try:
            amount = float(amount)
        except:
            raise ConvertionError(f'Не удалось обработать сумму в котируемой валюте {amount}.')

        r = requests.get(f'https://api.exchangeratesapi.io/latest?base={base_ticker}&symbols={quote_ticker}')
        global_base = json.loads(r.content)['rates'][keys[quote]]
        res = round(global_base * amount, 2)

        return res