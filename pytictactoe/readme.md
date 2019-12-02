## Tic Tac Toe 3000 (Python)

Run `python main.py` to play Tic Tac Toe 3000!
Play a game with a configurable size board and number of boxes in a row required to win


### Playing the game
Upon launching `main.py` you will see the following:  
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

Playing the game with a win length (number of connections in a row to win) less than the side length of the board is possible and can make for much more interesting gameplay than standard rules!   

For example, a game could look something like this (board size = 6, win length = 4):  
```
  A   B   C   D   E   F  
1   | X |   |   |   |   | 
 ------------------------
2   | X | X | O |   |   | 
 ------------------------
3   |   |   | X |   |   | 
 ------------------------
4   |   | O | O | X |   | 
 ------------------------
5   |   |   |   |   | O | 
 ------------------------
6   |   |   |   |   |   | 
Game Over. X wins!
```
