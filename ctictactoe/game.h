#ifndef GAME_H
#define GAME_H

#include <iostream>

class Game {
    public:
        int board_size;
        int connect_to_win;
        char player_letters[2];
        void configureGame();
        void printWelcome();
        Game();

        friend std::ostream& operator<<(std::ostream& os, const Game& dt);
};

#endif