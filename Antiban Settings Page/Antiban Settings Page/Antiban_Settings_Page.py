import tkinter as tk

from AntibanSettingsGUI import AntibanSettingsGUI
from AntibanSettingsController import AntibanSettingsController

# Starting point for the Antiban settings page, builds the screen and connects it to the database logic
def main():
    root = tk.Tk()

    gui = AntibanSettingsGUI(root)

    controller = AntibanSettingsController(gui)
    controller.load_latest_settings()

    root.mainloop()

# Only runs main() if this file is opened directly
if __name__ == "__main__":
    main()
