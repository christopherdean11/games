// project includes
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
  
  while (true){
    game.tick(&board);
    if (game.isOver(&board)){
      game.printWinner(&board);
      return 0;
    }
  }
}
