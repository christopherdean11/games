from game import Game
import json

def main(config:dict=None):
    game = Game(config)
    while True:
        game.tick()
        if game.is_over():
            game.print_winner()
            return

def debug():
    game = Game()
    # game.board.state = [[0,1,2,3], [10, 11, 12, 13], [100, 101, 102, 103], [1000, 1001, 1002, 1003]]
    game.board.state = [[0,1,0,-1], [-1,0,1,0],[-1,0,0,1],[0,0,0,0]]
    game.is_over()

if __name__ == "__main__":
    with open('tictactoe/configs.json') as f:
        c = json.load(f)
    main(c)
    # debug()
