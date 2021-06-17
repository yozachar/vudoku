import numpy as np


class SudokuSolver:
    def __init__(self):
        self.board = None

    def solveRecursively(self, board):

        cell = self.isEmptyCell(self.board)

        if not cell:
            return True
        else:
            row, col = cell

        for sol in range(1, 10):
            if self.isValid(self.board, sol, (row, col)):
                self.board[row, col] = sol
                if self.solveRecursively(self.board):
                    return True
            self.board[row, col] = 0

        return False

    def isValid(self, board, num, pos):
        # check row
        if num in self.board[pos[0]]:
            return False
        # check column
        if num in self.board[..., pos[1]]:
            return False

        swapped = np.swapaxes(np.reshape(
            self.board, (3, 3, 3, 3)), 1, 2).reshape(9, 9)

        x = (pos[0] // 3) * 3 + 3
        y = (pos[1] // 3) * 3 + 3
        z = 0

        print(x, y)

        if x == 3:
            if y == 3:
                z = 0
            elif y == 6:
                z = 1
            else:
                z = 2
        elif x == 6:
            if y == 3:
                z = 3
            elif y == 6:
                z = 4
            else:
                z = 5
        else:
            if y == 3:
                z = 6
            elif y == 6:
                z = 7
            else:
                z = 8

        print(swapped[z])
        if num in swapped[z]:
            return False

        return True

    def isEmptyCell(self, board):
        for idx in range(len(self.board)):
            for jdx in range(len(self.board[0])):
                if self.board[idx, jdx] == 0:
                    return (idx, jdx)  # row, col
        return None

    def gateway(self, string='780400120600075009000601078007040260001050930904060005070300012120007400049206007'):
        self.board = np.array(list(string), dtype=np.int32).reshape(9, 9)
        # print(self.board, end="**\n")
        self.solveRecursively(self.board)
        return self.board


slr = SudokuSolver()
print(slr.gateway())
