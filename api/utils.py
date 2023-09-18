import requests
from django.conf import settings


def parse_latest_rates():
    """
    Function to parse latest rates from fixer.io

    :return: a dictionary with currencies info - code and rate.
    """

    base_url = 'http://data.fixer.io/api/'
    endpoint = 'latest'
    access_key = settings.FIXER_API_KEY

    url = base_url + endpoint + '?access_key=' + access_key
    response = requests.get(url).json()
    currencies = response.get('rates')

    return currencies


