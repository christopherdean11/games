//
//  main.swift
//  SwiftTicTacToe
//
//  Created by Christopher Dean on 12/7/19.
//  Copyright © 2019 Christopher Dean. All rights reserved.
//

import Foundation

let b = Board(board_size: 3)

let p1 = Player(name: "Chris", playerLetter: "C", id: 1)
let p2 = Player(name: "Alli", playerLetter: "A", id: 2)

b.state = [1,0,2,1,2,0,0,1,2]
b.printBoard(players: [p1, p2])
