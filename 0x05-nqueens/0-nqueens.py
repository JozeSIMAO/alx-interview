#!/usr/bin/python3
"""N queens puzzle solution"""
import sys


def is_safe(board, row, col, N):
    """
    Check if it's safe to place a queen at board[row][col]
    """
    # Check this row on left side
    for i in range(col):
        if board[row][i]:
            return False
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False
    # Check lower diagonal on left side
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j]:
            return False
    return True


def solve_nqueens_util(board, col, N, res):
    """
    A recursive utility function to solve N queens problem
    """
    # If all queens are placed, then add solution to res
    if col == N:
        res.append([[i, row] for i, row in enumerate(board)])
        return True
    # Initialize current column as unsafe
    for i in range(N):
        if is_safe(board, i, col, N):
            # Place this queen in board[i][col]
            board[i][col] = 1
            # recur to place rest of the queens
            solve_nqueens_util(board, col + 1, N, res)
            # If placing queen in board[i][col] doesn't lead to a solution
            # then remove queen from board[i][col]
            board[i][col] = 0
    return False


def solve_nqueens(N):
    """
    Solve N queens problem
    """
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [[0] * N for _ in range(N)]
    res = []
    solve_nqueens_util(board, 0, N, res)
    for solution in res:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
        solve_nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
