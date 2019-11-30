#ifndef GAME_H
#define GAME_H

#include <iostream>
#include <string>

class Game {
    public:
        int board_size;
        int connect_to_win;
        char player_letters[2];
        Game(); // constructor
        void configureGame();
        void printWelcome();
        void getNextMove(int* move_out);
        void parseMove(std::string m, int* move_out);

        friend std::ostream& operator<<(std::ostream& os, const Game& dt); // "cout <<" overload
};

#endif