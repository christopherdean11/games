#ifndef GAME_H
#define GAME_H

#include "board.h"
#include <iostream>
#include <string>


class Game {
    private:
        int current_player;
        int num_players;
        int connect_to_win;
        void parseMove(std::string m, int* move_out);

    public:
        // Board board;
        char player_letters[2];
        int board_size;
        Game(); // constructor
        void configureGame();
        void printWelcome();
        void getNextMove(int* move_out);
        void updateBoard(Board *board, int move[]);
        void updateCurrentPlayer();
        void tick(Board *board);

        friend std::ostream& operator<<(std::ostream& os, const Game& dt); // "cout <<" overload
};

#endif