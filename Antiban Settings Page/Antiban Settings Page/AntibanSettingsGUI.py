import tkinter as tk
from tkinter import ttk


class AntibanSettingsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Antiban Settings Page")
        self.root.geometry("620x650")
        self.root.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(
            self.root,
            text="Anti-Ban Settings",
            font=("Arial", 20, "bold")
        )
        title_label.pack(pady=15)

        description_label = tk.Label(
            self.root,
            text="Configure safety settings to reduce WhatsApp account ban risk.",
            font=("Arial", 10)
        )
        description_label.pack(pady=5)

        main_frame = tk.Frame(self.root, padx=25, pady=15)
        main_frame.pack(fill="both", expand=True)

        tk.Label(main_frame, text="Safety Profile", font=("Arial", 11, "bold")).grid(row=0, column=0, sticky="w", pady=8)

        self.safety_profile = ttk.Combobox(
            main_frame,
            values=["Conservative", "Moderate", "Aggressive"],
            state="readonly",
            width=25
        )
        self.safety_profile.grid(row=0, column=1, pady=8, sticky="w")
        self.safety_profile.set("Conservative")

        tk.Label(main_frame, text="Minimum Delay (seconds)", font=("Arial", 11)).grid(row=1, column=0, sticky="w", pady=8)
        self.min_delay_entry = tk.Entry(main_frame, width=28)
        self.min_delay_entry.grid(row=1, column=1, pady=8, sticky="w")

        tk.Label(main_frame, text="Maximum Delay (seconds)", font=("Arial", 11)).grid(row=2, column=0, sticky="w", pady=8)
        self.max_delay_entry = tk.Entry(main_frame, width=28)
        self.max_delay_entry.grid(row=2, column=1, pady=8, sticky="w")

        tk.Label(main_frame, text="Max Messages Per Hour", font=("Arial", 11)).grid(row=3, column=0, sticky="w", pady=8)
        self.max_hour_entry = tk.Entry(main_frame, width=28)
        self.max_hour_entry.grid(row=3, column=1, pady=8, sticky="w")

        tk.Label(main_frame, text="Max Messages Per Day", font=("Arial", 11)).grid(row=4, column=0, sticky="w", pady=8)
        self.max_day_entry = tk.Entry(main_frame, width=28)
        self.max_day_entry.grid(row=4, column=1, pady=8, sticky="w")

        self.random_delay_var = tk.BooleanVar(value=True)
        self.auto_pause_var = tk.BooleanVar(value=True)
        self.typing_simulation_var = tk.BooleanVar(value=True)
        self.simulate_reading_var = tk.BooleanVar(value=False)
        self.business_hours_only_var = tk.BooleanVar(value=False)
        self.skip_recent_contacts_var = tk.BooleanVar(value=True)

        checkbox_frame = tk.LabelFrame(main_frame, text="Protection Options", padx=15, pady=10)
        checkbox_frame.grid(row=5, column=0, columnspan=2, sticky="we", pady=15)

        tk.Checkbutton(checkbox_frame, text="Enable Random Delay", variable=self.random_delay_var).pack(anchor="w")
        tk.Checkbutton(checkbox_frame, text="Enable Auto Pause", variable=self.auto_pause_var).pack(anchor="w")
        tk.Checkbutton(checkbox_frame, text="Enable Typing Simulation", variable=self.typing_simulation_var).pack(anchor="w")
        tk.Checkbutton(checkbox_frame, text="Enable Reading Simulation", variable=self.simulate_reading_var).pack(anchor="w")
        tk.Checkbutton(checkbox_frame, text="Business Hours Only (09:00 - 17:00)", variable=self.business_hours_only_var).pack(anchor="w")
        tk.Checkbutton(checkbox_frame, text="Skip Recent Contacts", variable=self.skip_recent_contacts_var).pack(anchor="w")

        tk.Label(main_frame, text="Risk Level", font=("Arial", 11, "bold")).grid(row=6, column=0, sticky="w", pady=8)

        self.risk_level = ttk.Combobox(
            main_frame,
            values=["Low", "Medium", "High"],
            state="readonly",
            width=25
        )
        self.risk_level.grid(row=6, column=1, pady=8, sticky="w")
        self.risk_level.set("Low")

        button_frame = tk.Frame(main_frame)
        button_frame.grid(row=7, column=0, columnspan=2, pady=25)

        self.save_button = tk.Button(
            button_frame,
            text="Save Settings",
            width=18,
            bg="#28a745",
            fg="white"
        )
        self.save_button.grid(row=0, column=0, padx=10)

        self.reset_button = tk.Button(
            button_frame,
            text="Reset to Default",
            width=18,
            bg="#6c757d",
            fg="white"
        )
        self.reset_button.grid(row=0, column=1, padx=10)

        self.status_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 10),
            fg="green"
        )
        self.status_label.pack(pady=10)

    def set_default_values(self):
        self.safety_profile.set("Conservative")
        self.min_delay_entry.delete(0, tk.END)
        self.min_delay_entry.insert(0, "30")

        self.max_delay_entry.delete(0, tk.END)
        self.max_delay_entry.insert(0, "90")

        self.max_hour_entry.delete(0, tk.END)
        self.max_hour_entry.insert(0, "20")

        self.max_day_entry.delete(0, tk.END)
        self.max_day_entry.insert(0, "100")

        self.random_delay_var.set(True)
        self.auto_pause_var.set(True)
        self.typing_simulation_var.set(True)
        self.simulate_reading_var.set(False)
        self.business_hours_only_var.set(False)
        self.skip_recent_contacts_var.set(True)
        self.risk_level.set("Low")


    def load_settings_to_gui(self, settings):
        if not settings:
           self.set_default_values()
           return

        self.safety_profile.set(settings["safety_profile"])

        self.min_delay_entry.delete(0, tk.END)
        self.min_delay_entry.insert(0, settings["min_delay"])

        self.max_delay_entry.delete(0, tk.END)
        self.max_delay_entry.insert(0, settings["max_delay"])

        self.max_hour_entry.delete(0, tk.END)
        self.max_hour_entry.insert(0, settings["max_messages_per_hour"])

        self.max_day_entry.delete(0, tk.END)
        self.max_day_entry.insert(0, settings["max_messages_per_day"])

        self.random_delay_var.set(bool(settings["random_delay"]))
        self.auto_pause_var.set(bool(settings["auto_pause"]))
        self.typing_simulation_var.set(bool(settings["typing_simulation"]))
        self.simulate_reading_var.set(bool(settings["simulate_reading"]))
        self.business_hours_only_var.set(bool(settings["business_hours_only"]))
        self.skip_recent_contacts_var.set(bool(settings["skip_recent_contacts"]))

        self.risk_level.set(settings["risk_level"])