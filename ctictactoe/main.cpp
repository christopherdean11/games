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
  Board board = Board(game.board_size);
  int nTurns = 0;
  while (nTurns < 4){
    game.tick(&board);
    nTurns++;
  }

  return 0;
}
