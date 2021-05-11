class ValidateDimensions:
    def __init__(self, grid):
        self.grid = test_grid if not grid else grid

    def dimension_checker(self) -> bool:
        for row in self.grid:
            if len(row) != 9:
                return False

        for column in zip(*self.grid):
            if len(column) != 9:
                return False

        return True


class ValidateSolution:

    def __init__(self, grid):
        self.sol_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        self.grid = test_grid if not grid else grid

    def solution_checker(self) -> bool:
        for row in self.grid:
            if set(row) != self.sol_set:
                return False

        for column in zip(*self.grid):
            if set(column) != self.sol_set:
                return False

        for idx in (0, 3, 6):
            for jdx in (0, 3, 6):
                kdx = jdx + 3
                if set(self.grid[idx][jdx:kdx] + self.grid[idx+1][jdx:kdx] + self.grid[idx+2][jdx:kdx]) != self.sol_set:
                    return False

        return True


test_grid = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
             [4, 5, 6, 7, 8, 9, 1, 2, 3],
             [7, 8, 9, 1, 2, 3, 4, 5, 6],
             [2, 3, 1, 5, 6, 4, 8, 9, 7],
             [5, 6, 4, 8, 9, 7, 2, 3, 1],
             [8, 9, 7, 2, 3, 1, 5, 6, 4],
             [3, 1, 2, 6, 4, 5, 9, 7, 8],
             [6, 4, 5, 9, 7, 8, 3, 1, 2],
             [9, 7, 8, 3, 1, 2, 6, 4, 5]]


'''
Try pandas later...

import pandas as pd

df = pd.DataFrame(test_grid)

for idx in range(9):
    print(df.iloc[idx:idx+1, 0:])
    print()
    print(df.iloc[0:, idx:idx+1])
    print("\n -- \n")

for idx in range(0,9,3):
    for idy in range(0,9,3):
        print(df.iloc[idx:idx+3, idy:idy+3], end='\n\n')
    print("\n --- \n")
'''