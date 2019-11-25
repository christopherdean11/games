import os

class Board:
    state = []
    show = []

    def __init__(self):
        # self.state = [[0, 0, 0],[0, 0, 0], [0, 0, 0]]
        self.state = [[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0]]
        self.show = [[' ', ' ', ' ', ' '],  [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '],[' ', ' ', ' ', ' ']]

    def update(self, loc, player, letter):
        self.state[loc[0]][loc[1]] = player
        self.show[loc[0]][loc[1]] = letter

    def _print_board_row(self, board_row, rowId: int):
        print(f'{rowId} {board_row[0]} | {board_row[1]} | {board_row[2]} | {board_row[3]}')

    def print_board(self):
        print()
        print('  A   B   C')
        for i in range(0, len(self.show)):                
            self._print_board_row(self.show[i], i+1)
            if i < len(self.show)-1:
                print(' -----------')

class Game:
    state = {}
    board = []
    player_letters = ['X', 'O']
    players = [-1, 1]
    board_size = 4

    def __init__(self):
        self.board = Board()
        self.state['activePlayerIdx'] = 0
        resp = input('Set player letters y/[n]: ')
        if resp == 'y':
            self.get_player_letters()

    def get_player_letters(self):
        player1 = input('Player 1, enter your letter: ')
        player2 = input('Player 2, enter your letter: ')
        self.player_letters = [player1, player2]

    def tick(self):
        self._reset_screen()
        self.board.print_board()
        move = self.get_next_move()
        loc = self.parse_move(move)
        self.update_board(loc, )
        self.update_player()

    def _reset_screen(self):
        os.system('clear')

    def get_next_move(self):
        return input(f"Player {self.player_letters[self.state['activePlayerIdx']]}, enter move: ")
        
    def parse_move(self, move):
        # must be formatted as 'A1'
        col = ord(move[0]) - ord('A')
        row = int(move[1]) - 1
        # have to verify move is available on the board
        return (row, col)

    def update_board(self, loc):
        self.board.update(loc, self.players[self.state['activePlayerIdx']], self.player_letters[self.state['activePlayerIdx']])

    def update_player(self):
        self.state['activePlayerIdx'] = 1 - self.state['activePlayerIdx']

    def is_over(self):
        board_seg = []
        board = self.board.state
        for row in board:
            board_seg.append(row)
        
        for col in zip(*board):
            board_seg.append(col)

        diag1 = []
        diag2 = []
        for i in range(0, len(board)):
            diag1.append(board[i][i])
            diag2.append(board[i][len(board)-i-1])

        board_seg.append(diag1)
        board_seg.append(diag2)

        for seg in board_seg:
            xwin = self.players[0] * self.board_size == sum(seg)
            owin = self.players[1] * self.board_size == sum(seg)
            if xwin or owin:
                self._reset_screen()
                self.board.print_board()
                winner_letter = self.player_letters[0] if xwin else self.player_letters[1]
                print(f'Game Over. {winner_letter} wins!')
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
