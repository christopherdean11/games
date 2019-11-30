#include "board.h"

Board::Board(int board_size){
    size = board_size;
    // need a 2D array, will create a 1D and use 
    // array[i][j] == array[j*i + j] to access it
    state = new int[board_size * board_size];
};

Board::~Board(){
    delete[] state;
};