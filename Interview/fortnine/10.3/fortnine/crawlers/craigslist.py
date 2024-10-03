import requests
from bs4 import BeautifulSoup

def scrape_craigslist_titles(url):
    headers = {''} # to set, also based on configs...
    response = requests.get(url) # headers, timeouts from compliance... 
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')

    a_tags = soup.find_all('a')
    return a_tags