# This the project entry point
'''
The project path is laid out as follows:

Video Input --> Sudoku Grabber -->  Solver --> Visualizer
'''

from scavenger import sr, cv
from extractor import de, np, Image
from solver import SudokuSolver

import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase

isSolved = False
bw_sdk = p_string = s_board = None

st.title("Vudoku")

col1, col2 = st.beta_columns(spec=2)

class Receiver(VideoProcessorBase):

    def transform(self, frame):
        image = frame.to_ndarray(format='bgr24')
        
        yield image # need to work on generators

        bw_sdk = sr.relay(image=image)  # returns a black and white sudoku grid
        p_string = de.miner(image=bw_sdk)  # returns a 81 bit string
        ss = SudokuSolver(string=p_string)
        isSolved, s_board = ss.solveRecursively()  # returns puzzle status and 
        # print(s_board) # convert this to an image

        if isSolved:
            return s_board


with col1:
    st.header(body='Input')
    webrtc_streamer(key='Output', video_transformer_factory=Receiver)

with col2:
    st.header(body='Output')
    result = cv.cvtColor(src=cv.imread(filename='src/sample/result.jpg'), code=cv.COLOR_BGR2RGB)
    st.image(image=result) # final image
