import regex as re
import pandas as pd
import requests
from datetime import datetime
from bs4 import BeautifulSoup


# Test access to the Edmunds website
url = 'https://cars.usnews.com/cars-trucks/advice/car-brands-available-in-america'
headers = {
    "User-Agent": "Mozilla/5.0"
}
response = requests.get(url, headers=headers)
try:
    status = response.status_code
    print(status)
except Exception as e:
    print(e)

soup = BeautifulSoup(response.content, 'html.parser')

print(soup)