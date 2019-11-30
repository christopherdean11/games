// project includes
#include "screencmd.h"
#include "game.h"
#include "board.h"
// built-in includes
#include <iostream>
#include <string>

int main ()
{
  Game game = Game();
  game.printWelcome();
  game.configureGame();
  std::cout << game;
  int players[2] = {1,2};
  // print board state
  Board brd = Board(game.board_size);
  //brd.printBoard(2, players, game.player_letters);
  
  int move[2] = {0,0};
  game.getNextMove(move);
  for (int i = 0; i < 2; i++){
    std::cout << move[i] << ", ";
  }
  std::cout << std::endl;
  return 0;
}
