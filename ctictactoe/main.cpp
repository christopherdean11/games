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
  Board board = Board(game.board_size);
  while (!game.isOver(&board)){
    game.tick(&board);
  }
  game.printWinner();
  return 0;
}
