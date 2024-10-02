import requests
from bs4 import BeautifulSoup

def fetch_page(url):
    # Set headers to mimic a browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    
    try:
        # Use a session to persist certain parameters across requests
        with requests.Session() as session:
            response = session.get(url, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses
            
            return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def parse_html(html):
    if html is None:
        return
    
    soup = BeautifulSoup(html, 'html.parser')
    
    # Example: Extracting titles and links from <h2> tags
    for h2 in soup.find_all('h2'):
        title = h2.get_text(strip=True)
        link = h2.find('a')['href'] if h2.find('a') else None
        print(f"Title: {title}, Link: {link}")

def main():
    url = 'https://example.com'  # Replace with your target URL
    html = fetch_page(url)
    parse_html(html)

if __name__ == "__main__":
    main()
