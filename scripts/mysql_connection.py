import mysql.connector
from mysql.connector import Error
from sqlalchemy import create_engine
import yaml

def load_config():
    # Load configuration from config.yaml
    with open(r"C:\Users\amank\OneDrive\Desktop\Car_Forcasting\config\config.yaml", "r") as file:
        config = yaml.safe_load(file)
    return config

def create_connection(database_name):
    config = load_config()
    db_config = config["database"]
    
    # Extract database credentials from config file
    username = db_config["username"]
    password = db_config["password"]
    host = db_config["host"]
    port = db_config.get("port", 3306)  # default to 3306 if port is not in config

    # Establish MySQL connection
    connection = None
    try:
        connection = mysql.connector.connect(
            user=username,
            password=password,
            host=host,
            database=database_name,
            port=port
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    # Create SQLAlchemy engine
    engine = create_engine(f'mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database_name}')

    return engine, connection
