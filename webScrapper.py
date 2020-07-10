from bs4 import BeautifulSoup
import requests
from random import randint
import numpy as np
from time import sleep

minWord = 2000
minClaps = 1000
headers = {"Accept-Language": "en-US, en;q=0.5"}
numWords = 0
numClaps = 0

pages = np.arange(1, 1001, 50)

for page in pages:
    page = requests.get("https://www.medium.com" + str(page), headers=headers)
    content = BeautifulSoup(page.text, "html.parser")
    link_div = content.find_all('div')
    sleep(randint(2, 10))


    def get_numWords():
        y = 0
        for text in page.find_all('p', class_='data-selectable-paragraph'):
            res = text.p.text
            x = res.split()
            y = y + len(x)
        return y


    def get_numClaps():
        y = page.h4.button.text
        x = 0
        if 'K' in y:
            y.replace("K", "")
            x = 1000 * int(y)
        else:
            x = int(y)
        return x


    for container in link_div:
        # Title
        title = container.h1.a.text

        # URL
        url = page.request.url

        # Words
        totalWords = numWords.get_numWords()

        # Claps
        totalClaps = numClaps.get_numClaps()

        # Saves to a text file after checking if article meets standards
        if totalWords > minWord and totalClaps > minClaps:
            file1 = open("Articles", 'w')
            file1.write("Title: " + title + "\n")
            file1.write("URL: " + url + "\n")
            file1.write("Total Words: " + totalWords + "\n")
            file1.write("Total Claps: " + totalClaps + "\n")
            file1.close()

