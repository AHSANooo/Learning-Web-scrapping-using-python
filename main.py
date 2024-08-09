import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

website_name = input("Enter the name of the website (e.g., arxiv.org): ")
search_term = input("Enter the word to search: ")

search_urls = {
    "arxiv.org": f"https://arxiv.org/search/?query={search_term}&searchtype=all&source=header",

}
if website_name in search_urls:
    url = search_urls[website_name]
else:
    raise ValueError("Website not supported. Please enter 'arxiv.org'.")

driver = webdriver.Firefox()
driver.get(url)

time.sleep(5)

data = []

while True:
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    container_class = "arxiv-result"
    field_classes = ["title", "authors", "abstract"]

    containers = soup.find_all(class_=container_class)

    for container in containers:
        row = {}
        for field_class in field_classes:
            field_data = container.find(class_=field_class).get_text(strip=True)
            row[field_class] = field_data
        data.append(row)

    try:
        next_button = driver.find_element(By.LINK_TEXT, 'Next')
        next_button.click()
    except:

        print("No more pages found. Ending scrape.")
        break

driver.quit()

df = pd.DataFrame(data)
output_file = f'{website_name}_search_results.csv'
df.to_csv(output_file, index=False)

print(f"Data has been saved to {output_file}")
