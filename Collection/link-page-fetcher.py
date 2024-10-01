# This script will simply fetch listed relevant HREFs
# URLS and FILENAMES have been REDACTED.
# This is a small project with only 1200~ URLS to fetch.

import requests
from bs4 import BeautifulSoup
import csv

# Base URL format
base_url = "https://www.redacted/directory?p={page}"

with open('links.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)

    # 65 pages as of 01/10/24 (dd/mm/yy)
    # The total number of pages could be auto-fetched for a larger project.
    for page in range(1, 65):
        url = base_url.format(page=page)
        response = requests.get(url)
        
        if response.status_code != 200:
            print(f"Failed to retrieve page {page}: {response.status_code}")
            continue
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all <ul> elements with class 'schoollist cols1'
        school_lists = soup.find_all('ul', class_='schoollist cols1')
        
        if len(school_lists) >= 2:
            # Get the second <ul> element
            second_school_list = school_lists[1]
            
            # Find all <a> tags within the second <ul>
            links = second_school_list.find_all('a')
            
            # Write all href attributes to the CSV file
            for link in links:
                writer.writerow([link.get('href')])
        else:
            print(f"Length of array colleting class='schoollist cols1' < 2 : {page}")

print("Saved school links to 'school_links.csv'.")
