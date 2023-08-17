"""Solver."""

# standard
import itertools
from typing import Any

# external
import numpy as np


class SudokuSolver:
    """Sudoku Solver."""

    def __init__(self):
        """Initialize Solver."""
        self.board: np.ndarray[Any, np.dtype[np.int32]]

    def solve_recursively(self, board: np.ndarray[Any, np.dtype[np.int32]]):
        """Solve Recursively."""
        if cell := self.is_empty_cell(self.board):
            row, col = cell

        else:
            return True
        for sol in range(1, 10):
            if self.is_valid(self.board, sol, (row, col)):
                self.board[row, col] = sol
                if self.solve_recursively(self.board):
                    return True
            self.board[row, col] = 0

        return False

    def is_valid(self, board: np.ndarray[Any, np.dtype[np.int32]], num: int, pos: tuple[int, int]):
        """Is Valid?"""
        # check row
        if num in self.board[pos[0]]:
            return False
        # check column
        if num in self.board[..., pos[1]]:
            return False

        swapped = np.swapaxes(np.reshape(self.board, (3, 3, 3, 3)), 1, 2).reshape(9, 9)

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
        elif y == 3:
            z = 6
        elif y == 6:
            z = 7
        else:
            z = 8

        print(swapped[z])
        return num not in swapped[z]

    def is_empty_cell(self, board: np.ndarray[Any, np.dtype[np.int32]]):
        """Is Empty Cell?"""
        return next(
            (
                (idx, jdx)
                for idx, jdx in itertools.product(range(len(self.board)), range(len(self.board[0])))
                if self.board[idx, jdx] == 0
            ),
            None,
        )

    def gateway(
        self,
        string: str = "78040012060007500900060107800704026000105093"
        + "0904060005070300012120007400049206007",
    ):
        """Gateway."""
        self.board = np.array(list(string), dtype=np.int32).reshape(9, 9)
        # print(self.board, end="**\n")
        self.solve_recursively(self.board)
        return self.board.dtype


slr = SudokuSolver()
print(slr.gateway())
