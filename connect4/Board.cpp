
#include <iostream>
#include "Board.hpp"
#include <cstdlib>
#include <vector>

using namespace std;

Board::Board() : Board(6, 4) {}

Board::Board(int numBins, int capacity) {
    if (numBins < 5) numBins = 5;
    if (capacity < 4) capacity = 4;

    this->numBins = numBins;
    this->capacity = capacity;

    grid = vector<vector<int>>(this->numBins, vector<int>());
}

void Board::display() const {
    // Print the top border
    cout << "+";
    for (int col = 0; col < numBins; ++col) {
        cout << "--+";
    }
    cout << endl;

    // Iterate through each row from bottom to top (capacity-1 to 0)
    for (int row = capacity - 1; row >= 0; --row) {
        cout << "|";  // Start the row display
        
        // Iterate through each bin (column)
        for (int col = 0; col < numBins; ++col) {
            if (grid[col].size() > row) {
                int val = grid[col][row];
                // Map the value to the corresponding shape (using Unicode characters)
                if (val == 1) cout << "\033[31m⬟\033[0m";    // Red ball
                else if (val == 2) cout << "\033[34m◉\033[0m"; // Blue pentagon
                else if (val == 3) cout << "\033[31m⬤\033[0m"; // Red circle
                else if (val == 4) cout << "\033[34m⭔\033[0m"; // Blue empty pentagon
                else cout << " ";  // Empty space if no piece is there
            } else {
                cout << " ";  // Empty space
            }
            cout << " |";
        }
        cout << endl;

        // Print the row border
        cout << "+";
        for (int col = 0; col < numBins; ++col) {
            cout << "--+";
        }
        cout << endl;
    }

    // Print the index labels of the bins at the bottom
    cout << " ";
    for (int col = 0; col < numBins; ++col) {
        if (col < 10)
            cout << " " << col << " ";  // Single digit column index
        else
            cout << col << " ";        // Double digit column index
    }
    cout << endl;
}




int Board::add(int player) {
    int bin;
    cout << "Enter a bin index in [0, " << numBins << ") that is not full: ";
    while (true) {
        cin >> bin;
        if (bin < 0 || bin >= numBins) {
            cout << "invalid bin index, needs to be in [0, " << numBins << ")\n";
        } else if (grid[bin].size() >= capacity) {
            cout << "bin is full\n";
        } else {
            break;
        }
        cout << "Re-enter a bin index in [0, " << numBins << ") that is not full: ";
    }

    grid[bin].push_back(player); 
    return bin;
}


int Board::winInHorizontal(int bin) {
    return 0;  // Add logic for horizontal win check
}

int Board::winInVertical(int bin) {
    return 0;  // Add logic for vertical win check
}

int Board::winInDiagonal(int bin) {
    return 0;  // Add logic for diagonal win check
}

int Board::win(int bin) {
    return winInHorizontal(bin) || winInVertical(bin) || winInDiagonal(bin);
}

void Board::play() {
    // Add gameplay logic here
}










