import tkinter as tk
from tkinter import filedialog, messagebox
from ExcelManager import ExcelManager
from MessageBuilder import MessageBuilder
from MessageRandomizer import MessageRandomizer
from BulkMessageController import BulkMessageController
from DBmanager import DBManager
from openpyxl import Workbook


class BulkMessageGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Bulk Message Page")
        self.root.geometry("1150x700")
        self.root.resizable(False, False)

        self.excel_file_path = None
        self.attachment_path = None

        self.create_widgets()
        self.excel_manager = ExcelManager()
        self.message_builder = MessageBuilder()
        self.message_randomizer = MessageRandomizer()
        self.db_manager = DBManager()
        self.controller = BulkMessageController(
            self.excel_manager,
            self.message_builder,
            self.message_randomizer,
            self.db_manager
        )
        self.contacts = []

    def create_widgets(self):
        title_label = tk.Label(
            self.root,
            text="Bulk Message Page",
            font=("Arial", 22, "bold")
        )
        title_label.pack(pady=18)

        main_frame = tk.Frame(self.root)
        main_frame.pack(fill="both", expand=True, padx=25, pady=10)

        left_frame = tk.LabelFrame(main_frame, text="Excel Contacts", padx=12, pady=12)
        left_frame.place(x=10, y=10, width=300, height=550)

        upload_button = tk.Button(
            left_frame,
            text="Upload Excel",
            width=28,
            command=self.upload_excel
        )
        upload_button.pack(pady=6)

        sample_button = tk.Button(
            left_frame,
            text="Download Sample",
            width=28,
            command=self.download_sample
        )
        sample_button.pack(pady=6)

        self.excel_status_label = tk.Label(
            left_frame,
            text="No Excel file selected",
            fg="gray"
        )
        self.excel_status_label.pack(pady=12)

        self.contact_listbox = tk.Listbox(left_frame, width=38, height=26)
        self.contact_listbox.pack(pady=8)

        center_frame = tk.LabelFrame(main_frame, text="Message", padx=12, pady=12)
        center_frame.place(x=335, y=10, width=500, height=550)

        message_label = tk.Label(center_frame, text="Type your message:")
        message_label.pack(anchor="w")

        self.message_text = tk.Text(center_frame, width=58, height=19)
        self.message_text.pack(pady=8)

        variable_hint = tk.Label(
            center_frame,
            text="Example: Hello {{Name}}, this is a test message.",
            fg="gray"
        )
        variable_hint.pack(anchor="w", pady=(2, 8))

        attachment_button = tk.Button(
            center_frame,
            text="Add Attachment",
            width=28,
            command=self.add_attachment
        )
        attachment_button.pack(pady=8)

        self.attachment_label = tk.Label(
            center_frame,
            text="No attachment selected",
            fg="gray"
        )
        self.attachment_label.pack(pady=(0, 12))

        self.randomise_var = tk.BooleanVar()
        random_checkbox = tk.Checkbutton(
            center_frame,
            text="Enable message randomisation",
            variable=self.randomise_var
        )
        random_checkbox.pack(anchor="w", pady=8)

        right_frame = tk.LabelFrame(main_frame, text="Delay & Campaign", padx=12, pady=12)
        right_frame.place(x=860, y=10, width=250, height=550)

        min_delay_label = tk.Label(right_frame, text="Min Delay (seconds):")
        min_delay_label.pack(anchor="w", pady=(8, 0))

        self.min_delay_entry = tk.Entry(right_frame, width=24)
        self.min_delay_entry.insert(0, "5")
        self.min_delay_entry.pack(pady=6)

        max_delay_label = tk.Label(right_frame, text="Max Delay (seconds):")
        max_delay_label.pack(anchor="w", pady=(14, 0))

        self.max_delay_entry = tk.Entry(right_frame, width=24)
        self.max_delay_entry.insert(0, "10")
        self.max_delay_entry.pack(pady=6)

        start_button = tk.Button(
            right_frame,
            text="Start Campaign",
            width=24,
            height=2,
            bg="#28a745",
            fg="white",
            command=self.start_campaign
        )
        start_button.pack(pady=(30, 12))

        clear_button = tk.Button(
            right_frame,
            text="Clear",
            width=24,
            bg="#dc3545",
            fg="white",
            command=self.clear_form
        )
        clear_button.pack(pady=8)

        status_frame = tk.LabelFrame(right_frame, text="Status", padx=10, pady=10)
        status_frame.pack(pady=35, fill="x")

        self.status_label = tk.Label(
            status_frame,
            text="Ready",
            fg="green",
            wraplength=190
        )
        self.status_label.pack(pady=10)

    def upload_excel(self):
        file_path = filedialog.askopenfilename(
            title="Select Excel File",
            filetypes=[("Excel files", "*.xlsx")]
        )

        if file_path:
            try:
                self.contacts = self.excel_manager.read_contacts(file_path)
                self.excel_file_path = file_path

                self.excel_status_label.config(
                    text=f"{len(self.contacts)} contacts loaded",
                    fg="green"
            )

                self.contact_listbox.delete(0, tk.END)

                for contact in self.contacts:
                    self.contact_listbox.insert(
                        tk.END,
                        f"{contact['name']} - {contact['phone_number']}"
                    )

                self.status_label.config(
                    text="Excel file loaded successfully.",
                    fg="green"
                )

            except Exception as e:
                messagebox.showerror("Excel Error", str(e))
                self.status_label.config(
                    text="Excel upload failed.",
                    fg="red"
            )

    def download_sample(self):
        file_path = filedialog.asksaveasfilename(
            title="Save Sample Excel",
            defaultextension=".xlsx",
            filetypes=[("Excel files", "*.xlsx")],
            initialfile="sample_contacts.xlsx"
        )

        if not file_path:
           return

        workbook = Workbook()
        sheet = workbook.active
        sheet.title = "Contacts"

        sheet["A1"] = "Name"
        sheet["B1"] = "Phone Number"
        sheet["C1"] = "Company"
        sheet["D1"] = "City"

        sheet["A2"] = "John"
        sheet["B2"] = "+905551111111"
        sheet["C2"] = "Example Company"
        sheet["D2"] = "Istanbul"

        workbook.save(file_path)

        messagebox.showinfo("Success", "Sample Excel file created successfully.")
        self.status_label.config(
            text="Sample Excel file created successfully.",
            fg="green"
        )

    def add_attachment(self):
        file_path = filedialog.askopenfilename(
            title="Select Attachment"
        )

        if file_path:
            self.attachment_path = file_path
            self.attachment_label.config(text="Attachment selected", fg="green")
            self.status_label.config(text="Attachment added successfully.", fg="green")

    def start_campaign(self):
        message = self.message_text.get("1.0", tk.END).strip()
        min_delay = self.min_delay_entry.get().strip()
        max_delay = self.max_delay_entry.get().strip()

        if not self.excel_file_path:
            messagebox.showerror("Error", "Please upload an Excel file first.")
            return

        if not message:
            messagebox.showerror("Error", "Please enter a message.")
            return

        if not min_delay.isdigit() or not max_delay.isdigit():
            messagebox.showerror("Error", "Delay values must be numbers.")
            return

        if int(min_delay) > int(max_delay):
            messagebox.showerror("Error", "Min delay cannot be greater than max delay.")
            return

        final_message = self.controller.create_preview(
             self.contacts,
             message,
             self.randomise_var.get()
        )

        messagebox.showinfo(
             "Message Preview",
             final_message
        )

        saved_count = self.controller.save_campaign(
           self.contacts,
           message,
           self.randomise_var.get(),
           self.attachment_path,
           min_delay,
           max_delay
        )

        messagebox.showinfo(
           "Success",
           f"{saved_count} messages saved successfully."
        )

        self.status_label.config(
            text=f"{saved_count} messages saved successfully.",
            fg="green"
        )

    def clear_form(self):
        self.excel_file_path = None
        self.attachment_path = None

        self.message_text.delete("1.0", tk.END)

        self.min_delay_entry.delete(0, tk.END)
        self.min_delay_entry.insert(0, "5")

        self.max_delay_entry.delete(0, tk.END)
        self.max_delay_entry.insert(0, "10")

        self.contact_listbox.delete(0, tk.END)

        self.excel_status_label.config(text="No Excel file selected", fg="gray")
        self.attachment_label.config(text="No attachment selected", fg="gray")
        self.randomise_var.set(False)
        self.status_label.config(text="Ready", fg="green")

    def run(self):
        self.root.mainloop()