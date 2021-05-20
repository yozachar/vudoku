# Vudoku - A Visual Sudoku Solver

[![Gitmoji](https://img.shields.io/badge/gitmoji-%20😎-FFDD67.svg)](https://gitmoji.dev)
[![Status](https://img.shields.io/badge/Project%20Completed-85%25-orange)](https://github.com/joe733/vudoku)

## Sudoku

- Sudoku is a mathematical puzzle.
- Regular or a common Sudoku is a 9x9 grid split into 9 sub squares with sparse entries.

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

This project aims to solve 9x9 Sudoku squares using computer vision techniques. So here's the basic idea.

1. The system gets a video / image as input.
2. It scans the input and tries to detect a grid which gets saved.
3. The grid is then split into cells.
4. Each cell is parsed to get the data in it which is either `None` or `digit`.
5. After retrieving the numbers it's then given to the solver in string format.
6. The solver finds a solution and returns it to be displayed later.

Asking a computer to solve it requires translating Sudoku into code. This can be achieved in many ways, linear arrays, encoded and decoded strings, two dimensional arrays etc. This project uses simple string expression.

## Task List

- [X] Get input frames from still images or video capture.
- [X] Preprocess image, prep it to extract Sudoku grid.
- [X] Grab the Sudoku box using contours of the maximum area.
- [ ] Rectify flipped images after perspective transform.
- [X] Split the grid into Sudoku boxes to extract digits.
- [X] Train a logistic regression classifier on MNIST data set. Current random accuracy is `91%`.
- [ ] Get the digits recognized correctly.
  - [ ] Preprocess the image (of a single digit) to remove excess / thick border.
  - [ ] Scale and center the image.
  - [ ] If nothing works, try a different solver or even another classifier.
  - [ ] Encode the classified image into a 81 bit string.
- [X] Solve the Sudoku using simple backtracking
- [X] Additional module just to validate solved sudoku
- [ ] Restructure the code and add a logical connections and control flow

### Extras

- [ ] Good to have a solid CLI and GUI interface
- [ ] Improve the grid and number detection algorithm
- [ ] Host it on services like [PythonAnywhere](https://www.pythonanywhere.com/) / [Streamlit](https://streamlit.io/)
