import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

class DatabaseManager:

    # Loads database credentials from .env and establishes connection
    def __init__(self):
        self.connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )

    # Fetches the activation key record from the database, returns None if not found
    def get_activation_key(self, activation_key):
        cursor = self.connection.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM activation_keys WHERE activation_key = %s",
            (activation_key,)
        )

        result = cursor.fetchone()

        cursor.close()

        return result