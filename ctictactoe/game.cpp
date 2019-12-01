#include "game.h"
#include "screencmd.h"
#include <iostream>
#include <string>

using namespace std;

// Default Constructor 
Game::Game(){
    num_players = 2;
    player_letters[0]= 'X';
    player_letters[1] = 'O';
    board_size = 3;
    connect_to_win = 3;
    current_player = 1;
    winner = 0;
}

// Print welcome message to screen
void Game::printWelcome(){
    resetScreen();
    std::cout << "==========================" << std::endl;
    std::cout << "    Tic Tac Toe 3000!" << std::endl;
    std::cout << std::endl;
    std::cout << "Game Configuration" << std::endl;
    return;
}

// Customize cout << operator for this class
ostream & operator << (ostream& out, const Game  &g){
    out << "Game Setup: \n";
    out << "Player 1: " << g.player_letters[0] << "\n" ;
    out << "Player 2: " << g.player_letters[1] << std::endl;
    out << "Board Size: " << g.board_size << std::endl;;
    out << "Run Length to Win: "  << g.connect_to_win << std::endl;
    return out;
}

// Configure game object with user input
void Game::configureGame(){
    cout << "Use custom player letters? y/[n]: ";
    string resp;
    getline(cin, resp);
    if (resp == "y"){
        string buf;
        cout << "\nPlayer 1, enter your letter: ";
        getline(cin, buf);
        player_letters[0] = buf[0];
        cout << "\nPlayer 2, enter your letter: ";
        getline(cin, buf);
        player_letters[1] = buf[0];
    }

    cout << "What board size? [3]: ";
    getline(cin, resp);
    if (resp.empty()){
        board_size = 3;
    }else{
        board_size = stoi(resp);
    }
    cout << "How many to connect to win? [3]: ";
    getline(cin, resp);
    if (resp.empty()){
        connect_to_win = 3;
    }else{
        connect_to_win = stoi(resp);
    }

    return;
}

void Game::getNextMove(int* move_out){
    cout << "Player " << current_player << ", enter a move: ";
    string buf;
    getline(cin, buf);
    parseMove(buf, move_out);
    return;
}

void Game::parseMove(string move_in, int* move_out){
    // input in form A1
    // convert to 0,0
    int row, col;
    col = move_in[0]; // A in A1
    row = move_in[1]; // 1 in A1
    move_out[0] = row - '0' - 1;
    move_out[1] = col - 'A';
    return;
}

void Game::updateBoard(Board *board, int* move){
    board->updateState(move[0], move[1], current_player);
    return;
}

void Game::updateCurrentPlayer(){
    current_player++;
    if (current_player > num_players){
        current_player = 1;
    }
    return;
}

void Game::tick(Board *board){
    resetScreen();
    int players[2] = {1,2};
    int move[2] = {0,0};
    // TODO: change printBoard to not need players array
    board->printBoard(num_players, players, player_letters);
    getNextMove(move);
    updateBoard(board, move);
    updateCurrentPlayer();
    return;
}

bool Game::isOver(Board *board){
    int segment[board_size];
    // Check each row
    for (int i = 0; i < board_size; i++){
        for (int j = 0; j < board_size; j++){
            segment[j] = board->state[board_size*i + j];
        }
        if (segmentHasWinner(segment)){
            return true;
        }
    }
    // check each column
    for (int i = 0; i < board_size; i++){
        for (int j = 0; j < board_size; j++){
            segment[j] = board->state[board_size*j + i];
        }
        if (segmentHasWinner(segment)){
            return true;
        }
    }

    // diagonal 1 - top left to bottom right, moving down
    for (int i = 0; i < board_size; i++){
        segment[i] = board->state[board_size*i + i];
        if (segmentHasWinner(segment)){
            return true;
        }
    }

    // diagonal 2 -  top right to bottom left
    for (int i = 0; i < board_size; i++){
        segment[i] = board->state[board_size-1-i + board_size*i];
        if (segmentHasWinner(segment)){
            return true;
        }
    }

    
    return false;
}

bool Game::segmentHasWinner(int *segment){
    // initialize count var, used to contain number of 
    // player[i] spots in a row on the board
    int count[num_players];
    for (int i = 0; i < num_players; i++){
        count[i] = 0;
    }

    // Loop over segment to look for a winner
    for (int i = 0; i < board_size; i++){
        // If element indicates player1, inc player1 count
        if ((segment[i] > 0) && (segment[i] == 1)){
            count[0]++;
        // If element is no move or is player2, reset count
        }else{
            count[0] = 0;
        }
        // If element indicates player2, inc player2 count
        if ((segment[i] > 0) && (segment[i] == 2)){
            count[1]++;
        // If element is no move or is player1, reset count
        }else{
            count[1] = 0;
        }

        // Check winner each loop
        // winner could be early if connect_to_win < board_size
        if (count[0] >= connect_to_win){
            winner = 1;
            break;
        }
        if (count[1] >= connect_to_win){
            winner = 2;
            break;
        }
    }
    return (winner > 0);
}

void Game::printWinner(){
    resetScreen();
    cout << "Player " << winner << " ( " << player_letters[winner-1] << " ) wins the game!" << endl;
}