import os
from datetime import datetime
from DatabaseManager import DatabaseManager

class LicenseManager:

    def __init__(self):
        self.key_file = "activation_key.txt"
        self.expiry_file = "expiry_date.txt"
        self.database = DatabaseManager()

    # Validates the key against the database and saves it locally if successful
    def validate_key(self, key, machine_id):

        record = self.database.get_activation_key(key)

        if record is None:
           return False
        
       # Make sure the key belongs to this machine
        if record["machine_id"] != machine_id:
           return False


        if record["status"] != "Active":
           return False

        expires_at = record["expires_at"]

        # Reject if the license has expired
        if expires_at < datetime.now():
           return False

        self.save_activation_key(key)
        self.save_expiry_date_from_database(expires_at)

        return True
    
    # Saves the activation key to a local file
    def save_activation_key(self, key):
        with open(self.key_file, "w") as file:
            file.write(key)

    def has_saved_key(self):
        return os.path.exists(self.key_file)

    # Reads and returns the saved activation key from file
    def get_saved_key(self):
        with open(self.key_file, "r") as file:
            return file.read()

    def has_saved_expiry_date(self):
        return os.path.exists(self.expiry_file)

    # Reads and returns the expiry date from local file
    def get_expiry_date(self):
        with open(self.expiry_file, "r") as file:
            expiry_text = file.read()

        return datetime.strptime(expiry_text, "%Y-%m-%d %H:%M:%S")

    # Returns True if the license has passed its expiry date
    def is_expired(self):
        expiry_date = self.get_expiry_date()

        return datetime.now() > expiry_date

    # Calculates and returns the number of days remaining
    def get_days_left(self):
        expiry_date = self.get_expiry_date()
        remaining_time = expiry_date - datetime.now()

        return remaining_time.days
    
    # Returns "Active" or "Expired" based on current date
    def get_status(self):
       if self.is_expired():
         return "Expired"

       return "Active"

    # Saves the expiry date received from the database to a local file
    def save_expiry_date_from_database(self, expires_at):
       with open(self.expiry_file, "w") as file:
         file.write(str(expires_at))