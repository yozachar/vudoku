# Vudoku - A Visual Sudoku Solver

> Final year project

<a href="https://gitmoji.dev">
  <img src="https://img.shields.io/badge/gitmoji-%20😎-FFDD67.svg?style=flat-square" alt="Gitmoji">
</a>

This project aims to solve 9x9 sudoku squares using computer vision techniques.

## Sudoku

- Sudoku is a mathematical puzzle.
- Regular or a common sudoku is a 9x9 grid split into 9 sub squares with sparse entries.

```text
╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗
║ 8 │ 5 │   ║   │   │ 2 ║ 4 │   │   ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║ 7 │ 2 │   ║   │   │   ║   │   │ 9 ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║   │   │ 4 ║   │   │   ║   │   │   ║
╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣
║   │   │   ║ 1 │   │ 7 ║   │   │ 2 ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║ 3 │   │ 5 ║   │   │   ║ 9 │   │   ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║   │ 4 │   ║   │   │   ║   │   │   ║
╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣
║   │   │   ║   │ 8 │   ║   │ 7 │   ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║   │ 1 │ 7 ║   │   │   ║   │   │   ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║   │   │   ║   │ 3 │ 6 ║   │ 4 │   ║
╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝
```

- The goal is to fill the gird with numbers from 1 to 9
- To solve tt has three simple rules:
  - No repetition along a row
  - No repetition along a column
  - No repetition within a sub square

Asking a computer to solve it requires translating Sudoku into code. For start we can represent sudo as a linear array like so:

```py
sudoku_linear = [ 8,  5, '', '', '',  2,  4, '', '',  7,  2, '', '', '', '', '', '',  9, '', '',  4, '', '', '', '', '', '', '', '', '',  1, '',  7, '', '',  2,  3, '',  5, '', '', '',  9, '', '', '',  4, '', '', '', '', '', '', '', '', '', '', '',  8, '', '',  7, '', '',  1,  7, '', '', '', '', '', '', '', '', '', '',  3,  6, '',  4, '']

sudoku_linear[76] # 6
```

This is a very messy way to represent sudoku 😖. Linear arrays increases the time complexity of the program. Let's try the 2D arrays:

```py
sudoku_2d = [
   #  0   1   2   3   4   5   6   7   8
    [ 8,  5, '', '', '',  2,  4, '', ''], #0
    [ 7,  2, '', '', '', '', '', '',  9], #1
    ['', '',  4, '', '', '', '', '', ''], #2
    ['', '', '',  1, '',  7, '', '',  2], #3
    [ 3, '',  5, '', '', '',  9, '', ''], #4
    ['',  4, '', '', '', '', '', '', ''], #5
    ['', '', '', '',  8, '', '',  7, ''], #6
    ['',  1,  7, '', '', '', '', '', ''], #7
    ['', '', '', '',  3,  6, '',  4, '']  #8
]

sudoku_2d[4][2] # 5
```

Not bad, but to get something more efficient let's call NumPy's [ndarrays](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html) and [Compressed Sparse Row](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csr_matrix.html#scipy.sparse.csr_matrix) from SciPy for help. We'll use a 3D NumPy array. The `x` and `y` axes will locate a cell and `z` axis will store all the probable values for that cell. We'll also use CSR from SciPy to make it memory efficient.

```py
sudoku = scipy.sparse.csr_matrix(numpy.ndarray(shape=(9,9,), buffer=numpy.array(sudoku_2d)))
```
