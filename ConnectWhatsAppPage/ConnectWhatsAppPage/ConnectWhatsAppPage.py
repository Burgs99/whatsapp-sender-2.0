import tkinter as tk
from connect_whatsapp_gui import ConnectWhatsAppGUI

# Starting point for the Connect WhatsApp page, opens window
if __name__ == "__main__":
    root = tk.Tk()
    app = ConnectWhatsAppGUI(root)
    root.mainloop()
