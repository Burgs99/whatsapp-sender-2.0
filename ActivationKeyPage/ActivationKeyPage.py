from MachineManager import MachineManager
from LicenseManager import LicenseManager

machine = MachineManager()
license_manager = LicenseManager()

machine_id = machine.generate_machine_id()

print("Machine ID:", machine_id)

if license_manager.has_saved_key():

    key = license_manager.get_saved_key()

    if license_manager.validate_key(key, machine_id):
        print("Already Activated")
        print("Days Left:", license_manager.get_days_left())
        print("Status:", license_manager.get_status())

    else:
        print("Saved activation key is invalid. Please enter a new key.")

        key = input("Enter Activation Key: ")

        if license_manager.validate_key(key, machine_id):
            print("Activation Successful")
            print("Days Left:", license_manager.get_days_left())
            print("Status:", license_manager.get_status())
        else:
            print("Invalid Activation Key")

else:

    key = input("Enter Activation Key: ")

    if license_manager.validate_key(key, machine_id):
        print("Activation Successful")
        print("Days Left:", license_manager.get_days_left())
        print("Status:", license_manager.get_status())

    else:
        print("Invalid Activation Key")
