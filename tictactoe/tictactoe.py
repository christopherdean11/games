import os

BOARD_START = [[' ', ' ', ' '],  [' ', ' ', ' '], [' ', ' ', ' ']]

class Board:
    state = []

    def __init__(self):
        # self.state = [[-1, -1, -1],[-1, -1, -1], [-1, -1,-1]]
        self.state = [[' ', ' ', ' '],  [' ', ' ', ' '], [' ', ' ', ' ']]

    def update(self, player, move):
        pass

    def _print_board_row(self, board_row, rowId: int):
        print(f'{rowId} {board_row[0]} | {board_row[1]} | {board_row[2]}')

    def print_board(self):
        print()
        print('  A   B   C')
        self._print_board_row(self.state[0], 1)
        print(' -----------')
        self._print_board_row(self.state[1], 2)
        print(' -----------')
        self._print_board_row(self.state[2], 3)

class Game:
    state = {}
    board = []
    player_letters = ['X', 'O']

    def __init__(self):
        self.board = Board()
        self.state['activePlayerIdx'] = 0

    def tick(self):
        self._reset_screen()
        self.board.print_board()
        move = self.get_next_move()
        loc = self.parse_move(move)
        self.update_board(loc)
        self.update_player()

    def _reset_screen(self):
        os.system('clear')

    def get_next_move(self):
        return input(f"Player {self.player_letters[self.state['activePlayerIdx']]}, enter move: ")
        
    def parse_move(self, move):
        # must be formatted as 'A1'
        col = ord(move[0]) - ord('A')
        row = int(move[1]) - 1
        return (row, col)

    def update_board(self, loc):
        self.board.state[loc[0]][loc[1]] = self.player_letters[self.state['activePlayerIdx']]

    def update_player(self):
        self.state['activePlayerIdx'] = 1 - self.state['activePlayerIdx']

    def is_over(self):
        board_seg = []
        board = self.board.state
        for row in board:
            board_seg.append(row)
        
        board_seg.append([board[0][0], board[1][0], board[2][0]]) # col 1
        board_seg.append([board[0][1], board[1][1], board[2][1]]) # col 2
        board_seg.append([board[0][2], board[1][2], board[2][2]]) # col 3
        board_seg.append([board[0][0], board[1][1], board[2][2]]) # diag 1
        board_seg.append([board[0][2], board[1][1], board[0][2]]) # diag 2

        for seg in board_seg:
            xwin = 'XXX' == ''.join(seg).strip()
            owin = 'OOO' == ''.join(seg).strip()
            if xwin or owin:
                self._reset_screen()
                self.board.print_board()
                player_letter = 'X' if xwin else 'O'
                print(f'Game Over. {player_letter} wins!')
                return True
        return False

def main():
    game = Game()
    while True:
        game.tick()
        if game.is_over():
            return

if __name__ == "__main__":
    main()

