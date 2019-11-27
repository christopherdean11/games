class Board:
    state = []
    show = []

    def __init__(self, size):
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
            
