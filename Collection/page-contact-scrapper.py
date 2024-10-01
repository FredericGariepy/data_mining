# This script simply scrapes the information from pages.
# The project is rather small, with only 1200~ records and all data was fetched.

# For larger projects, Improvements include:
# Data Extraction Check, Throttling requests, Logging and Error Handling

import csv
import requests
from bs4 import BeautifulSoup
import sys

# These are typical imports for throtling, regex expressions, logging.
# import time 
# import re
# import logging

# System stdout requires this config for foreign characters. Do not remove.
sys.stdout.reconfigure(encoding='utf-8')

# Define the input and output file paths
input_file = r'C:\...\school_links.csv'
output_file = r'C:\...\school_info.csv'

# Open the output CSV file outside the loop to keep it open
with open(output_file, mode='w', encoding="utf-8", newline='') as outfile:
    writer = csv.writer(outfile)
    # Write header to output CSV
    writer.writerow(['Title', 'Address', 'Email', 'Phone', 'Website', 'Director', 'Director Phone'])
    
    # Open the input CSV file and read the lines
    with open(input_file, mode='r', encoding="utf-8") as infile:
        reader = csv.reader(infile)
        
        # Process each line in the input CSV
        for index, line in enumerate(reader):
            # Create the full URL
            line = line[0].strip()
            url = f"https://www.redacted.domain/{line}"
            try:  
                response = requests.get(url)
                response.raise_for_status()

                #if response.status_code == 200:
                #    print(f"Processing index: {index}")

                soup = BeautifulSoup(response.text, 'html.parser')

                # Extract the information from the page
                main_info = soup.find(class_='maininfo')
                title = main_info.find('strong', class_='title').text.strip()
                address = main_info.find('li', class_='address').text.strip()
                email = main_info.find('li', class_='mail').a.text.strip()
                phone = main_info.find('li', class_='phone').a.text.strip()
                website = main_info.find('li', class_='www').a['href'].strip()
                director = main_info.find('li', class_='director').strong.text.strip()
                director_phone = main_info.find('li', class_='director').find_all('a')[0].text.strip()
                
                row = [title, address, email, phone, website, director, director_phone]
                #print(f"Writing row: {row}")

                writer.writerow(row)
                outfile.flush()  # Force write to disk
                
            except Exception as e:
                print(f"Error processing INDEX: {index} @ {url}: {e}")
           
print("Data extraction complete!")
