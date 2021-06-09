# Vudoku - A Visual Sudoku Solver

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/joe733/vudoku/main/src/main.py)
[![Status](https://img.shields.io/badge/Project%20Completed-95%25-brightgreen)](https://github.com/joe733/vudoku)
[![Streamlit](https://img.shields.io/badge/Streamlit-0.82.0-blue)](https://github.com/streamlit/streamlit/)
[![Streamlit](https://img.shields.io/badge/Keras-2.4.3-blue)](https://github.com/opencv/opencv-python)
[![Streamlit](https://img.shields.io/badge/PythonOpenCV-4.5.2-blue)](https://github.com/opencv/opencv-python)
[![Git-emoji](https://img.shields.io/badge/Gitmoji-%20😎-FFDD67.svg)](https://gitmoji.dev)
[![CodeSize](https://img.shields.io/github/languages/code-size/joe733/vudoku?color=red&label=Code%20Size)](https://github.com/joe733/vudoku)

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

## How to test

The application has been deployed. Please visit [Streamlit Share](https://share.streamlit.io/joe733/vudoku/main/src/main.py).

- Meanwhile you can clone the repository
- Open the directory. `cd vudoku`
- Create a conda environment `conda env create -f src/environment.yml`
- Open terminal in the root of the clone repository and run `streamlit run src/main.py`
- It should automatically redirect you to the browser, if not open the browser and go to [`https://localhost:8501`](http://localhost:8501/)

## Current UI

![InitialUI](src/assets/images/screens/initial_ui.png)

## Task List

- [X] Get input frames from still images or video capture
- [X] Preprocess image, prep it to extract Sudoku grid
- [X] Grab the Sudoku box using contours of the maximum area
- [ ] Rectify flipped images after perspective transform
- [X] Split the grid into Sudoku boxes to extract digits
- [X] ~~Train a logistic regression classifier on MNIST data set - current random accuracy is around `91%`~~
- [X] Build and Train a keras Sequential Model (2 x Conv2D + MaxPool2D + Dropout + Flatten + Dense[ReLu] Dropout + Dense[SoftMax])
- [ ] Work on improving sudoku grabbing quality
  - [X] Get the digits recognized correctly
  - [ ] Preprocess the image (of a single digit) to remove excess / thick border
  - [ ] Scale and center the image
  - [X] ~~If nothing works, try a different solver or even another classifier.~~
  - [X] Encode the classified image into a 81 bit string
- [X] Solve the Sudoku using simple backtracking
- [X] ~~Additional module just to validate solved sudoku~~
- [X] Restructure the code and add a logical connections and control flow
- [X] Adds Streamlit GUI support
- [X] Deployed on Streamlit

### Extras

- [ ] Good to have a solid CLI interface
- [ ] Improve the number detection and grid splitting algorithm
- [X] ~~Host it on services like [PythonAnywhere](https://www.pythonanywhere.com/) / [Streamlit](https://streamlit.io/)~~

> **NB**: *If you find anything in this repositry that is not properly cited please let me know, I'm be more than happy to rectify it.*
