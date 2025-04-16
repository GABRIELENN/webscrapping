import requests
from bs4 import BeautifulSoup
from .config import BBC_NEWS_URL, HEADERS

def fetch_homepage():
    response = requests.get(BBC_NEWS_URL, headers=HEADERS)
    response.raise_for_status()
    return response.text

def get_soup(html):
    return BeautifulSoup(html, "html.parser")
