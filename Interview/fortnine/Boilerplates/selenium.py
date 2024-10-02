from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# Firefox options
options = Options()
options.headless = True  # Run in headless mode

# Set up proxy
proxy = "http://your_proxy:port"
options.add_argument(f'--proxy-server={proxy}')

# Start Firefox with geckodriver
driver = webdriver.Firefox(options=options)

try:
    # Change headers
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    driver.execute_script("window.navigator.chrome = {runtime: {}};")

    # Navigate to a page
    driver.get("https://example.com")
    
    # Example of accessing elements
    title = driver.title
    logger.info(f"Page title: {title}")

    # Perform actions, e.g., find an element
    element = driver.find_element(By.TAG_NAME, "h1")
    logger.info(f"Header text: {element.text}")

finally:
    driver.quit()  # Close the browser
