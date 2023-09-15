import requests
from bs4 import BeautifulSoup


def get_quotes(from_curr: str, to_curr: str):
    """

    :param from_curr:
    :param to_curr:
    :return:
    """

    try:
        # parse currency rate from Fixer

        url = f""
        response = requests.get(url)


        return rate
    except:
        return "No valid data"
