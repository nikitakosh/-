from bs4 import BeautifulSoup as bs
import requests

def get_html(url):
    response = requests.get(url)
    soup = bs(response.text, 'lxml')
    return soup


def get_content()
url = "https://www.hltv.org/results"
get_html(url)