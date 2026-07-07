import uuid
import os

class MachineManager:
    
    # Returns existing machine ID from file, or generates and saves a new one
    def generate_machine_id(self):
        file_name = "machine_id.txt"

        if os.path.exists(file_name):
            with open(file_name, "r") as file:
                return file.read()

        machine_id = str(uuid.uuid4())

        with open(file_name, "w") as file:
            file.write(machine_id)

        return machine_id