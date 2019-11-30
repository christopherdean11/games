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

  // print board state
  Board brd = Board(game.board_size
  );
  std::cout << "\n\nBoard State:\n";
  for (int i=0;i<brd.size;i++){
    for (int j = 0; j < brd.size; j++){
      std::cout << brd.state[j*i + j];
    }
    std::cout << std::endl; 
  }
  std::cout<< std::endl;

  return 0;
}
