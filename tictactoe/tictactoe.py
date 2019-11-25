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
        self._print_board_row(board[0], 1)
        print(' -----------')
        self._print_board_row(board[1], 2)
        print(' -----------')
        self._print_board_row(board[2], 3)



class Game:
    state = []
    board = []
    player_letters = ['X', 'O']

    def __init__(self):
        self.board = Board()
        self.state['activePlayerIdx'] = 0


    def get_next_move(self):
        # return input(f'Player {self.player_letters[self.state['activePlayerIdx']]}, enter move: ')
        pass

    def parse_move(self, move):
        # must be formatted as 'A1'
        col = ord(move[0]) - ord('A')
        row = int(move[1]) - 1
        return (row, col)

    def check_winner(self):
        board_seg = []
        for row in self.board:
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
                reset_screen()
                print_board(board)
                player_letter = 'X' if xwin else 'O'
                print(f'Game Over. {player_letter} wins!')
                return True
        
        return False



def reset_screen():
    os.system('clear')

def get_move(player_letter):
    return input(f'Player {player_letter}, enter move: ')

def parse_move(move):
    # must be formatted as 'A1'
    col = ord(move[0]) - ord('A')
    row = int(move[1]) - 1
    return (row, col)


def _print_board_row(board_row, rowId: int):
    print(f'{rowId} {board_row[0]} | {board_row[1]} | {board_row[2]}')


def print_board(board):
    print()
    print('  A   B   C')
    _print_board_row(board[0], 1)
    print(' -----------')
    _print_board_row(board[1], 2)
    print(' -----------')
    _print_board_row(board[2], 3)

def check_winner(board):
    board_seg = []
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
            reset_screen()
            print_board(board)
            player_letter = 'X' if xwin else 'O'
            print(f'Game Over. {player_letter} wins!')
            return True
    
    return False

def main():
    board = BOARD_START
    move_count = 0
    while True:
        reset_screen()
        print_board(board)

        player = move_count % 2
        player_letter = 'X' if player else 'O'
        move = get_move(player_letter)
        loc = parse_move(move)
        board[loc[0]][loc[1]] = player_letter
        move_count = move_count + 1

        if check_winner(board):
            return


if __name__ == "__main__":
    main()

