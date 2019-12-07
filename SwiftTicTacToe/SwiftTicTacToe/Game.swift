//
//  Game.swift
//  SwiftTicTacToe
//
//  Created by Christopher Dean on 12/7/19.
//  Copyright © 2019 Christopher Dean. All rights reserved.
//

class Game{
    var state: [Int] = []
    let players = [1, 2]
    var winner = ""
    // configuration
    let player_letters = ["X", "O"]
    var board_size = 3
    var connect_to_win = 3
    
    init(board_size: Int, win_length: Int){
        self.board_size = board_size
        self.connect_to_win = win_length
    }
    
}
