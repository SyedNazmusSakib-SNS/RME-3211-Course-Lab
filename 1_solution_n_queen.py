def isSafe(board, row, col, n):
    for i in range(row - 1, -1, -1):
        if board[i][col] == 'Q':
            return False
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1
    return True

def solve(board, row, n, solutions, found):
    if found[0]:
        return  # Stop if already found
    if row == n:
        solutions.append(["".join(r) for r in board])
        found[0] = True
        return
    for col in range(n):
        if isSafe(board, row, col, n):
            board[row][col] = 'Q'
            solve(board, row + 1, n, solutions, found)
            if found[0]:
                return  # Early exit after finding one
            board[row][col] = '.'

def solveNQueens(n):
    if n == 0:
        return []
    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []
    found = [False]  # Using list to modify inside recursion
    solve(board, 0, n, solutions, found)
    return solutions

def printBoard(board):
    for row in board:
        print(row)
    print()

def main():
    n = int(input("Enter the size of the chessboard (n): "))
    results = solveNQueens(n)

    if results:
        print(f"\nFound 1 solution for {n}-Queens problem:\n")
        printBoard(results[0])
    else:
        print(f"No solution exists for {n}-Queens problem.")

if __name__ == "__main__":
    main()