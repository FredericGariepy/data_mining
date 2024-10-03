'''
pseudo - purpose built
holder for collections of webscraping 
11:44 PM 10/2/2024
'''


import os
import sys

# Add the parent directory to the Python path
# this is to call directory as modules // lovely wizardry
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

from compliance.robots import *
from config.settings import BASE_URL

from utils.utlis import scrape_craigslist_titles

url = BASE_URL

def main():
    print("Collecting robots.txt for compliance...")
    update_compliance()
    print("Collected robots.txt data.")
    scrape() #...

def scrape():
    titles = scrape_craigslist_titles(url=url)
    print(titles)





# Compliance
# This could use some refactoring possibly, likely a compliaceManager class ?
def update_compliance():
    # Basically, update the DISALLOW in compliance
    robots_txt = get_robots_txt(url)
    if robots_txt:
        disallowed_paths = extract_disallowed_paths(robots_txt)
        crawl_delay = extract_crawl_delay(robots_txt)
        #user_agents = extract_user_agents(robots_txt)
        overwrite_compliance(disallowed_paths=disallowed_paths,crawl_delay=crawl_delay)



def scrape():
    pass