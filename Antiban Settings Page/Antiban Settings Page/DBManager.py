import os
import mysql.connector
from dotenv import load_dotenv


load_dotenv()


class DBManager:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )

    def save_antiban_settings(self, settings):
        cursor = self.connection.cursor()

        query = """
        INSERT INTO antiban_settings (
            safety_profile,
            min_delay,
            max_delay,
            random_delay,
            max_messages_per_hour,
            max_messages_per_day,
            auto_pause,
            typing_simulation,
            simulate_reading,
            business_hours_only,
            skip_recent_contacts,
            risk_level
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        values = (
            settings["safety_profile"],
            settings["min_delay"],
            settings["max_delay"],
            settings["random_delay"],
            settings["max_messages_per_hour"],
            settings["max_messages_per_day"],
            settings["auto_pause"],
            settings["typing_simulation"],
            settings["simulate_reading"],
            settings["business_hours_only"],
            settings["skip_recent_contacts"],
            settings["risk_level"]
        )

        cursor.execute(query, values)
        self.connection.commit()
        cursor.close()

    def get_latest_antiban_settings(self):
        cursor = self.connection.cursor(dictionary=True)

        query = """
        SELECT *
        FROM antiban_settings
        ORDER BY id DESC
        LIMIT 1
        """

        cursor.execute(query)
        result = cursor.fetchone()
        cursor.close()

        return result

    def close_connection(self):
        if self.connection.is_connected():
            self.connection.close()