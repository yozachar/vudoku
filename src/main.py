# This the project entry point
'''
The project path is laid out as follows:

Video Input --> Sudoku Grabber -->  Solver --> Visualizer
'''

from artist import cap_img, Layout, st
from solver import SudokuSolver
from extractor import DigitExtractor, np
from scavenger import SudokuRecognizer, cv

isSolved = False
bw_sdk = p_string = s_board = None
image = cv.cvtColor(src=cv.imread(filename='src/assets/images/sample/result.jpg'), code=cv.COLOR_BGR2RGB)

lyt = Layout()
dex = DigitExtractor()
srg = SudokuRecognizer()

if lyt.capture:
    image = cap_img if cap_img else image

if lyt.edges or lyt.contours or lyt.transform:
    bw_sdk = srg.relay(image=image)  # returns a black and white sudoku grid

if lyt.solve:
    p_string = dex.miner(image=bw_sdk)  # returns a 81 bit string
    ss = SudokuSolver(string=p_string)
    isSolved, s_board = ss.solveRecursively()  # returns puzzle status and 
# print(s_board) # convert this to an image

lyt.sample = image
lyt.topCols()