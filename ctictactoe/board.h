#include <string>

class Board{
    public:
        int *state;
        int size;
        std::string show;
        Board(int); // constructor
        ~Board();
};

