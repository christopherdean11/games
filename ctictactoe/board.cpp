#include "board.h"
#include "screencmd.h"
#include <iostream>


Board::Board(){
    board_size = 3;
    initBoard();
}

Board::Board(int boardSize){
    board_size = boardSize;
    initBoard();
};

Board::~Board(){
    delete[] state;
};

void Board::initBoard(){
    //need a 2D array, will create a 1D and use 
    // array[i][j] == array[j*i + j] to access it
    state = new int[board_size * board_size];
    for (int i = 0; i < board_size*board_size; i++){
        state[i] = 0;
    }
}

void Board::printBoard(int numPlayers, int players[2], char player_letters[2]){
    // print column headings
    // resetScreen();
    char c;
    std::cout << " ";
    for (int i=0; i < board_size; i++){
        c = 'A' + i;
        std::cout << "  " << c ;
    }
    std::cout << std::endl;

    // loop over rows
    for (int i = 0; i < board_size; i++){
        // add row heading
        std::cout << i+1;
        std::cout << "  ";
        // loop columns in row[i]
        for (int j = 0; j < board_size; j++){
            for (int p = 0; p < numPlayers; p++){
                c = ' ';
                if (state[board_size*i + j] == players[p]){
                    c = player_letters[p];
                    break;
                }
            }
            std::cout << c << "  ";
        }
        // end the row with newline
        std::cout << std::endl;
    }
}

void Board::updateState(int row, int col, int player){
    state[board_size * row + col] = player;
}
