import tkinter as tk


class message_box(tk.Toplevel):
    def __init__(self, parent, title, message):
        super().__init__(parent)
        self.title(title)
        self.geometry("200x150")
        self.resizable(False, False)

        self.transient(parent)
        self.grab_set()

        tk.Label(self, text=message, font=("Vazirmatn", 14), wraplength=150).pack(
            padx=20, pady=20
        )

        tk.Button(
            self,
            text="حله اوکی",
            font=("Vazirmatn", 12),
            bg="#3a7afe",
            fg="white",
            activebackground="#264ea5",
            relief="flat",
            padx=20,
            command=self.destroy,
        ).pack(pady=(0, 20))

        self.update_idletasks()
        self.center(parent)
        self.focus()

    def center(self, parent):
        x = parent.winfo_x() + parent.winfo_width() // 2 - self.winfo_width() // 2
        y = parent.winfo_y() + parent.winfo_height() // 2 - self.winfo_height() // 2
        self.geometry(f"+{x}+{y}")
