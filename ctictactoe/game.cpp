#include "game.h"
#include <iostream>
#include <string>

using namespace std;

// Default Constructor
Game::Game(){
    player_letters[0]= 'X';
    player_letters[1] = 'O';
}


void Game::configureGame(){
    cout << "Use custom player letters? y/[n]: ";
    string resp;
    getline(cin, resp);
    if (resp == "y"){
        cout << "\nPlayer 1, enter your letter: ";
        cin >> player_letters[0];
        cout << "\nPlayer 2, enter your letter: ";
        cin >> player_letters[1];
    }
    return;
}