from ui.app import dooz_app
import tkinter
from tkinter import messagebox
import ctypes
import os
import sys


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


if ctypes.windll or os.name != "nt":
    ctypes.windll.gdi32.AddFontResourceW(resource_path("ui/fonts/vazirmatn.ttf"))
else:
    messagebox.showinfo("Dooz Game", "This app is optimized to run on Windows")

if __name__ == "__main__":
    root = tkinter.Tk()
    app = dooz_app(root)
    root.iconbitmap(True, resource_path("ui/icon.ico"))
    root.mainloop()
