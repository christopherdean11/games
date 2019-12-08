//
//  main.swift
//  SwiftTicTacToe
//
//  Created by Christopher Dean on 12/7/19.
//  Copyright © 2019 Christopher Dean. All rights reserved.
//

import Foundation

let p1 = Player(name: "Me", playerLetter: "X", id: 1)
let p2 = Player(name: "You", playerLetter: "O", id: 2)
let game = Game(board_size: 4, win_length: 3, players: [p1, p2])
repeat{
    game.tick()
} while !game.isOver()
game.printBoard()
game.printWinner()
