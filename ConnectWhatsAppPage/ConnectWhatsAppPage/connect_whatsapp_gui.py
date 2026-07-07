from whatsapp_web_manager import WhatsAppWebManager
import tkinter as tk
from tkinter import ttk, messagebox
from connection_manager import ConnectionManager


class ConnectWhatsAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Connect WhatsApp Page")
        self.root.geometry("420x380")

        self.manager = ConnectionManager()
        self.web_manager = WhatsAppWebManager()

        title_label = tk.Label(root, text="Connect WhatsApp", font=("Arial", 16, "bold"))
        title_label.pack(pady=15)

        self.phone_label = tk.Label(root, text="Phone Number:")
        self.phone_entry = tk.Entry(root, width=35)
        

        method_label = tk.Label(root, text="Connection Method:")
        method_label.pack()

        self.method_combo = ttk.Combobox(
            root,
            values=["QR Code", "Phone Number"],
            state="readonly",
            width=32
        )
        self.method_combo.current(0)
        self.method_combo.pack(pady=5)
        self.method_combo.bind("<<ComboboxSelected>>", self.update_method_view)

        status_label = tk.Label(root, text="Connection Status:")
        status_label.pack()

        self.status_combo = ttk.Combobox(
            root,
            values=["Pending", "Connected", "Disconnected"],
            state="readonly",
            width=32
        )
        self.status_combo.current(0)
        self.status_combo.pack(pady=5)

        open_browser_button = tk.Button(
        root,
        text="Open WhatsApp Web",
        command=self.open_whatsapp_web
        )
        open_browser_button.pack(pady=5)

        check_status_button = tk.Button(
        root,
        text="Check Login Status",
        command=self.check_login_status
        )
        check_status_button.pack(pady=5)


        save_button = tk.Button(root, text="Save Connection", command=self.save_connection)
        save_button.pack(pady=15)

        self.result_label = tk.Label(root, text="", fg="green")
        self.result_label.pack()
        self.update_method_view()

    def save_connection(self):
        phone_number = self.phone_entry.get()
        connection_method = self.method_combo.get()
        status = self.status_combo.get()

        if connection_method == "QR Code":
           status = "Pending"
           phone_number = "N/A"

        if connection_method == "Phone Number" and phone_number == "":
           messagebox.showerror("Error", "Phone number is required.")
           return

        if connection_method == "QR Code":
           phone_number = "N/A"

        self.manager.save_connection(phone_number, connection_method, status)
        self.result_label.config(text=f"Connection saved with status: {status}")

        self.phone_entry.delete(0, tk.END)

    def open_whatsapp_web(self):
        connection_method = self.method_combo.get()
        phone_number = self.phone_entry.get()

        if connection_method == "Phone Number":
           if phone_number == "":
              messagebox.showerror("Error", "Phone number is required for phone number linking.")
              return

           started = self.web_manager.open_phone_number_linking(phone_number)

           if started:
              self.result_label.config(text="Phone number linking started. Complete verification on WhatsApp.")
           else:
              self.result_label.config(text="Could not start phone number linking.")

        else:
            self.web_manager.open_whatsapp_web()
            self.result_label.config(text="WhatsApp Web opened for QR Code login.")

    def update_method_view(self, event=None):
        selected_method = self.method_combo.get()

        self.phone_label.pack_forget()
        self.phone_entry.pack_forget()

        if selected_method == "QR Code":
           self.status_combo.set("Pending")

        if selected_method == "Phone Number":
           self.phone_label.pack(after=self.method_combo, pady=(10, 0))
           self.phone_entry.pack(after=self.phone_label, pady=5)

    def check_login_status(self):
        connection_method = self.method_combo.get()
        phone_number = self.phone_entry.get()

        if self.web_manager.is_logged_in():
           if connection_method == "QR Code":
              phone_number = "N/A"

           if connection_method == "Phone Number" and phone_number == "":
              messagebox.showerror("Error", "Phone number is required.")
              return

           self.manager.save_connection(phone_number, connection_method, "Connected")

           self.status_combo.set("Connected")
           self.result_label.config(text="WhatsApp Web login successful. Status saved as Connected")
        else:
            self.result_label.config(text="WhatsApp Web is not connected yet.")