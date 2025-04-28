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

def solve(board, row, n, solutions, target_count):
    if len(solutions) >= target_count:
        return  # here we made the change to get target solutions
    if row == n:
        solutions.append(["".join(r) for r in board])
        return
    for col in range(n):
        if isSafe(board, row, col, n):
            board[row][col] = 'Q'
            solve(board, row + 1, n, solutions, target_count)
            if len(solutions) >= target_count:
                return
            board[row][col] = '.'

def solveNQueens(n, target_count):
    if n == 0:
        return []
    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []
    solve(board, 0, n, solutions, target_count)
    return solutions

def printBoard(board):
    for row in board:
        print(row)
    print()

def main():
    n = int(input("Enter the size of the chessboard (n): "))
    k = int(input("Enter the number of solutions you want to see: "))

    results = solveNQueens(n, k)

    if results:
        print(f"\nFound {len(results)} solution(s) for {n}-Queens problem:\n")
        for idx, solution in enumerate(results, start=1):
            print(f"Solution {idx}:")
            printBoard(solution)
    else:
        print(f"No solution exists for {n}-Queens problem.")

if __name__ == "__main__":
    main()