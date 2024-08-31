#this get coin names, can also be configured to get stock data tickers and names
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import csv
import time

# Set up Selenium WebDriver
driver = webdriver.Chrome()  # Make sure you have ChromeDriver installed

# URL of the CoinGecko page
url = "https://www.coingecko.com/en/all-cryptocurrencies"

# Open the page with Selenium
driver.get(url)

# Initialize list to store coin names
coin_names = []

# Function to extract coin names from the current page
def extract_coin_names():
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    rows = soup.select('table tbody tr')
    for row in rows:
        coin_name = row.select_one('td a div div').text.strip()
        coin_names.append(coin_name)

# Extract coin names from the first page
extract_coin_names()

# Loop to click "Show More" until all items are loaded
while True:
    try:
        # Wait for the "Show More" button to be clickable and then click it
        show_more_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/main/div/div[4]/button/div'))  # Use the XPath provided
        )
        show_more_button.click()
        
        # Wait for the page to load
        time.sleep(3)  # Adjust the sleep time as needed
        
        # Extract coin names from the new page
        extract_coin_names()
    except Exception as e:
        # If there's an exception (e.g., no more "Show More" button, bit this button name may change so check it if #errors arise,), break the loop
        print("No more pages or an error occurred:", e)
        break

# Save coin names to a CSV file
csv_file_path = 'crypto_names.csv'
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Coin Name'])  # Write header
    for name in coin_names:
        writer.writerow([name])  # Write each coin name

print(f"Coin names have been saved to {csv_file_path}")

# Close the browser
driver.quit()