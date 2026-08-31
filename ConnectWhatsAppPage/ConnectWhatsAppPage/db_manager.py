import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

# Handles connecting to the database for the Connect WhatsApp page
class DBManager:
    def __init__(self):
        self.config = {
            "host": os.getenv("DB_HOST"),
            "user": os.getenv("DB_USER"),
            "password": os.getenv("DB_PASSWORD"),
            "database": os.getenv("DB_NAME")
        }

    # Opens and returns a new database connection
    def get_connection(self):
        return mysql.connector.connect(**self.config)
