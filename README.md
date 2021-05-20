# Vudoku - A Visual Sudoku Solver

[![Gitmoji](https://img.shields.io/badge/gitmoji-%20😎-FFDD67.svg)](https://gitmoji.dev)
[![Status](https://img.shields.io/badge/Project%20Completed-85%25-orange)](https://github.com/joe733/vudoku)

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

This project aims to solve 9x9 sudoku squares using computer vision techniques. So here's the basic idea.

1. The system gets a video / image as input.
2. It scans the input and tries to detect a grid which gets saved.
3. The grid is then split into cells.
4. Each cell is parsed to get the data in it which is either `None` or `digit`.
5. After retriving the numbers it's then given to the solver in string format.
6. The solver finds a solution and

Asking a computer to solve it requires translating Sudoku into code. This can be achieved in many ways, linear arrays, encoded and decoded strings, two dimensional arrays etc.
