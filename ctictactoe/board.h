#ifndef GAME_BOARD_H
#define GAME_BOARD_H

#include <string>

class Board{
    public:
        int *state;
        int board_size;
        std::string show;
        Board(int); // constructor
        ~Board();
        void printBoard(int numPlayers, int players[2], char player_letters[2]);
        void updateState(int row, int col, int player);
};

#endif