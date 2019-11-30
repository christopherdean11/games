// project includes
#include "screencmd.h"
#include "game.h"
#include "board.h"
// built-in includes
#include <iostream>

int main ()
{
  Game game = Game();
  game.printWelcome();
  game.configureGame();
  std::cout << game;
  int players[2] = {1,2};
  // print board state
  Board brd = Board(game.board_size);
  brd.printBoard(2, players, game.player_letters);
  brd.updateState(0,1,players[0]);
  brd.updateState(1,0,players[1]);
  brd.updateState(0,2,players[0]);
  brd.updateState(2,2,players[1]);
  brd.printBoard(2, players, game.player_letters);
  return 0;
}
