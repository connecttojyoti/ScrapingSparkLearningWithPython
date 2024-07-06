from Holiday_Detection_Parsing.extracting_parsing_holidays import *
from Holiday_Detection_Parsing.storing_output_to_db import *

URL = "https://www.commerce.wa.gov.au/labour-relations/public-holidays-western-australia"
def main():
    try:
        # Fetching page content
        page_content = fetch_url_content(URL)
        # Extracting and parsing holidays
        if page_content:
            holidays = parse_holidays(page_content)
        # Extracting and parsing holidays
            if holidays:
                conn,cursor = saving_holidays_to_db(holidays)
                with conn:
                    Displaying_data_from_db(cursor)
    except sqlite3.Error as e:
        logging.error("Database error occured in main.py %s",e)
    except Exception as e:
        logging.error("Error occured in main.py %s",e)
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    main()


