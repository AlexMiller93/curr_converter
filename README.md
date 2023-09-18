### Currency Converter API

- [About](#about)
- [Getting Started](#getting_started)
- [Installing](#installing)
- [Usage](#usage)
- [Contributing](#contributing)

- [About]

This project converts currencies using data from external API. 
This version uses Django and Django REST Framework for API architecture and library requests to scraping the Fixer.io website in search of currencies quotes.

- [Getting Started]

Clone project from GitHub
`git clone https://github.com/AlexMiller93/curr_converter`

Move to project folder
`cd ../CurrencyConverter`

- [Installing]

For Windows
`python3 -m venv env` install virtual environment
`.\env\Scripts\activate` activate

For Linux/Mac
`python3 -m venv env` install virtual environment
`source env/bin/activate` activate

To run local server
`python manage.py runserver`

- [Usage]

To get current rates from fixer.io you should send request like 
`http://data.fixer.io/api/latest?access_key={access_key}`

To get access_key you should visit website fixer.io and sign up. 
https://fixer.io/

In this project user can calculate quantity of currency using 2 ways, 
by clicking button in html template or by writing GET response with parameters.

1. User writes a quantity of currency need to convert to another one. 
Choose two currencies from list and press button to calculate value with POST request.

2. User writes GET request like
`GET /api/rates?from=USD&to=RUB&value=1` where USD and RUB are currencies and value is 1.
Server response will be a dict with key "result" and value. 

- [Contributing]

Project Stack:
Django 4.2.5
DRF 3.14.0
Requests

##  Future updates

1. Install Docker
2. Add animation via CSS and JavaScript
3. Implement function using JS and JQuery
4. Add list of several past exchanges