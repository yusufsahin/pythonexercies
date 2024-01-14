# beautiful_soup_example.py
from bs4 import BeautifulSoup
import requests

response = requests.get('http://freshquietyoungzen.neverssl.com/online/')
soup = BeautifulSoup(response.content, 'html.parser')
print(soup.title.text)

