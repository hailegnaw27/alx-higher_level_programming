#!/usr/bin/python3
"""
Solution to the N queens puzzle.
Usage: nqueens N
where N must be an integer greater or equal to 4
"""

import sys


def nqueens(N):
    """
    Solves the N queens puzzle.
    """

    def is_safe(board, row, col):
        """
        Determines if it is safe to place a queen at board[row][col].
        """

        # check the row on the left side
        for i in range(col):
            if board[row][i]:
                return False

        # check upper diagonal on left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j]:
                return False

        # check lower diagonal on left side
        for i, j in zip(range(row, N), range(col, -1, -1)):
            if board[i][j]:
                return False

        # it is safe to place a queen at board[row][col]
        return True

    def backtrack(board, col, solutions):
        """
        Tries to place a queen in a column col.
        """

        # base case: all queens have been placed
        if col == N:
            solutions.append([[row, board[row].index(1)] for row in range(N)])
            return solutions

        for row in range(N):
            if is_safe(board, row, col):
                # place the queen
                board[row][col] = 1
                # backtrack with the remaining columns
                backtrack(board, col + 1, solutions)
                # remove the queen
                board[row][col] = 0

        return solutions

    # check if the argument is an integer
    if not isinstance(N, int):
        print("N must be a number", file=sys.stderr)
        sys.exit(1)

    # check if the argument is greater or equal than 4
    if N < 4:
        print("N must be at least 4", file=sys.stderr)
        sys.exit(1)

    # create an empty board
    board = [[0 for x in range(N)] for y in range(N)]

    # find the solutions
    solutions = backtrack(board, 0, [])

    # print the solutions
    for sol in solutions:
        print(sol)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N", file=sys.stderr)
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        nqueens(N)
    except ValueError:
        print("N must be a number", file=sys.stderr)
        sys.exit(1)
