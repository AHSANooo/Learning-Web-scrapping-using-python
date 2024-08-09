# Web Scraping with Python, Selenium, and BeautifulSoup

This project demonstrates how to scrape data from multiple pages of a website using Python, Selenium, and BeautifulSoup. The script is designed to handle pagination automatically, allowing you to extract data from all available pages and save it into a CSV file.

## Features

- **Dynamic Search**: Input the name of the website and the search term to generate search URLs dynamically.
- **Pagination Handling**: Automatically navigates through all available pages to scrape data.
- **Data Extraction**: Uses BeautifulSoup to extract relevant fields from the webpage.
- **CSV Export**: Saves the scraped data into a structured CSV file for easy analysis.

## Requirements

- Python
- Selenium
- BeautifulSoup4
- Pandas
- WebDriver (e.g., ChromeDriver or GeckoDriver for Firefox)

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/AHSANooo/Learning-Web-scrapping-using-python.git
    cd Learning-Web-scrapping-using-python
    ```

2. Download the appropriate WebDriver for your browser:
    - [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/)
    - [GeckoDriver for Firefox](https://github.com/mozilla/geckodriver/releases)

3. Make sure the WebDriver is in your system's PATH or specify the path in the script.

## Usage

1. Run the script:
    ```bash
    python main.py
    ```

2. Enter the name of the website (e.g., `arxiv.org`).

3. Enter the word or phrase you want to search.

4. The script will navigate through the search results pages, scrape the data, and save it in a CSV file named `<website_name>_search_results.csv`.

## Example

If you enter:
- Website: `arxiv.org`
- Search Term: `machine learning`

The script will scrape all search results related to "machine learning" from arxiv.org, including all pages of results, and save the data into a file named `arxiv.org_search_results.csv`.

## Code Overview

- **main.py**: The main script that handles user input, constructs search URLs, manages pagination, and extracts data.
- **requirements.txt**: Lists all Python packages required to run the script.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue if you have any suggestions or improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Support

If you have any questions or run into issues, feel free to [open an issue](https://github.com/your-username/web-scraping-multiple-pages/issues) or reach out via email.

## Resources

- [Selenium Documentation](https://www.selenium.dev/documentation/)
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/)

## Video Demo


Happy Scraping!
