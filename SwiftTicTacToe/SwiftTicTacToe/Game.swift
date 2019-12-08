//
//  Game.swift
//  SwiftTicTacToe
//
//  Created by Christopher Dean on 12/7/19.
//  Copyright © 2019 Christopher Dean. All rights reserved.
//

class Game{
    let players: [Player]
    var winner: Player? = nil
    var active_player_idx: Int = 0
    var board: Board
    
    // configuration
    let board_size: Int
    let connect_to_win: Int
    
    init(board_size: Int, win_length: Int, players: [Player]){
        self.board_size = board_size
        self.connect_to_win = win_length
        self.players = players
        self.board = Board(board_size: self.board_size)
    }
    
    func tick() {
        clearScreen()
        self.board.printBoard(players: self.players)
        let move = getNextMove(player: self.players[self.active_player_idx])
        updateBoard(move: move)
        updateActivePlayer()
    }
    
    func isOver() -> Bool{
        var segment = Array(repeating: 0, count: self.board_size)
        // check rows
        for i in 0..<self.board_size{
            for j in 0..<self.board_size{
                segment[j] = self.board.lookupSingleSpace(i, j)
            }
            if segmentHasWinner(segment){
                return true
            }
        }
        // check columns
        for i in 0..<self.board_size{
            for j in 0..<self.board_size{
                segment[j] = self.board.lookupSingleSpace(j, i)
            }
            if segmentHasWinner(segment){
                return true
            }
        }
        
        // check diagonals
        for i in 0..<self.board_size{
            segment[i] = self.board.lookupSingleSpace(i, i)
        }
        if segmentHasWinner(segment){
            return true
        }
        // check diagonals
        for i in 0..<self.board_size{
            segment[i] = self.board.lookupSingleSpace(i, self.board_size-1-i)
        }
        if segmentHasWinner(segment){
            return true
        }
        return false
    }
    
    func segmentHasWinner(_ segment: [Int]) -> Bool{
        var count: Int
        // loop all players
        for player in self.players{
            // reset count for each player
            count = 0
            // loop all spaces in this segment
            for space in segment{
                // if space owned by player, increment count
                // otherwise reset count
                if space == player.id{
                    count += 1
                }else{
                    count = 0
                }
                // check if count is sufficient to win each iterattion
                // because connect_to_win could be less than board_size
                if count >= self.connect_to_win{
                    // if winner is found set winner property
                    // and return early
                    self.winner = player
                    return true
                }
            }
        }
        return false
    }
    
    func printWinner(){
        if let w = winner {
            print("\(w.name) wins!")
        }else{
            print("An error occured finding the winner")
        }
    }
    
    func updateActivePlayer(){
        var i = self.active_player_idx + 1
        if i == self.players.count{
            i = 0
        }
        self.active_player_idx = i
    }
    
    func updateBoard(move: (Int, Int)){
        self.board.update(move: move, player: self.players[self.active_player_idx])
    }
    
    func printBoard(){
        self.board.printBoard(players: self.players)
    }
    
    func getNextMove(player: Player) -> (row:Int, col:Int){
        var move: (Int, Int)?
        var validMove = false
        repeat {
            print("\(player.name), enter your next move: ", terminator: "")
            let rawResponse = readLine(strippingNewline: true)
            if let resp = rawResponse{
                // response was not nil
                // try to parse
                move = parseMove(resp)
                validMove = move != nil
                if !validMove{
                    print("Please try again and enter a move in the format, A1")
                }
            }
        } while !validMove
        return (move!.0, move!.1)
    }
    
    func parseMove(_ strIn: String) -> (Int, Int)? {
        // I feel bad about the if else trees in this function, but not sure how else to handle it
        var row: Int
        var col: Int
        
        // input string has two characters
        if strIn.count != 2{
            return nil
        }
        // first char is letter between A and A + board size
        if let c = strIn.first?.asciiValue{
            if c >= 65 && c < 65+self.board_size{
                // convert to 0-indexed int
                col = Int(c) - 65
            }else{
                return nil
            }
        }else{
            return nil
        }
        // second char is an integer
        if let c = strIn.last?.wholeNumberValue {
            // convert to 0-indexed int (is a 1-index int in user's view)
            if c > 0 && c <= self.board_size{
                row = c - 1
            }else{
                return nil
            }
        }else{
            return nil
        }
        if self.board.lookupSingleSpace(row, col) != 0{
            print("Board space already taken, please try again")
            return nil
        }
        
        return (row, col)
    }
    
    func clearScreen(){
        // print an ANSI escape sequence for clear screen to the terminal
        print("\u{001B}[2J")
    }
}
