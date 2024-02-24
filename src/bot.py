import numpy as np
import random


def botMove(board, player):
    symbol = player.getSymbol()

    if 0 not in board.board:
        return

    while True:
        i = random.randint(0, 2)
        j = random.randint(0, 2)
        if board.board[i, j] == 0:
            break

    board.board[i, j] = symbol
