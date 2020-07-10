from bs4 import BeautifulSoup
import requests
import numpy as np
from requests import get
import re

headers = {"Accept-Language": "en-US, en;q=0.5"}
url = "https://medium.com/better-programming/how-to-scrape-multiple-pages-of-a-website-using-a-python-web-scraper-4e2c641cff8"
results = requests.get(url, headers=headers)
soup = BeautifulSoup(results.text, "html.parser")
link_div = soup.find('div')
link_p = soup.find_all('div', class_='data-selectable-paragraph')
link_button = soup.find('div')

title = link_div.h1.text
numText = 0
for container in link_p:
    x = len(container.p.text.split())
    numText = numText + x


print(title)
print(numText)

