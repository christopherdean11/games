import os
from board import Board

class Game:
    # internal use
    state = dict() # empty dictionary
    board = []     # empty list
    players = [-1, 1]
    winner = ''
    # configuration
    player_letters = ['X', 'O']
    board_size = 3
    connect_to_win = 3

    def __init__(self, config:dict = None):
        self.state['activePlayerIdx'] = 0
        self._welcome(config)
        self._configure_game(config)
        self.board = Board(self.board_size)

    def tick(self):
        self._reset_screen()
        self.board.print_board()
        move = self.get_next_move()
        self.update_board(move)
        self.update_player()

    def get_next_move(self):
        move = self._get_user_move_input()
        while not self.is_valid_move(move):
            print('Invalid move, space not available. Try again.')
            move = self._get_user_move_input()
        return move
    
    def is_valid_move(self, possible_move):
        return self.board.state[possible_move[0]][possible_move[1]] == 0

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

    def print_winner(self):
        self._reset_screen()
        self.board.print_board()
        print(f'Game Over. {self.winner} wins!')

    def is_over(self):
        board_seg = []
        board = self.board.state
        
        # get each row as a segment
        for row in board:
            board_seg.append(row)
        # transpose and check again to get columns
        for col in zip(*board):
            board_seg.append(col)
        
        # get diagonals - top left to bottom right, moving down
        diag1 = dict()
        for offset in range(0, self.board_size - self.connect_to_win + 1):
            for i in range(0, self.board_size - offset):
                if offset not in diag1:
                    diag1[offset] = []
                diag1[offset].append(board[i+offset][i])

        # get diagonals - top left to bottom right, moving right, start at one to skip main diagonal (is in diag3)
        diag2 = dict()
        for offset in range(1, self.board_size - self.connect_to_win + 1):
            for i in range(0, self.board_size - offset):
                if offset not in diag2:
                    diag2[offset] = []
                diag2[offset].append(board[i][i+offset])

        # get diagonals - bottom left to top right, moving up
        diag3 = dict()
        for offset in range(0, self.board_size - self.connect_to_win + 1):
            for i in range(0, self.board_size - offset):
                if offset not in diag3:
                    diag3[offset] = []
                diag3[offset].append(board[self.board_size - 1 - i - offset][i])

        # get diagonals - bottom left to top right, moving right, start at one to skip main diagonal (is in diag3)
        diag4 = dict()
        for offset in range(1, self.board_size - self.connect_to_win + 1):
            for i in range(0, self.board_size - offset):
                if offset not in diag4:
                    diag4[offset] = []
                diag4[offset].append(board[self.board_size - 1 - i][i+offset])

        for d in diag1.values():
            board_seg.append(d)

        for d in diag2.values():
            board_seg.append(d)

        for d in diag3.values():
            board_seg.append(d)
        
        for d in diag4.values():
            board_seg.append(d)

        for seg in board_seg:
            xcount = 0
            ocount = 0
            for i in range(len(seg)):
                if self.players[0] == seg[i]:
                    xcount = xcount + 1
                else:
                    # reset xcount counter if not equal to ensure win only when N number in a row
                    xcount = 0
                if self.players[1] == seg[i]:
                    ocount = ocount + 1
                else:
                    # reset ocount counter, same as xwin reset
                    ocount = 0
                
                if xcount >= self.connect_to_win or ocount >= self.connect_to_win:
                    self.winner =  self.player_letters[0] if xcount else self.player_letters[1]
                    return True
        return False
    
    # --- Private Methods  ---------------------------------------------------------
    def _reset_screen(self):
        os.system('clear')

    def _welcome(self, config=None):
        if config is not None:
            dbg = config.get('debug',False)
            
        if not dbg:
            self._reset_screen()
            print('==========================')
            print('    Tic Tac Toe 3000!')
            print()
            print('Game Configuration')

    def _configure_game(self, config:dict = None):
        if config is None:
            resp = input('Use custom player letters? y/[n]: ')
            if resp == 'y':
                self._get_player_letters()
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
        else:
            pass
            self.player_letters = config['player_letters']
            self.board_size = config['board_size']
            self.connect_to_win = config['winning_run_length']

    def _get_player_letters(self):
        player1 = input('Player 1, enter your letter: ')
        player2 = input('Player 2, enter your letter: ')
        self.player_letters = [player1, player2]

    def _is_response_valid(self, new_move_response):
        if len(new_move_response) != 2:
            # must two characters
            return False
        try:
            int(new_move_response[1])
        except ValueError:
            # second character is not an int
            return False
        
        if not new_move_response[0].isalpha():
            # first character is not A-Z
            return False

        if new_move_response[0].islower():
            return False

        return True

    def _get_user_move_input(self):
        resp = input(f"Player {self.player_letters[self.state['activePlayerIdx']]}, enter move: ")
        if resp == 'quit':
            raise SystemExit # completely quit the application
        while not self._is_response_valid(resp):
            print('Invalid input format. Try again. Must be formatted as A1')
            resp = input(f"Player {self.player_letters[self.state['activePlayerIdx']]}, enter move: ")
        return self.parse_move(resp)
