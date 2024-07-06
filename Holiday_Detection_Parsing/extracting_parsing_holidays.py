from tabulate import tabulate
import requests
import logging
from bs4 import BeautifulSoup

def fetch_url_content(url):
    try:
        print("Started fetching public holidays content from the given url")
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        logging.error("An error occurred: %s", e)
        raise
def parse_holidays(page_content):
    try:
        print("Started parsing the HTML content")
        soup = BeautifulSoup(page_content, 'html.parser')

        div_content = soup.find('div', {'class': 'field field-name-body'})
        if div_content is None:
            logging.warning("Missing div element in class field field-name-body")
            return []
        table = div_content.find('table')
        if table is None:
            logging.warning("Could not able to find table within div")
            return []

        print("Now processing the table content and fetching the required data")
        holidays = []
        if table:
            # extracting table header to fetch year
            header_row = table.find('thead').find('tr')
            if header_row is None:
                logging.warning("Could not find table header row")
                return []
            headers = header_row.find_all('th')
            years = [int(header.get_text(strip=True)) for header in headers if header.get_text(strip=True).isdigit()]

            valid_years = [2024, 2025]  #only care about 2024 and 2025
            year_indices = [i for i, year in enumerate(years) if year in valid_years]

            tbody = table.find('tbody')
            if tbody is None:
                logging.warning("Could not find table body")
                return []

        # Iterate over table rows
            for row in tbody.find_all('tr'):
                holiday_name = row.find('th').get_text(strip=True)
                columns = row.find_all('td')

                for i in year_indices:
                    if i < len(columns):
                        holiday_date = columns[i].get_text(strip=True)
                        holidays.append({'Year': years[i], 'Holiday Date': holiday_date, 'Holiday Name': holiday_name})

        print("Showing fetched holidays:\n",holidays)
        if holidays:
            headers = ["Year","Holiday Date","Holiday Name"]
            table_data = [[h['Year'],h['Holiday Date'],h['Holiday Name']]for h in holidays]
            print("\nPrinting Holidays in Pretty Format:")
            print(tabulate(table_data,headers= headers,tablefmt = "pretty"))
        else:
            print("No holidays found")
        return holidays
    except Exception as e:
        logging.error("Error parsing holidays: %s", e)
        return []


