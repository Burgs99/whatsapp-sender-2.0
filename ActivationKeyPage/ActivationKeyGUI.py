import tkinter as tk
from tkinter import messagebox
from MachineManager import MachineManager
from LicenseManager import LicenseManager

# Set up MachineID and License managers for this page
machine = MachineManager()
license_manager = LicenseManager()
machine_id = machine.generate_machine_id() #Gets this PC's permanant Machine ID

# Validates the entered key and updates the UI based on the result
#DEPLOYMENT PLAN: this function implements the TC-002 and TC-003
def activate_key():
    key = key_entry.get().strip()

    if key == "": #Stops early if nothing was typed in
        messagebox.showwarning("Missing Key", "Please enter an activation key.")
        return

    if license_manager.validate_key(key, machine_id):
        #Showes success + license details (TC-002)
        status_value.config(text="Activation Successful", fg="green")
        days_value.config(text=f"Days Left: {license_manager.get_days_left()}")
        license_value.config(text=f"Status: {license_manager.get_status()}")
    else:
        #Show error and clear old information (TC-003)
        status_value.config(text="Invalid Activation Key", fg="red")
        days_value.config(text="")
        license_value.config(text="")

# Copies the machine ID to clipboard
def copy_machine_id():
    window.clipboard_clear()
    window.clipboard_append(machine_id)
    messagebox.showinfo("Copied", "Machine ID copied to clipboard.")

# This creates the actual window
window = tk.Tk()
window.title("WA Sender 2.0 - Activation")
window.geometry("560x360")
window.resizable(False, False)

#Page title
title_label = tk.Label(
    window,
    text="WA Sender 2.0",
    font=("Arial", 20, "bold")
)
title_label.pack(pady=(20, 5))

#Page subtitle
subtitle_label = tk.Label(
    window,
    text="Activation Key Page",
    font=("Arial", 12)
)
subtitle_label.pack(pady=(0, 20))

#Machine ID Label
#Displays the generated system ID
machine_label = tk.Label(
    window,
    text="Machine ID",
    font=("Arial", 10, "bold")
)
machine_label.pack()

machine_frame = tk.Frame(window) #Holds the machine ID box and the copy button side by side
machine_frame.pack(pady=5)

#Machine ID box ( Pre-filled, read only so it cannot be edited by mistake)
machine_value = tk.Entry(machine_frame, width=55)
machine_value.insert(0, machine_id)
machine_value.config(state="readonly")
machine_value.pack(side="left", padx=(0, 5))

#This copy button runs 'copy_machine_id() above
copy_button = tk.Button(
    machine_frame,
    text="Copy",
    command=copy_machine_id
)
copy_button.pack(side="left")

#This input is the 'insert Activation key' requirement
key_label = tk.Label(
    window,
    text="Activation Key",
    font=("Arial", 10, "bold")
)
key_label.pack(pady=(20, 5))

#Activation Key input box
key_entry = tk.Entry(window, width=50)
key_entry.pack()

#Activates button runs 'activate_Key() above
activate_button = tk.Button(
    window,
    text="Activate",
    width=20,
    command=activate_key
)
activate_button.pack(pady=15)

#Shows either 'Successful' or 'Invalid Activation Key'
status_value = tk.Label(window, text="", font=("Arial", 10, "bold"))
status_value.pack()

#Shows how many days are left on the License
days_value = tk.Label(window, text="", font=("Arial", 10))
days_value.pack(pady=3)

#Shows the license status as either Active or Expired
license_value = tk.Label(window, text="", font=("Arial", 10))
license_value.pack()

window.mainloop() # Keeps the window open and responsive to clicks
