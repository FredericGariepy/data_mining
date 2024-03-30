'''
3/30/24
This Script uses a collection of subdirectories to harvests data into a csv file.
'''
import requests
from bs4 import BeautifulSoup
import csv
import sys
sys.stdout.reconfigure(encoding='utf-8')
import logging

# CONFIGS

# Configure logging with more specific level and formatting
logging.basicConfig(
    filename='scrapper.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Configure Source and Destination Files
url_source_file = 'SOURCE.txt'
data_out_file = 'DESTINATION.csv'

# Configure Base URL
base_url='https://www.example.com'

def harvestData(endpoint, count):
    url = base_url+endpoint
    try:
        response = requests.get(url=url)

        # Parse the HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        if response.status_code==200:
            try:
                # Find the text of the h1 tag
                school_name = soup.find('h1').get_text(strip=True)

                # Find the div with class "maininfo"
                maininfo_div = soup.find('div', class_='maininfo')
                
                # Extract information
                location = maininfo_div.find(class_='address').text.strip()
                emails = [email.text for email in maininfo_div.find(class_='mail').find_all('a')]
                phones = [phone.text for phone in maininfo_div.find(class_='phone').find_all('a')]
                websites = [website['href'] for website in maininfo_div.find(class_='www').find_all('a')]

                # Write to CSV
                with open(data_out_file, 'a', newline='', encoding='utf-8') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([school_name,', '.join(emails), ', '.join(phones), ', '.join(websites), location])
            
            except Exception as e:
                logger.error(f"Extraction error for {url} (endpoint: {endpoint}, file line: {count}): {e}")
        else:
            logger.error(f"Unexpected exception for URL {url} (endpoint: {endpoint}, file line: {count}): {e}")
    
    except Exception as e:
        logger.error(f"[X] Failure harvesting {endpoint} on file line {count}. Status Code: {response.status_code}")
        print(f" Exception for URL {url}: {e}\nSee error logs")

# Execution
print(f"Program {__name__} started..")
with open(file=url_source_file,mode='r',encoding='utf8') as file:
        for count, line in enumerate(file, start=1):
            # DEBUG: If scrapper was halted, un-comment both lines bellow to re-start from failpoint. Reffer to error log line count for failpoint.
            #if count < number:
            #    continue  # Skip lines until number specified
          
            endpoint = line.strip()
            try:
                harvestData(endpoint=endpoint,count=count)
                print(f"[{count}] Success harvesting {endpoint}")
            except Exception as e:
                print(f"[X] Failure harvesting {endpoint} on line {count}\nError: {e}\nSee error logs")
