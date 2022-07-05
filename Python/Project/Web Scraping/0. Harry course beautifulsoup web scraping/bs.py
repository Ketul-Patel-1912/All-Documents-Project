from gettext import install
from http.client import REQUEST_ENTITY_TOO_LARGE
import bs4
import html5lib
from requests import request


# There is two way to scrape a website
# 1. USe the API
# 2. HTML web scraping using some tool like bs4

#Step-0 installing required librabry

# pip install request
# pip install html5lib
# pip install bs4

import requests
from bs4 import BeautifulSoup
url = 'https://codewithharry.com'

# Step-1 Get the HTML

r = requests.get(url)
htmlContent = r.content
# getting the html content in htmlcontent variable
# print(htmlContent)


# Step-2 Parse the HTML

soup = BeautifulSoup(htmlContent,'html.parser')
print(soup)


# Step-3 HTML Tree traversal