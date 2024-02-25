import numpy as np
import pygame as pg
import copy


class TTCBoard:
    def __init__(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.ended = False

    def drawBoard(self, screen, swidth, sheight):
        block_height = sheight / 3
        block_width = swidth / 3

        for i in range(0, 3):
            for j in range(0, 3):
                rect = pg.Rect(
                    i * block_width, j * block_height, block_width, block_height
                )

                if self.board[i][j] != 0:
                    self.drawCrossCirc(
                        i,
                        j,
                        screen,
                        i * block_width + block_width / 2,
                        j * block_height + block_height / 2,
                        min(block_width, block_height) / 2,
                    )

                pg.draw.rect(screen, "gray", rect, 1)

    def drawCrossCirc(self, index1, index2, screen, cx, cy, r):
        if self.board[index1, index2] == 1:
            pg.draw.line(screen, "gray", (cx - r, cy + r), (cx + r, cy - r), 1)
            pg.draw.line(screen, "gray", (cx - r, cy - r), (cx + r, cy + r), 1)
        else:
            pg.draw.circle(screen, "gray", (cx, cy), r, 1)

    def hasWinner(self):
        if (
            abs(sum(self.board[0])) == 3
            or abs(sum(self.board[1])) == 3
            or abs(sum(self.board[2])) == 3
        ):
            return True
        elif (
            abs(sum(self.board[:, 0])) == 3
            or abs(sum(self.board[:, 1])) == 3
            or abs(sum(self.board[:, 2])) == 3
        ):
            return True
        elif (
            abs(self.board[0, 0] + self.board[1, 1] + self.board[2, 2]) == 3
            or abs(self.board[0, 2] + self.board[1, 1] + self.board[2, 0]) == 3
        ):
            return True

        return False

    def __deepcopy__(self, memodict={}):
        dp = TTCBoard()
        dp.board = copy.deepcopy(self.board)
        return dp

    def __str__(self):
        return str(self.board)
