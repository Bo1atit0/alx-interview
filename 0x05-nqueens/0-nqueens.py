#!/usr/bin/python3
import sys


def print_usage_error(msg):
    """Print error message and exit."""
    print(msg)
    sys.exit(1)


def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]."""
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solve_nqueens_util(board, col, solutions):
    """Use backtracking to find solutions."""
    if col == len(board):
        solution = [[i, row.index(1)] for i, row in enumerate(board)]
        solutions.append(solution)
        return

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            solve_nqueens_util(board, col + 1, solutions)
            board[i][col] = 0  # backtrack


def solve_nqueens(n):
    """Solve the N-Queens puzzle and print all solutions."""
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_nqueens_util(board, 0, solutions)
    for solution in solutions:
        print(solution)


def main():
    """Parse input, validate, and solve the N-Queens problem."""
    if len(sys.argv) != 2:
        print_usage_error("Usage: nqueens N")

    try:
        n = int(sys.argv[1])
    except ValueError:
        print_usage_error("N must be a number")

    if n < 4:
        print_usage_error("N must be at least 4")

    solve_nqueens(n)


if __name__ == "__main__":
    main()
