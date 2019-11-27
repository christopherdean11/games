import pytest
from game import Game

def game_config(size, win_length):
    return {
        'board_size': size,
        'winning_run_length': win_length,
        'player_letters':['X', 'O']
    }

def test_gameconfig():
    cfg = game_config(4,3)
    cfg['player_letters'] = ['A', 'B']
    game = Game(cfg)
    assert game.board_size==4
    assert game.connect_to_win == 3
    assert game.player_letters == ['A', 'B']

def test_valid_move_true():
    cfg = game_config(2,2)
    game = Game(cfg)
    game.board.state = [[0,1], [1,0]]
    assert game.is_valid_move((0,0))

def test_valid_move_false():
    cfg = game_config(2,2)
    game = Game(cfg)
    game.board.state = [[0,1], [1,0]]
    assert game.is_valid_move((1,0))==False

def test_is_over_row():
    cfg = game_config(3,3)
    game = Game(cfg)
    game.board.state = [[1,1,1],[0,0,0], [1,0,1]]
    assert game.is_over()

def test_is_over_col():
    cfg = game_config(3,3)
    game = Game(cfg)
    game.board.state = [[1,0,0],[1,0,0], [1,0,1]]
    assert game.is_over()

def test_is_over_diag1():
    # diagonal from top left to bottom right
    cfg = game_config(3,3)
    game = Game(cfg)
    game.board.state = [[1,0,0],[0,1,0], [0,0,1]]
    assert game.is_over()

def test_is_over_diag2():
    # diagonal from bottom left to top right
    cfg = game_config(3,3)
    game = Game(cfg)
    game.board.state = [[0,0,1],[0,1,0], [1,0,0]]
    assert game.is_over()

def test_is_over_diag1_partial():
    # diagonal from top left to bottom right
    cfg = game_config(4,3)
    game = Game(cfg)
    game.board.state = [[0,1,0,0],[0,0,1,0], [0,0,0,1],[0,0,0,0]]
    assert len(game.board.state)==4, "incorrectly size debug board"
    assert len(game.board.state[0])==4, "incorrectly sized debug board"
    assert game.is_over()

def test_is_over_diag2_partial():
    # diagonal from top left to bottom right
    cfg = game_config(4,3)
    game = Game(cfg)
    game.board.state = [[0,0,0,1],[0,0,1,0], [0,1,0,0],[0,0,0,0]]
    assert len(game.board.state)==4, "incorrectly size debug board"
    assert len(game.board.state[0])==4, "incorrectly sized debug board"
    assert game.is_over()