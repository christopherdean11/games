#include <iostream>
#include "screencmd.h"

void getUserInput(char* buf){
  std::cin >> buf;
  return;
}

void resetScreen(){
  std::system("clear");
  return;
}