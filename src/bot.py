import numpy as np
import random
import copy


def makeMove(index1, index2, ttcBoard, symbol):
    ttcBoard.moves.append([index1, index2])
    ttcBoard.board[index1, index2] = symbol


class RandomBot:
    def __init__(self, ttcBoard, symbol):
        self.__ttcBoard = ttcBoard
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
    def __init__(self, ttcBoard, symbol):
        self.__ttcBoard = ttcBoard
        self.__symbol = symbol

    def move(self):
        choices = np.argwhere(self.__ttcBoard.board == 0)

        for i in range(len(choices)):
            index1, index2 = choices[i]

            newboard = copy.deepcopy(self.__ttcBoard)
            makeMove(index1, index2, newboard, self.__symbol)

            if newboard.hasWinner() == self.__symbol:
                makeMove(index1, index2, self.__ttcBoard, self.__symbol)

        try:
            index1, index2 = random.choice(choices)
            makeMove(index1, index2, self.__ttcBoard, self.__symbol)
        except:
            return

    def getSymbol(self):
        return self.__symbol


class TwoLayerBot:
    def __init__(self, ttcBoard, symbol):
        self.__ttcBoard = ttcBoard
        self.__symbol = symbol

    def move(self):
        losing_move = None
        first_choices = np.argwhere(self.__ttcBoard.board == 0)
        for i in range(len(first_choices)):
            index1, index2 = first_choices[i]
            newBoard1 = copy.deepcopy(self.__ttcBoard)

            makeMove(index1, index2, newBoard1, self.__symbol)
            if newBoard1.hasWinner() == self.__symbol:
                makeMove(index1, index2, self.__ttcBoard, self.__symbol)
                return

            second_choices = np.argwhere(newBoard1.board == 0)
            other_symbol = -1 if self.__symbol == 1 else 1
            for j in range(len(second_choices)):
                ix1, ix2 = second_choices[j]
                newBoard2 = copy.deepcopy(newBoard1)
                makeMove(ix1, ix2, newBoard2, other_symbol)
                if newBoard2.hasWinner() == other_symbol:
                    losing_move = (ix1, ix2)

        if losing_move != None:
            makeMove(losing_move[0], losing_move[1], self.__ttcBoard, self.__symbol)
            return

        index1, index2 = random.choice(first_choices)
        makeMove(index1, index2, self.__ttcBoard, self.__symbol)

    def getSymbol(self):
        return self.__symbol


class Choice:
    def __init__(self, move, value, depth):
        self.move = move
        self.value = value
        self.depth = depth

    def __str__(self):
        return str(self.move) + ": " + str(self.value)


class MiniMaxBot:
    def __init__(self, ttcBoard, symbol):
        self.__ttcBoard = ttcBoard
        self.__symbol = symbol

    def minimax(self, ttcBoard, is_max, player_symbol, depth):
        winner = ttcBoard.hasWinner()
        other_player = 1 if self.__symbol == -1 else -1
        if winner == self.__symbol:
            return Choice(ttcBoard.getLastMove(), 10 - depth, depth)
        elif winner == other_player:
            return Choice(ttcBoard.getLastMove(), -10 + depth, depth)
        elif ttcBoard.boardFull():
            return Choice(ttcBoard.getLastMove(), 0, depth)

        candidate_choices = []
        choices = np.argwhere(ttcBoard.board == 0)
        for choice in choices:
            row, col = choice
            newBoard = copy.deepcopy(ttcBoard)
            makeMove(row, col, newBoard, player_symbol)
            result = self.minimax(
                newBoard, not is_max, 1 if player_symbol == -1 else -1, depth + 1
            )
            result.move = newBoard.getLastMove()
            candidate_choices.append(result)

        max_choice = None
        max_value = -100
        min_choice = None
        min_value = 100

        for choice in candidate_choices:
            if is_max and choice.value > max_value:
                max_choice = choice
                max_value = choice.value
            elif not is_max and choice.value < min_value:
                min_choice = choice
                min_value = choice.value

        if is_max:
            return max_choice
        else:
            return min_choice

    def move(self):
        best_move = self.minimax(self.__ttcBoard, True, self.__symbol, 0)
        makeMove(best_move.move[0], best_move.move[1], self.__ttcBoard, self.__symbol)
