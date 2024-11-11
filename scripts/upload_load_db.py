import pandas as pd
from mysql_connection import create_connection


def load_data_sql(database_name, table_name):

    engine, connection = create_connection(database_name)

    # Load data from the MySQL database tables into DataFrames
    loaded_data = pd.read_sql(table_name, con=engine)


    # Close the connection
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed.")

    return loaded_data


def upload_data_sql(df, table_name, database_name):

    engine, connection = create_connection(database_name)

    # Load data from the MySQL database tables into DataFrames
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)

    # Close the connection
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed.")

    return connection
