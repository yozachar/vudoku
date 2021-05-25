import numpy as np


class SudokuSolver:
    def __init__(self, string='003000000400000020080120006000000000200060007000807031010640900605008000908300040'):
        self.board = np.array(list(string), dtype=np.int32).reshape(9, 9)

    def solveRecursively(self):
        cell = self.isEmptyCell()
        if not cell:
            # , ''.join(str(i) for i in self.board.flatten().tolist())
            return True
        else:
            row, col = cell
        for sol in range(1, 10):
            if self.isValid(sol, (row, col)):
                self.board[row][col] = sol
                if self.solveRecursively():
                    # , ''.join(str(i) for i in self.board.flatten().tolist())
                    return True
                self.board[row][col] = 0
        return False

    def isValid(self, num, pos):
        # check row
        for i in range(len(self.board[0])):
            if self.board[pos[0]][i] == num and pos[1] != i:
                return False
        # check column
        for i in range(len(self.board)):
            if self.board[i][pos[1]] == num and pos[0] != i:
                return False
        # check box
        box_x = pos[1] // 3
        box_y = pos[0] // 3
        for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x*3, box_x*3 + 3):
                if self.board[i][j] == num and (i, j) != pos:
                    return False
        return True

    def isEmptyCell(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == 0:
                    return (i, j)  # row, col
        return None


ss = SudokuSolver()
# print(ss.solveRecursively())