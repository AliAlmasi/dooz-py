import random

class computer_player:
    def __init__(self, symbol='O'):
        self.symbol = symbol
        self.opponent = 'X' if symbol == 'O' else 'O'

    def choose_move(self, board):
        # 1. اگر بتواند برنده شود، ببرد
        for i in range(9):
            if board[i] == ' ':
                board[i] = self.symbol
                if self._check_win(board, self.symbol):
                    board[i] = ' '
                    return i
                board[i] = ' '

        # 2. اگر حریف بتواند برنده شود، جلویش را بگیرد
        for i in range(9):
            if board[i] == ' ':
                board[i] = self.opponent
                if self._check_win(board, self.opponent):
                    board[i] = ' '
                    return i
                board[i] = ' '

        # 3. مرکز را بگیرد
        if board[4] == ' ':
            return 4

        # 4. گوشه‌ها
        corners = [0, 2, 6, 8]
        empty_corners = [i for i in corners if board[i] == ' ']
        if empty_corners:
            return random.choice(empty_corners)

        # 5. بقیه (کنارها)
        return random.choice([i for i in range(9) if board[i] == ' '])

    def _check_win(self, board, player):
        wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
        return any(board[a] == board[b] == board[c] == player for a,b,c in wins)