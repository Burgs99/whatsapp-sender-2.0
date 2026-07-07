import mysql.connector
import json
import os
from dotenv import load_dotenv


class DBManager:
    def __init__(self):
        load_dotenv()

        self.connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )

    def save_bulk_message(self, contact_name, phone_number, variable_data,
                          message_text, attachment, min_delay, max_delay):
        cursor = self.connection.cursor()

        query = """
        INSERT INTO bulk_messages
        (contact_name, phone_number, variable_data, message_text, attachment,
         min_delay, max_delay, send_status)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        values = (
            contact_name,
            phone_number,
            json.dumps(variable_data),
            message_text,
            attachment,
            min_delay,
            max_delay,
            "Pending"
        )

        cursor.execute(query, values)
        self.connection.commit()
        cursor.close()

    def close_connection(self):
        if self.connection.is_connected():
            self.connection.close()