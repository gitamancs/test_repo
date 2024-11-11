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
    database = 'clean_data_car'
    
    engine = create_engine(f'mysql+mysqlconnector://{username}:{password}@{host}/{database}')

    sales_sata = pd.read_csv(r'C:\Users\amank\OneDrive\Desktop\Car_Forcasting\data\processed_data\sales_data_clean.csv')
    stock_sata = pd.read_csv(r'C:\Users\amank\OneDrive\Desktop\Car_Forcasting\data\processed_data\stock_data_clean.csv')


    sales_sata.to_sql('sales_data', con=engine, if_exists='replace', index=False)
    stock_sata.to_sql('stock_data', con=engine, if_exists='replace', index=False)



    # Close the MySQL connection
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed.")
