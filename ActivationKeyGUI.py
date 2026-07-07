import tkinter as tk
from tkinter import messagebox
from MachineManager import MachineManager
from LicenseManager import LicenseManager


machine = MachineManager()
license_manager = LicenseManager()
machine_id = machine.generate_machine_id()

# Validates the entered key and updates the UI based on the result
def activate_key():
    key = key_entry.get().strip()

    if key == "":
        messagebox.showwarning("Missing Key", "Please enter an activation key.")
        return

    if license_manager.validate_key(key, machine_id):
        status_value.config(text="Activation Successful", fg="green")
        days_value.config(text=f"Days Left: {license_manager.get_days_left()}")
        license_value.config(text=f"Status: {license_manager.get_status()}")
    else:
        status_value.config(text="Invalid Activation Key", fg="red")
        days_value.config(text="")
        license_value.config(text="")

# Copies the machine ID to clipboard
def copy_machine_id():
    window.clipboard_clear()
    window.clipboard_append(machine_id)
    messagebox.showinfo("Copied", "Machine ID copied to clipboard.")


window = tk.Tk()
window.title("WA Sender 2.0 - Activation")
window.geometry("560x360")
window.resizable(False, False)

title_label = tk.Label(
    window,
    text="WA Sender 2.0",
    font=("Arial", 20, "bold")
)
title_label.pack(pady=(20, 5))

subtitle_label = tk.Label(
    window,
    text="Activation Key Page",
    font=("Arial", 12)
)
subtitle_label.pack(pady=(0, 20))

machine_label = tk.Label(
    window,
    text="Machine ID",
    font=("Arial", 10, "bold")
)
machine_label.pack()

machine_frame = tk.Frame(window)
machine_frame.pack(pady=5)

machine_value = tk.Entry(machine_frame, width=55)
machine_value.insert(0, machine_id)
machine_value.config(state="readonly")
machine_value.pack(side="left", padx=(0, 5))

copy_button = tk.Button(
    machine_frame,
    text="Copy",
    command=copy_machine_id
)
copy_button.pack(side="left")

key_label = tk.Label(
    window,
    text="Activation Key",
    font=("Arial", 10, "bold")
)
key_label.pack(pady=(20, 5))

key_entry = tk.Entry(window, width=50)
key_entry.pack()

activate_button = tk.Button(
    window,
    text="Activate",
    width=20,
    command=activate_key
)
activate_button.pack(pady=15)

status_value = tk.Label(window, text="", font=("Arial", 10, "bold"))
status_value.pack()

days_value = tk.Label(window, text="", font=("Arial", 10))
days_value.pack(pady=3)

license_value = tk.Label(window, text="", font=("Arial", 10))
license_value.pack()

window.mainloop()