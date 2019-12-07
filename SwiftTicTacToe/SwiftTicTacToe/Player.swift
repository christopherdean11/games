//
//  Player.swift
//  SwiftTicTacToe
//
//  Created by Christopher Dean on 12/7/19.
//  Copyright © 2019 Christopher Dean. All rights reserved.
//

class Player{
    let name: String
    let letter: String
    let id: Int
    
    init(name: String, playerLetter: String, id: Int) {
        self.name = name
        self.letter = playerLetter
        self.id = id
    }
}
