import requests
# import functools

from cachetools import TTLCache,cached


class OpenExchangeClient:
    BASE_URL = "https://openexchangerates.org/api"

    def __init__(self, app_id):
        self.app_id = app_id

    @property
    # @functools.lru_cache(maxsize=2)
    @cached(cache=TTLCache(maxsize=2,ttl=900))
    def latest(self):
        return requests.get(f"{self.BASE_URL}/latest.json?app_id={self.app_id}").json()

    def convert(self, from_amt, from_currency, to_currency):
        rates = self.latest["rates"]
        to_rate = rates[to_currency]

        if from_currency == "USD":
            return from_amt * to_rate
        else:
            from_in_usd = from_amt / rates[to_currency]
            return from_in_usd * to_rate
