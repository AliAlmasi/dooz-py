class dooz_game:
    def __init__(self):
        self.board = [" "] * 9
        self.current_player = "X"
        self.game_over = False

    def make_move(self, index):
        if self.board[index] == " " and not self.game_over:
            self.board[index] = self.current_player
            return True
        return False

    def check_winner(self):
        wins = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6),
        ]
        for a, b, c in wins:
            if self.board[a] == self.board[b] == self.board[c] != " ":
                self.game_over = True
                return self.board[a]
        return None

    def is_draw(self):
        if " " not in self.board:
            self.game_over = True
            return True
        return False

    def reset(self):
        self.board = [" "] * 9
        self.current_player = "X"
        self.game_over = False

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"
