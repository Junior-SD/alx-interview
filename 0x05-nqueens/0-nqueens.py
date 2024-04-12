#!/usr/bin/python3
"""Nqueens solution
"""

import sys


def checks(n):
    """performs extra checks for N
    """
    if len(n) != 2:
        print('Usage: nqueens N')
        exit(1)

    try:
        int(n[1])
    except ValueError:
        print('N must be a number')
        exit(1)

    n = int(n[1])

    if n < 4:
        print('N must be at least 4')
        exit(1)

    return n


def solver(board, row, n):
    """Solver implementation
    """
    DATASET = {}
    count = 0
    my_list = []
    if row == n:
        for i in range(n):
            DATASET[i] = board[i]
        # print(DATASET)
        for k, v in DATASET.items():
            for index, item in enumerate(v):
                if item == 1:
                    my_list.append([k, index])
        print(my_list)

        return
    for col in range(n):
        if safe(board, row, col, n):
            board[row][col] = 1
            solver(board, row + 1, n)
            board[row][col] = 0


def safe(board, row, col, n):
    """chcek if the board is safe
    """
    for i in range(row):
        if board[i][col] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False
    return True


def nqueen(n):
    """Implementation
    """
    n = checks(n)
    board = [[0] * n for i in range(n)]
    solver(board, 0, n)


if __name__ == '__main__':
    n = sys.argv
    nqueen(n)
