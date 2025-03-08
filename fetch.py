import requests
import logging
from time import sleep

API_URL = "https://api.slingacademy.com/v1/sample-data/files/employees.json"
MAX_RETRIES = 3
TIMEOUT = 20  # Increase timeout to avoid timeouts

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def fetch_employee_data():
    retries = 0
    while retries < MAX_RETRIES:
        try:
            logging.info(f"Fetching data from {API_URL} (Attempt {retries + 1}/{MAX_RETRIES})...")
            response = requests.get(API_URL, timeout=TIMEOUT)
            
            if response.status_code == 200:
                logging.info("Successfully retrieved data!")
                
                # Print the raw response for debugging (first 500 characters)
                logging.info(f"Raw API Response: {response.text[:500]}")
                
                data = response.json()

                if isinstance(data, list): 
                    return data
                else:
                    logging.error("Unexpected API response format. Expected a list of employees.")
                    return None
            
            else:
                logging.warning(f"Failed attempt {retries + 1}: {response.status_code} - {response.text}")
        
        except requests.exceptions.Timeout:
            logging.warning(f"Attempt {retries + 1}: Request timed out. Retrying in 5 seconds...")
            sleep(5)
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching data: {e}")
            return None

        retries += 1

    logging.error("Max retries reached. API is not responding.")
    return None