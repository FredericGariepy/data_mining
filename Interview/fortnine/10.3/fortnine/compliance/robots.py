'''
This script is lacking for sophisticated robot.txt files where:
diffrent User-agents have diffrent sets of dis/allow

Can also collect Sitemap, Allows, etc

'''

import requests
import re
import json
import os

# Path to the compliance JSON file, it resides in the fortnite directory
compliance_json = os.path.join("compliance", "compliance.json") # or use path if necessary


def get_robots_txt(url: str):
    try:
        response = requests.get(f"{url}/robots.txt", timeout=5)
        response.raise_for_status()  # Raise an error for bad responses
        return response.text
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def extract_disallowed_paths(robots_txt: str):
    # Use regex to find lines starting with "Disallow:"
    disallow_pattern = re.compile(r"^Disallow:\s*(.*)", re.MULTILINE)
    disallowed_paths = disallow_pattern.findall(robots_txt)
    # Clean up the paths (strip whitespace)
    return [path.strip() for path in disallowed_paths if path.strip()]

def extract_crawl_delay(robots_txt: str):
    # Use regex to find lines starting with "Disallow:"
    crawl_delay_pattern = re.compile(r"^Crawl-delay:\s*(.*)", re.MULTILINE)
    crawl_delay_pattern = crawl_delay_pattern.findall(robots_txt)
    # Clean up the paths (strip whitespace)
    return [path.strip() for path in crawl_delay_pattern if path.strip()]

# not using this right now... Need to make a better solution for agent-specific Dis/allows
def extract_user_agents(robots_txt: str):
    # Use regex to find lines starting with "Disallow:"
    user_agent_pattern = re.compile(r"^User-agent::\s*(.*)", re.MULTILINE)
    user_agent_pattern = user_agent_pattern.findall(robots_txt)
    # Clean up the paths (strip whitespace)
    return [path.strip() for path in user_agent_pattern if path.strip()]

# Function to overwrite the compliance.json file
def overwrite_compliance(disallowed_paths, crawl_delay):
    # Prepare the data
    data = {
        "DISALLOW": disallowed_paths,
        "CRAWL_DELAY": crawl_delay,
    }
    
    # Write new data to compliance.json
    with open(compliance_json, 'w') as f:
        json.dump(data, f, indent=4)
