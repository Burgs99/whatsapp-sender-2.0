import tkinter as tk

from AntibanSettingsGUI import AntibanSettingsGUI
from AntibanSettingsController import AntibanSettingsController


def main():
    root = tk.Tk()

    gui = AntibanSettingsGUI(root)

    controller = AntibanSettingsController(gui)
    controller.load_latest_settings()

    root.mainloop()


if __name__ == "__main__":
    main()
