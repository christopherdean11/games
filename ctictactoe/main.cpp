// project includes
#include "screencmd.h"
#include "game.h"
// built-in includes
#include <iostream>

int main ()
{
  char* player_letters;
  printWelcome();
  Game game = Game();
  game.configureGame();

  // debug printing
  std::cout << "Player1: " << game.player_letters[0] << "\nPlayer 2: " << game.player_letters[1] << std::endl;
  return 0;
}
