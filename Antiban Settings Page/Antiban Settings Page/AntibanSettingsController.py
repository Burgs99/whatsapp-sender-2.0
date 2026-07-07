from tkinter import messagebox
from DBManager import DBManager


class AntibanSettingsController:
    def __init__(self, gui):
        self.gui = gui
        self.db = DBManager()

        self.gui.save_button.config(command=self.save_settings)
        self.gui.reset_button.config(command=self.reset_settings)

    def save_settings(self):
        try:
            settings = self.get_settings_from_gui()

            self.db.save_antiban_settings(settings)

            self.gui.status_label.config(
                text="Settings saved successfully.",
                fg="green"
            )

            messagebox.showinfo(
                "Success",
                "Antiban settings saved successfully."
            )
   

        except ValueError:
            self.gui.status_label.config(
                text="Please enter valid numeric values.",
                fg="red"
            )

            messagebox.showerror(
                "Input Error",
                "Minimum delay, maximum delay, hourly limit, and daily limit must be numbers."
            )

    def reset_settings(self):
        self.gui.set_default_values()

        self.gui.status_label.config(
            text="Settings reset to default values.",
            fg="green"
        )

    def get_settings_from_gui(self):
        min_delay = int(self.gui.min_delay_entry.get())
        max_delay = int(self.gui.max_delay_entry.get())
        max_messages_per_hour = int(self.gui.max_hour_entry.get())
        max_messages_per_day = int(self.gui.max_day_entry.get())

        if min_delay < 0 or max_delay < 0 or max_messages_per_hour < 0 or max_messages_per_day < 0:
            raise ValueError

        if min_delay > max_delay:
            raise ValueError

        settings = {
            "safety_profile": self.gui.safety_profile.get(),
            "min_delay": min_delay,
            "max_delay": max_delay,
            "random_delay": self.gui.random_delay_var.get(),
            "max_messages_per_hour": max_messages_per_hour,
            "max_messages_per_day": max_messages_per_day,
            "auto_pause": self.gui.auto_pause_var.get(),
            "typing_simulation": self.gui.typing_simulation_var.get(),
            "simulate_reading": self.gui.simulate_reading_var.get(),
            "business_hours_only": self.gui.business_hours_only_var.get(),
            "skip_recent_contacts": self.gui.skip_recent_contacts_var.get(),
            "risk_level": self.gui.risk_level.get()
        }

        return settings

    def load_latest_settings(self):
        settings = self.db.get_latest_antiban_settings()
        self.gui.load_settings_to_gui(settings)