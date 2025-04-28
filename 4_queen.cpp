#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<vector<string>>ans;
    int N;
    bool isSafe(vector<string>& board, int row, int col) {
        // Check upwards
        for (int i = row;i >= 0;i--) {
            if (board[i][col] == 'Q') return false;
        }
        // Check upward-left
        for (int i = row, j = col;i >= 0 && j >= 0;i--, j--) {
            if (board[i][j] == 'Q') return false;
        }
        // Check upward-right
        for (int i = row, j = col;i >= 0 && j < N;i--, j++) {
            if (board[i][j] == 'Q') return false;
        }
        return true;
    }
    void solve(vector<string>& board, int row) {
        if (row == N) {
            ans.push_back(board);
            return;
        }
        for (int col = 0;col < N;col++) {
            if (isSafe(board, row, col)) {
                board[row][col] = 'Q';
                solve(board, row + 1);
                board[row][col] = '.';
            }
        }
    }
    vector<vector<string>> solveNQueens(int n) {
        if (n == 0) return {};
        N = n;
        vector<string>board(n, string(n, '.'));
        solve(board, 0);
        return ans;
    }
};

void printBoard(const vector<string>& board) {
    for (const string& row : board) {
        cout << row << endl;
    }
    cout << endl;
}

int main() {
    // Create a Solution object
    Solution solution;

    // Ask user for board size
    int n;
    cout << "Enter the size of the chessboard (n): ";
    cin >> n;

    // Solve the N-Queens problem
    vector<vector<string>> results = solution.solveNQueens(n);

    // Display the results
    cout << "\nFound " << results.size() << " solutions for " << n << "-Queens problem:\n\n";

    int solutionNum = 1;
    for (int i = 0; i < results.size(); i++) {
        cout << "Solution " << solutionNum++ << ":\n";
        printBoard(results[i]);
    }

    return 0;
}
