import tkinter as tk
from game.logic import dooz_game
from game.ai import computer_player
from ui.MessageBox import message_box


def default_font(size=16, bold=False):
    return ("Vazirmatn" if bold == False else "Vazirmatn Bold", size)


def end_game_message(parent, message="!بازی تمام"):
    message_box(parent, "پایان بازی", message)


class dooz_app:
    def __init__(self, root):
        self.root = root
        self.root.title("Dooz Game")
        self.root.geometry("450x550")
        self.root.resizable(False, False)

        self.game_mode = None
        self.game = dooz_game()
        self.computer = None

        self.mode_frame = tk.Frame(root)
        self.mode_frame.pack(pady=50)

        tk.Label(
            self.mode_frame, text="بازی دوز", font=default_font(26, bold=True)
        ).pack(pady=(30, 0))
        tk.Label(
            self.mode_frame, text="حالت بازی را انتخاب کنید", font=default_font()
        ).pack(pady=20)
        tk.Button(
            self.mode_frame,
            text="دو نفره",
            font=default_font(),
            command=lambda: self.start_game("pvp"),
            width=30,
            bg="#3a7afe",
            fg="white",
            activebackground="#264ea5",
            relief="flat",
        ).pack(pady=10)
        tk.Button(
            self.mode_frame,
            text="با کامپیوتر",
            font=default_font(),
            command=lambda: self.start_game("pvc"),
            width=30,
            bg="#3a7afe",
            fg="white",
            activebackground="#264ea5",
            relief="flat",
        ).pack(pady=10)

    def start_game(self, mode):
        self.game_mode = mode
        self.computer = computer_player() if mode == "pvc" else None

        self.mode_frame.destroy()

        self.buttons = []
        self.status_label = tk.Label(self.root, text="نوبت X", font=default_font(18))
        self.status_label.pack(pady=10)

        board_frame = tk.Frame(self.root)
        board_frame.pack()

        for i in range(3):
            for j in range(3):
                btn = tk.Button(
                    board_frame,
                    text=" ",
                    font=default_font(30),
                    width=5,
                    height=1,
                    command=lambda idx=i * 3 + j: self.button_click(idx),
                )
                btn.grid(row=i, column=j)
                self.buttons.append(btn)

        self.restart_btn = tk.Button(
            self.root,
            text="شروع مجدد",
            font=default_font(),
            command=self.restart_game,
            width=30,
            bg="#3a7afe",
            fg="white",
            activebackground="#264ea5",
            relief="flat",
        ).pack(pady=20)

        if self.game_mode == "pvc" and self.game.current_player == "O":
            self.computer_move()

    def button_click(self, index):
        if self.game.game_over or not self.game.make_move(index):
            return

        self.buttons[index].config(text=self.game.current_player)
        self.update_status()

        winner = self.game.check_winner()
        if winner:
            end_game_message(self.root, f"{winner} :برنده")
            return
        if self.game.is_draw():
            end_game_message(self.root, "مساوی")
            return

        self.game.switch_player()
        self.update_status()

        if self.game_mode == "pvc" and self.game.current_player == "O":
            self.root.after(500, self.computer_move)

    def computer_move(self):
        move = self.computer.choose_move(self.game.board)
        if move is not None:
            self.game.make_move(move)
            self.buttons[move].config(text="O")
            self.update_status()

            winner = self.game.check_winner()
            if winner:
                end_game_message(self.root, "!کامپیوتر برنده شد")
                return
            if self.game.is_draw():
                end_game_message(self.root, "مساوی")
                return

            self.game.switch_player()
            self.update_status()

    def update_status(self):
        if self.game.game_over:
            self.status_label.config(text="بازی تمام شد")
        else:
            self.status_label.config(text=f"نوبت {self.game.current_player}")

    def restart_game(self):
        self.game.reset()
        for btn in self.buttons:
            btn.config(text=" ")
        self.update_status()
