import pandas as pd
from tabulate import tabulate
import sqlite3
import logging
import os
import sys

logging.getLogger().setLevel(logging.INFO)

db_dir = os.path.join(os.getcwd(), 'data')  # Create a 'data' directory in current working directory
db_file = 'holiday.db'
db_path = os.path.join(db_dir, db_file)
os.makedirs(db_dir, exist_ok=True)

def saving_holidays_to_db(ls):
    try:
        print("Started saving the data in sqllite in memory database storage")
        conn = sqlite3.connect(db_path)
        df = pd.DataFrame(ls)
        df.to_sql('Holidays_Information',conn,index= False,if_exists='replace')
        print("Data stored in database table Holidays_Information")
        return conn , conn.cursor()
    except sqlite3.Error as e:
        if conn:
            conn.close()
        logging.error("Error while saving the data to database: %s",e)
        raise

def Displaying_data_from_db(cursor):
    try:
        print("Started fetching data from database")
        cursor.execute('SELECT * FROM Holidays_Information')
        records = cursor.fetchall()
        columns = [description[0] for description in cursor.description]
        print("Printing the fetched data in Pretty format")
        print(tabulate(records,columns,tablefmt='grid'))
    except sqlite3.Error as e:
        logging.error("Error while showing data from database: %s", e)
        raise


