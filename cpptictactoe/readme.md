## Tic Tac Toe 3000 (C++)

Build and run to play Tic Tac Toe 3000!  
Play a game with a configurable size board and number of boxes in a row required to win


### Build
Currently builds on Mac with clang++ using `clang++ *.cpp -o main.out`.  Note Mac requires installing the XCode Command Line Tools (or full Xcode).

### Playing the game
Upon launching `main.out` you will see the following:  
```
==========================
    Tic Tac Toe 3000!

Game Configuration
Use custom player letters? y/[n]: 
```
Respond with `y` to customize the player letters or answer blank or anything else to use default letters: `X, O`.  

Continue setup. 
```
Use custom player letters? y/[n]: y
Player 1, enter your letter: X
Player 2, enter your letter: O
What size board? [3]: 4
How many to connect to win? [4]: 4  
```

Then play! Enter a move in the format: `A1`
```
  A   B   C   D  
1   |   |   |   | 
 ----------------
2   |   |   |   | 
 ----------------
3   |   |   |   | 
 ----------------
4   |   |   |   | 
Player X, enter move: 
```
Continue playing until someone wins
```
  A   B   C   D  
1 X | O | O | O | 
 ----------------
2   | X |   |   | 
 ----------------
3   |   | X |   | 
 ----------------
4   |   |   | X | 
Game Over. X wins!
```

### Notes and Future Improvements
#### Win Checker
Win checker currently only checks for rows, columns, and the true diagonals.  A true diagonal is from corner to corner.  This means the if the game is started with a number of connections to win (run length) less than the length of a side, only the true diagonals can be used to win, currently.  See the python version `pytictactoe` in this repo for full diagonal checking support.  

For example, this is a win for `X` when the board is 4x4, and run length is 3.
```
  A   B   C   D  
1 X |   |   |   | 
 ----------------
2   | X |   |   | 
 ----------------
3   |   | X |   | 
 ----------------
4   |   |   |   | 
Game Over. X wins!
```

However, currently, this is not detected as a win in the same configuration (4x4, run length = 3): 
```
  A   B   C   D  
1   | X |   |   | 
 ----------------
2   |   | X |   | 
 ----------------
3   |   |   | X | 
 ----------------
4   |   |   |   | 
```
This will be fixed in a future update.


#### Move Entry
Support for detecting an invalid move is currently not implemented, so a new move can overwrite a previous play, and malformed input is essentially thrown away and you lose your turn. `pytictactoe` has this implemented and is coming soon to `ctictactoe`. 