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
        int winner;
        void parseMove(std::string m, int* move_out);
        bool segmentHasWinner(int *segment);
        void updateCurrentPlayer();
        void getNextMove(Board *board, int *move_out);
        void getMoveInput(int *move_out);
        bool isMoveInputValid(std::string buf);
        bool isValidMove(Board *board, int move[]);
        void updateBoard(Board *board, int move[]);

    public:
        int board_size;
        char player_letters[2];
        
        Game(); // constructor
        void configureGame();
        void printWelcome();
        void tick(Board *board);
        bool isOver(Board *board);
        void printWinner(Board *board);

        friend std::ostream& operator<<(std::ostream& os, const Game& dt); // "cout <<" overload
};

#endif
