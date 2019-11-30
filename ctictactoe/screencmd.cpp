#include <iostream>
#include "screencmd.h"

void printWelcome(){
  resetScreen();
  std::cout << "==========================" << std::endl;
  std::cout << "    Tic Tac Toe 3000!" << std::endl;
  std::cout << std::endl;
  std::cout << "Game Configuration" << std::endl;
  return;
}

void getUserInput(char* buf){
  std::cin >> buf;
  return;
}

void resetScreen(){
  std::system("clear");
  return;
}