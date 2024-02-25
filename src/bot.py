import numpy as np
import random
import copy


class RandomBot:
    def __init__(self, board, symbol):
        self.__ttcBoard = board
        self.__symbol = symbol

    def move(self):
        choices = np.argwhere(self.__ttcBoard.board == 0)
        try:
            i, j = random.choice(choices)
        except:
            return
        self.__ttcBoard.board[i, j] = self.__symbol

    def getSymbol(self):
        return self.__symbol


class OneLayerBot:
    def __init__(self, board, symbol):
        self.__ttcBoard = board
        self.__symbol = symbol

    def move(self):
        choices = np.argwhere(self.__ttcBoard.board == 0)

        for i in range(len(choices)):
            j, k = choices[i]

            newboard = copy.deepcopy(self.__ttcBoard)
            self.makeMove(j, k, newboard)

            if newboard.hasWinner():
                self.makeMove(j, k, self.__ttcBoard)

        try:
            j, k = random.choice(choices)
            self.makeMove(j, k, self.__ttcBoard)
        except:
            return

    def makeMove(self, index1, index2, board):
        board.board[index1, index2] = self.__symbol

    def getSymbol(self):
        return self.__symbol
