from MachineManager import MachineManager
from LicenseManager import LicenseManager

machine = MachineManager()
license_manager = LicenseManager()

machine_id = machine.generate_machine_id() # Gets the PC's permanant Machine ID

print("Machine ID:", machine_id)

# Checks if a key was already saved from a previous activiation
if license_manager.has_saved_key():

    key = license_manager.get_saved_key()

    if license_manager.validate_key(key, machine_id):
        #Saved key is still valid, no need to ask the user for it again
        print("Already Activated")
        print("Days Left:", license_manager.get_days_left())
        print("Status:", license_manager.get_status())

    else:
        #Saved key is expired or invalid, ask the user to enter a new one
        print("Saved activation key is invalid. Please enter a new key.")

        key = input("Enter Activation Key: ")

        if license_manager.validate_key(key, machine_id):
            print("Activation Successful")
            print("Days Left:", license_manager.get_days_left())
            print("Status:", license_manager.get_status())
        else:
            print("Invalid Activation Key")

else:
# No saved key at all, first time activating on this machine
    key = input("Enter Activation Key: ")

    if license_manager.validate_key(key, machine_id):
        print("Activation Successful")
        print("Days Left:", license_manager.get_days_left())
        print("Status:", license_manager.get_status())

    else:
        #Invalid Key statement
        print("Invalid Activation Key")
