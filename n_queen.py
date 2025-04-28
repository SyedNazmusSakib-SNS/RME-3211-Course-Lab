def isSafe(board, row, col, n):
    # Check upwards
    for i in range(row - 1, -1, -1):
        if board[i][col] == 'Q':
            return False
    # Check upward-left
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1
    # Check upward-right
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1
    return True

def solve(board, row, n, solutions):
    #if row == n:
        #solutions.append(["".join(r) for r in board])
        #return
    for col in range(n):
        if isSafe(board, row, col, n):
            board[row][col] = 'Q'
            solve(board, row + 1, n, solutions)
            board[row][col] = '.'

def solveNQueens(n):
    if n == 0:
        return []
    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []
    solve(board, 0, n, solutions)
    return solutions

def printBoard(board):
    for row in board:
        print(row)
    print()

def main():
    n = int(input("Enter the size of the chessboard (n): "))
    results = solveNQueens(n)
    solutions = 1
    print(f"\nFound {len(results)} solutions for {n}-Queens problem:\n")
    for idx, solution in enumerate(results, start=1):
        print(f"Solution {idx}:")
        printBoard(solution)
    
if __name__ == "__main__":
    main()

