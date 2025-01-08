from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class KVKExtractor:
    def __init__(self, driver):
        self.driver = driver

    def extract_kvk_data(self):
        try:
            # KVK number extraction
            print("Waiting for KVK number element...")
            kvk_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".mb-6:nth-child(1) .icon-fileCertificateIcon"))
            )
            kvk_number = kvk_element.text.strip()
            print("KVK Number:", kvk_number)

            # Extract company name using the provided class
            print("Waiting for company name element...")
            company_name_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".TextLink-module_icon-first-word__GYcoh"))
            )
            company_name = company_name_element.text.strip()
            print("Company Name:", company_name)

            # Extract address using the provided selector
            print("Waiting for address element...")
            address_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".icon-locationLargeIcon"))
            )
            address = address_element.text.strip()
            print("Address:", address)

            # Extract trade name using the specified class
            print("Waiting for trade name element...")
            company_summary = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".mb-6:nth-child(1)"))
            )
            trade_name_element = company_summary.find_element(By.CSS_SELECTOR, ".mt-2")
            trade_name = trade_name_element.text.strip()
            print("Trade Name:", trade_name)

        except Exception as e:
            print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    url = "https://www.kvk.nl/zoeken"

    driver = webdriver.Chrome()
    driver.get(url)
    wait = WebDriverWait(driver, 10)

    # Accept cookies
    try:
        print("Waiting for cookies button...")
        cookies_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Keuze opslaan']")))
        cookies_button.click()
        print("Cookies accepted.")
    except Exception as e:
        print(f"Couldn't find the cookies button: {e}")

    try:
        # Wait and find the input field
        print("Waiting for input field...")
        input_tag = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".FlexboxItem__s-sc-wm1s05-0 > input")))
        input_tag.click()
        input_tag.send_keys("09034338")
        print("Entered search term.")

        # Wait and click the search button
        print("Waiting for search button...")
        search_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".Button-module_primary__fOb-0")))
        search_button.click()
        print("Search button clicked.")

        # Initialize KVKExtractor and extract data
        extractor = KVKExtractor(driver)
        extractor.extract_kvk_data()

    except Exception as e:
        print("An error occurred during the search process:", e)

    finally:
        driver.quit()
        