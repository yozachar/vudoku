import numpy as np


class SudokuSolver:
    def __init__(self):
        self.board = None

    def solveRecursively(self):
        cell = self.isEmptyCell()
        if not cell:
            return True, self.board
        else:
            row, col = cell
        for sol in range(1, 10):
            if self.isValid(sol, (row, col)):
                self.board[row][col] = sol
                if self.solveRecursively():
                    return True, self.board
                self.board[row][col] = 0
        return False, None

    def isValid(self, num, pos):
        # check row
        for idx in range(len(self.board[0])):
            if self.board[pos[0]][idx] == num and pos[1] != idx:
                return False
        # check column
        for jdx in range(len(self.board)):
            if self.board[jdx][pos[1]] == num and pos[0] != jdx:
                return False
        # check box
        box_x = pos[1] // 3
        box_y = pos[0] // 3
        for idx in range(box_y*3, box_y*3 + 3):
            for jdx in range(box_x*3, box_x*3 + 3):
                if self.board[idx][jdx] == num and (idx, jdx) != pos:
                    return False
        return True

    def isEmptyCell(self):
        for idx in range(len(self.board)):
            for jdx in range(len(self.board[0])):
                if self.board[idx][jdx] == 0:
                    return (idx, jdx)  # row, col
        return None

    def gateway(self, string='003000000400000020080120006000000000200060007000807031010640900605008000908300040'):
        self.board = np.array(list(string), dtype=np.int32).reshape(9, 9)
        return self.solveRecursively()


slr = SudokuSolver()
