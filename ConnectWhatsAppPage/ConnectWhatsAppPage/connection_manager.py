from db_manager import DBManager


class ConnectionManager:
    def __init__(self):
        self.db = DBManager()

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

    def get_all_connections(self):
        connection = self.db.get_connection()
        cursor = connection.cursor(dictionary=True)

        query = "SELECT * FROM whatsapp_connections"

        cursor.execute(query)
        results = cursor.fetchall()

        cursor.close()
        connection.close()

        return results

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