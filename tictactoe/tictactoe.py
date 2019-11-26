import os

class Board:
    state = []
    show = []

    def __init__(self, size):
        # self.state = [[0, 0, 0],[0, 0, 0], [0, 0, 0]]
        self.state =[[0 for y in range(size) ] for x in range(size)] 
        self.show = [[' ' for y in range(size) ] for x in range(size)]
        self.size = size

    def update(self, loc, player, letter):
        self.state[loc[0]][loc[1]] = player
        self.show[loc[0]][loc[1]] = letter

    def _print_board_row(self, board_row, rowId: int):
        print(f'{rowId} '  , end='')
        for i in range(self.size):
            print(f'{board_row[i]} | ', end='')
        print()

    def print_board(self):
        print()
        headers = '   '.join([chr(y) for y in [x+65 for x in range(self.size)]])
        headers = '  ' + headers + '  '
        print(headers)
        for i in range(0, self.size):                
            self._print_board_row(self.show[i], i+1)
            if i < len(self.show)-1:
                print(' ', end='')
                print(''.join(['----']*self.size))
            

class Game:
    state = {}
    board = []
    player_letters = ['X', 'O']
    players = [-1, 1]
    board_size = 3
    connect_to_win = 3

    def __init__(self):
        self._welcome()
        self.state['activePlayerIdx'] = 0
        self._configure_game()
        self.board = Board(self.board_size)
    
    def _configure_game(self):
        resp = input('Use custom player letters? y/[n]: ')
        if resp == 'y':
            self.get_player_letters()
        resp = input('What size board? [3]: ')
        if resp == '':
            self.board_size = 3
        else:
            self.board_size = int(resp)
        cont = True
        while cont:
            resp = input(f'How many to connect to win? [{self.board_size}]: ')
            if resp == '':
                resp = self.board_size
            try:
                self.connect_to_win = int(resp)
                cont = False
            except ValueError:
                continue


    def _welcome(self):
        self._reset_screen()
        print('==========================')
        print('    Tic Tac Toe 3000!')
        print()
        print('Game Configuration')


    def tick(self):
        self._reset_screen()
        self.board.print_board()
        move = self.get_next_move()
        self.update_board(move)
        self.update_player()

    def _reset_screen(self):
        os.system('clear')

    def get_next_move(self):
        move = self._get_user_move_input()
        while not self.is_valid_move(move):
            print('Invalid move, space not available. Try again.')
            move = self._get_user_move_input()
        return move

    def _get_user_move_input(self):
        resp = input(f"Player {self.player_letters[self.state['activePlayerIdx']]}, enter move: ")
        while not self._is_response_valid(resp):
            print('Invalid input format. Try again. Must be formatted as A1')
            resp = input(f"Player {self.player_letters[self.state['activePlayerIdx']]}, enter move: ")
        return self.parse_move(resp)

    def is_valid_move(self, possible_move):
        return self.board.state[possible_move[0]][possible_move[1]] == 0

    def _is_response_valid(self, possible_move):
        if len(possible_move) != 2:
            # must two characters
            return False
        try:
            int(possible_move[1])
        except ValueError:
            # second character is not an int
            return False
        
        if not possible_move[0].isalpha():
            # first character is not A-Z
            return False

        if possible_move[0].islower():
            return False

        return True


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

    def get_player_letters(self):
        player1 = input('Player 1, enter your letter: ')
        player2 = input('Player 2, enter your letter: ')
        self.player_letters = [player1, player2]

    def is_over(self):
        board_seg = []
        board = self.board.state
        for row in board:
            board_seg.append(row)
        # transpose and check again to get columns
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
            xwin = 0
            owin = 0
            for i in range(len(seg)):
                if self.players[0] == seg[i]:
                    xwin = xwin + 1
                if self.players[1] == seg[i]:
                    owin = owin + 1
            if xwin >= self.connect_to_win or owin >= self.connect_to_win:
            # xwin = [self.players[0]] * self.connect_to_win in seg
            # owin = [self.players[1]] * self.connect_to_win in seg
            # if xwin or owin:
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
