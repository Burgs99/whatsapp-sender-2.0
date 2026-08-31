
import tkinter as tk
from tkinter import messagebox
 
from MachineManager import MachineManager
from LicenseManager import LicenseManager
 
machine_manager = MachineManager()
license_manager = LicenseManager()
 
root = tk.Tk()
root.title("WhatsApp Sender 2.0")
root.geometry("500x400")
 
title = tk.Label(
    root,
    text="WhatsApp Sender 2.0",
    font=("Arial", 18, "bold")
)
title.pack(pady=20)
 
tk.Label(root, text="Username").pack()
username_entry = tk.Entry(root, width=40)
username_entry.pack(pady=10)
 
tk.Label(root, text="Machine ID").pack() #generate system ID
machine_id_entry = tk.Entry(root, width=40)
machine_id_entry.pack(pady=10)
 
#Gets the Machine ID
machine_id = machine_manager.generate_machine_id()
machine_id_entry.insert(0, machine_id)
machine_id_entry.config(state="readonly")  # shown, but not editable by the user
 
tk.Label(root, text="Activation Key").pack()
activation_entry = tk.Entry(root, width=40)
activation_entry.pack(pady=10)
 
# Shows a small status message, e.g. when a saved activation is found.
status_label = tk.Label(root, text="", fg="green")
status_label.pack(pady=5)
 
 
def activate():
    username = username_entry.get().strip()
    machine = machine_id_entry.get().strip()
    key = activation_entry.get().strip()
 
    if not username:
        messagebox.showerror("Error", "Please enter a username.")
        return
    if not key:
        messagebox.showerror("Error", "Please enter an activation key.")
        return
 
    # looks the key up in the actual database, confirms
    # it belongs to this machine, is Active, and hasn't expired.
    is_valid = license_manager.validate_key(key, machine)
 
    if is_valid:
        messagebox.showinfo("Success", "Activation Successful")
        # this is where the rest of the app should open once activation succeeds 
    else:
        messagebox.showerror("Error", "Invalid or expired activation key.")
 
 # Runs once when the app opens
#It auto-fills the key if activated before
def check_existing_activation():
    
    if license_manager.has_saved_key() and license_manager.has_saved_expiry_date():
        if not license_manager.is_expired():
            saved_key = license_manager.get_saved_key()
            activation_entry.insert(0, saved_key)
            days_left = license_manager.get_days_left()
            status_label.config(
                text=f"Welcome back - already activated ({days_left} days left)"
            )
 
 
activate_btn = tk.Button(
    root,
    text="Activate",
    command=activate
)
activate_btn.pack(pady=20)
 
# Check for an existing activation right away, before the user does anything.
check_existing_activation()
 
root.mainloop()
