import numpy as np

input_representation = '003000000400000020080120006000000000200060007000807031010640900605008000908300040'
sudoku_puzzle = np.array(list(input_representation),
                         dtype=np.int32).reshape(9, 9)

if len(input_representation) != 81:
    print('Nope')


def solveRecursively(board):
    cell = isEmptyCell(board)
    if not cell:
        return True
    else:
        row, col = cell

    for sol in range(1,10):
        if isValid(board, sol, (row, col)):
            board[row][col] = sol

            if solveRecursively(board):
                return True

            board[row][col] = 0

    return False


def isValid(board, num, pos):
    # check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False

    return True


def isEmptyCell(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # row, col

    return None


print(solveRecursively(sudoku_puzzle))