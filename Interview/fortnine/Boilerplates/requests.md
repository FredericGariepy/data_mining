import requests

# Define the proxy server
proxies = {
    'http': 'http://your_proxy_server:port',
    'https': 'http://your_proxy_server:port',
}

# The target URL you want to scrape
url = 'http://example.com'

try:
    # Send a request through the proxy
    response = requests.get(url, proxies=proxies, timeout=10)

    # Check if the request was successful
    if response.status_code == 200:
        print(response.text)  # Process the response as needed
    else:
        print(f"Failed to access {url}: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
