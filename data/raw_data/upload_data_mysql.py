import pandas as pd
from sqlalchemy import create_engine
from mysql_connection import create_connection

# Create a connection to the MySQL database
connection = create_connection()

# Check if the connection was successful
if connection is None or not connection.is_connected():
    print("Failed to connect to the database. Exiting...")
else:
    print("Starting script...")

    # Define SQLAlchemy engine using the same connection parameters
    username = 'root'
    password = 'root'
    host = 'localhost'
    database = 'car_sales_forecast'
    
    engine = create_engine(f'mysql+mysqlconnector://{username}:{password}@{host}/{database}')

    # Load the Excel file
    excel_file = r'C:\Users\amank\OneDrive\Desktop\Car_Forcasting\data\raw_data\SampleSize.xlsx'
    xls = pd.ExcelFile(excel_file)

    # Iterate through each sheet and upload it to MySQL
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name)
        print(f"Uploading sheet: {sheet_name}")
        if df.empty:
            print(f"DataFrame for {sheet_name} is empty!")
        else:
            print(df.head())  # Show the first few rows of the DataFrame
            df.to_sql(sheet_name, con=engine, if_exists='replace', index=False)
            print(f'Table {sheet_name} uploaded successfully.')

    # Close the MySQL connection
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed.")
