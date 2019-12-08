//
//  Board.swift
//  SwiftTicTacToe
//
//  Created by Christopher Dean on 12/7/19.
//  Copyright © 2019 Christopher Dean. All rights reserved.
//

class Move{
    let row: Int
    let col: Int
    init(_ row: Int,_ col: Int){
        self.row = row
        self.col = col
    }
}

class Board{
    var state = [Int]()
    var board_size = 3
    
    init(board_size:Int) {
        self.board_size = board_size
        // initialize board to all zeros
        //self.state = Array(repeating: Array(repeating: 0, count: board_size), board_size)
        self.state = Array(repeating: 0, count: board_size * board_size)
    }
    
    func lookupSingleSpace(_ row: Int,_ col: Int) -> Int{
        return self.state[row * self.board_size + col]
    }
    func lookupSegment(indexes: [Move]) -> [Int]{
        var segment:[Int] = Array(repeating: 0, count: indexes.count)
        for (i, loc) in indexes.enumerated(){
            segment[i] = self.state[loc.row * self.board_size + loc.col]
        }
        return segment
    }
    
    func update(move: (row: Int,col: Int), player: Player) {
        self.state[move.row * self.board_size + move.col] = player.id
    }
    
    func printBoard(players: [Player]){
        printHeader()
        var out = " "
        // print a separator sized to the board
        // for each row
        for i in 0..<self.board_size {
            printSeparator()
            out = String(i+1)
            out.append("  | ")
            // for each column
            for j in 0..<self.board_size {
                // for each player
                var c = " "
                for p in 0..<players.count {
                    // check if square[i,j] is owned by a player
                    if (lookupSingleSpace(i,j) == players[p].id){
                        c = players[p].letter
                        // exit player loop if found
                        break
                    }
                }
                out.append(contentsOf: "\(c) | ")
            }
            print(out)
        }
    }
    private func printSeparator(){
        var out = ""
        out.append(contentsOf: "  -")
        for _ in 0..<self.board_size{
            out.append(contentsOf: "----")
        }
        out.append(contentsOf: "--")
        print(out)
    }
    
    private func printHeader(){
        var row = [String]()
        for i in 0..<self.board_size {
            let c = Character(UnicodeScalar(i+65)!)
            row.append(String(c))
        }
        row.insert("  ", at: 0)
        var r = row.joined(separator: " | ")
        r.append(" | ")
        print(r)
    }
}
