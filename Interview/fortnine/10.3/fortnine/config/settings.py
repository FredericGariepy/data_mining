import os
import sys
# Add the parent directory to the Python path
# this is to call directory as modules // lovely wizardry
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

BASE_URL = "https://nsa.gov/"

CRAWL_DELAY = 0
