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

    total_counts_model = pd.read_csv(r'C:\Users\amank\OneDrive\Desktop\Car_Forcasting\results\Total_counts_pred.csv')
    make_model = pd.read_csv(r'C:\Users\amank\OneDrive\Desktop\Car_Forcasting\results\Make_pred.csv')
    vehi_models_model = pd.read_csv(r'C:\Users\amank\OneDrive\Desktop\Car_Forcasting\results\Model_pred.csv')
    vehi_loc = pd.read_csv(r'C:\Users\amank\OneDrive\Desktop\Car_Forcasting\data\processed_data\vehi_loc.csv')
    site_data = pd.read_csv(r'C:\Users\amank\OneDrive\Desktop\Car_Forcasting\data\processed_data\site_data.csv')

    total_counts_model.to_sql('total_counts_model', con=engine, if_exists='replace', index=False)
    make_model.to_sql('make_model', con=engine, if_exists='replace', index=False)
    vehi_models_model.to_sql('vehi_models_model', con=engine, if_exists='replace', index=False)
    vehi_loc.to_sql('vehi_loc', con=engine, if_exists='replace', index=False)
    site_data.to_sql('site_data', con=engine, if_exists='replace', index=False)



    # Close the MySQL connection
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed.")
