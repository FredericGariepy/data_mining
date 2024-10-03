'''
pseudo - purpose built
holder for collections of webscraping 
11:44 PM 10/2/2024

What I was thinking here:
- build webscraping *compliance automation*
- Use the automation, allows more focus on scrapping
1:14 AM 10/3/2024
'''

import os
import sys

# Add the parent directory to the Python path, this is to call directory as modules // lovely wizard
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

# the compliance module I'm making
from compliance.robots import *
from config.settings import BASE_URL
url = BASE_URL

def main():
    print("Collecting robots.txt for compliance...")
    update_compliance()
    print("Collected robots.txt data.")
    print("Updating policies...")
    update_policy()
    print("Starting scrape..."
    scrape() #... 

          
# This needs a diffrent design.. I want the project to be a genral purpose scraping framework, accomodate, selenium/requests/bs4/etc
from utils.utlis import scrape_craigslist_titles
def scrape():
    titles = scrape_craigslist_titles(url=url)
    print(titles)

# Compliance
# This could use some refactoring, likely a compliaceManager class ?
def update_compliance():
    # Basically, from robots.txt get: disallow & crawl delay. Put them in JSON.
    # Use json to update settings || make a "Compliance Mode"
    robots_txt = get_robots_txt(url)
    if robots_txt:
        disallowed_paths = extract_disallowed_paths(robots_txt)
        crawl_delay = extract_crawl_delay(robots_txt)
        #user_agents = extract_user_agents(robots_txt)
        overwrite_compliance(disallowed_paths=disallowed_paths,crawl_delay=crawl_delay)
    
def update_policy():
    # Here is where compliance.json is used to configure settings & set policy
    pass
