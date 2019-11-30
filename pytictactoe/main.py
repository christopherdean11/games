import json
from game import Game

def main():
    game = Game()
    while True:
        game.tick()
        if game.is_over():
            game.print_winner()
            return

def debug():
    cfg = {
        "player_letters":["X", "O"],
        "board_size": 4,
        "winning_run_length": 3,
        "debug": True
    }
    game = Game(cfg)
    # game.board.state = [[0,1,2,3], [10, 11, 12, 13], [100, 101, 102, 103], [1000, 1001, 1002, 1003]]
    game.board.state = [[0,1,0,-1], [-1,0,1,0],[-1,0,0,1],[0,0,0,0]]
    game.is_over()
    game.print_winner()

if __name__ == "__main__":
    # main()
    debug()
