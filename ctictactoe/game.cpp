#include "game.h"
#include "screencmd.h"
#include <iostream>
#include <string>

using namespace std;

// Default Constructor 
Game::Game(){
    player_letters[0]= 'X';
    player_letters[1] = 'O';
    board_size = 3;
    connect_to_win = 3;
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
