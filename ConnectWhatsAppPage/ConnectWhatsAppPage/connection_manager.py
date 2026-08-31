from db_manager import DBManager

# Handles saving and reading Whatsapp connection records in the database
class ConnectionManager:
    def __init__(self):
        self.db = DBManager()

    # Adds a new connection record to the database
    def save_connection(self, phone_number, connection_method, status):
        connection = self.db.get_connection()
        cursor = connection.cursor()

        query = """
            INSERT INTO whatsapp_connections 
            (phone_number, connection_method, status, is_active)
            VALUES (%s, %s, %s, %s)
        """

        values = (phone_number, connection_method, status, False)

        cursor.execute(query, values)
        connection.commit()

        cursor.close()
        connection.close()

    # Updates the status of one excisting connection by its ID
    def update_connection_status(self, connection_id, status):
        connection = self.db.get_connection()
        cursor = connection.cursor()

        query = """
            UPDATE whatsapp_connections
            SET status = %s
            WHERE id = %s
        """

        values = (status, connection_id)

        cursor.execute(query, values)
        connection.commit()

        cursor.close()
        connection.close()

    # Returns every saved connection record
    def get_all_connections(self):
        connection = self.db.get_connection()
        cursor = connection.cursor(dictionary=True)

        query = "SELECT * FROM whatsapp_connections"

        cursor.execute(query)
        results = cursor.fetchall()

        cursor.close()
        connection.close()

        return results

    # Updates the most recent QR Code connection's status
    def update_latest_qr_connection(self, status):
        connection = self.db.get_connection()
        cursor = connection.cursor()

        query = """
           UPDATE whatsapp_connections
           SET status = %s, is_active = %s
           WHERE connection_method = %s
           ORDER BY id DESC
           LIMIT 1
           """

        values = (status, True, "QR Code")

        cursor.execute(query, values)
        connection.commit()

        cursor.close()
        connection.close()
