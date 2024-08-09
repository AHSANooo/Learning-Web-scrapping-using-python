import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

# Get user input
website_name = input("Enter the name of the website (e.g., arxiv.org): ")
search_term = input("Enter the word to search: ")

# Construct search URL
search_urls = {
    "arxiv.org": f"https://arxiv.org/search/?query={search_term}&searchtype=all&source=header",
    # Add more websites with known structures here
}

# Check if the website is supported
if website_name in search_urls:
    url = search_urls[website_name]
else:
    raise ValueError("Website not supported. Please enter 'arxiv.org'.")

# Set up WebDriver
driver = webdriver.Chrome()
driver.get(url)

# Wait for the page to load
time.sleep(5)

# Parse the page source with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Container and field classes (adjust according to the website)
container_class = "arxiv-result"
field_classes = ["title", "authors", "abstract"]

# Find all containers
containers = soup.find_all(class_=container_class)

# Extract data
data = []
for container in containers:
    row = {}
    for field_class in field_classes:
        field_data = container.find(class_=field_class).get_text(strip=True)
        row[field_class] = field_data
    data.append(row)

# Close the WebDriver
driver.quit()

# Save data to CSV using Pandas
df = pd.DataFrame(data)
output_file = f'{website_name}_search_results.csv'
df.to_csv(output_file, index=False)

print(f"Data has been saved to {output_file}")
