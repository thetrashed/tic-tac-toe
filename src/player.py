import math


class Player:
    def __init__(self, symbol, board, isHuman=True):
        self.__ttcBoard = board
        self.__symbol = symbol
        self.__isHuman = isHuman

    def getSymbol(self):
        return self.__symbol

    def move(self, mouse_pos, swidth, sheight):
        block_width = swidth / 3
        block_height = sheight / 3

        index1 = int(mouse_pos[0] / block_width)
        index2 = int(mouse_pos[1] / block_height)

        if (
            self.__ttcBoard.board[index1, index2] == 0
            and self.__ttcBoard.board[index1, index2] != self.__symbol
        ):
            self.__ttcBoard.board[index1, index2] = self.__symbol

    def __str__(self):
        return "Player is " + ("Human" if self.__isHuman else "not Human")
