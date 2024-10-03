import requests
from bs4 import BeautifulSoup

def scrape_craigslist_titles(url):
    # Send a GET request to the Craigslist page
    response = requests.get(url) # this should be informed by rate limiting, dis/allows, user-agents, etc
    response.raise_for_status()  # Raise an error for bad responses

    # Parse the page content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all posting titles
    titles = []
    postings = soup.find_all('a', class_='cl-app-anchor text-only posting-title')
    
    for post in postings:
        title = post.get_text(strip=True)  # Get text, stripping whitespace
        href = post['href']  # Get the href attribute
        titles.append((title, href))  # Store title and URL as a tuple

    return titles
