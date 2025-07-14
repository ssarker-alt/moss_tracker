#include <iostream>
#include "Board.hpp"

using namespace std;

int main() {
    char type;
    cout << "Enter a type (E/F/G): ";
    cin >> type;

    Board *game;

    if (type == 'E') {
        game = new Board;
        game->grid[0].push_back(2);
        game->grid[0].push_back(1);
        game->grid[1].push_back(2);
        game->grid[1].push_back(1);
        game->grid[2].push_back(2);
        game->grid[2].push_back(1);
        game->grid[3].push_back(2);
        game->display();
    }
    else if (type == 'F') {
        game = new Board;
        game->grid[0].push_back(0);
        game->grid[1].push_back(3);
        game->grid[0].push_back(0);
        game->grid[1].push_back(3);
        game->grid[0].push_back(0);
        game->grid[1].push_back(3);
        game->grid[3].push_back(0);
        game->grid[1].push_back(3);
        game->display();
    }
    else if (type == 'G') {
        game = new Board;
        int bin = game->add(0); // Player 0
        int bin2 = game->add(1); // Player 1

        cout << "The layout of the bins are as follows." << endl;
        for (int i = 0; i < game->numBins; i++) {
            if (game->grid[i].size() == 0)
                cout << "empty" << endl;
            else {
                for (int j = 0; j < game->grid[i].size(); j++)
                    cout << game->grid[i][j] << " ";
                cout << endl;
            }
        }
    }

    return 0;
}



