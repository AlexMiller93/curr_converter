from django.conf import settings
from django.db import models

import requests
from bs4 import BeautifulSoup

# Create your models here.


class Converter(models.Model):
    """

    """
    from_curr = models.CharField(max_length=5, help_text="Input currency")
    to_curr = models.CharField(max_length=5, help_text="Output currency")
    value = models.SmallIntegerField(help_text="Quantity to be converted")
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"From {self.from_curr} to {self.to_curr} \
        in quantity {self.value} {self.from_curr} in {self.timestamp}"

    def convert(self, from_curr, to_curr, value):
        """

        :param from_curr:
        :param to_curr:
        :param value:
        :return:
        """

        # fixer settings
        base_url = 'http://data.fixer.io/api/convert'
        # endpoint = 'convert'
        access_key = settings.FIXER_API_KEY

        # http://data.fixer.io/api/convert
        #     ? access_key = e64c0f09804e73eea3aad67345b8eddd
        #     & from = GBP
        #     & to = JPY
        #     & amount = 25

        try:
            # parse currency rate from Fixer

            url = f"{base_url}?{access_key}&from={from_curr}&to={to_curr}&amount={value}"
            response = requests.get(url)
            data = response.json()
            result = data["result"]

            quantity = round(result, 2)
            return quantity

        except:
            return "No valid data"

