# This the project entry point
'''
The project path is laid out as follows:

Video Input --> Sudoku Grabber -->  Solver --> Visualizer
'''

from scavenger import sr
from extractor import de, np
from solver import SudokuSolver

import streamlit as st
from webcam import webcam

image = webcam()
isSolved = False
bw_sdk = p_string = s_board = None

st.title("Vudoku")


if image is None:
    st.write("Waiting for capture...")
else:
    st.write("Got an Image")
    image = np.asarray(image)
    bw_sdk = sr.relay(image=image)  # returns a black and white sudoku grid
    p_string = de.miner(image=bw_sdk)  # returns a 81 bit string
    ss = SudokuSolver(string=p_string)
    isSolved, s_board = ss.solveRecursively()  # returns puzzle status

print(s_board)


# from streamlit_webrtc import webrtc_streamer, VideoProcessorBase

# col1, col2 = st.beta_columns(spec=2)
# dummy checker box

# class Receiver(VideoProcessorBase):

#     def transform(self, frame):
#         global output
#         image = frame.to_ndarray(format='bgr24')
#         # scv.img = img
#         # img = cv.cvtColor(cv.Canny(img, 100, 200), cv.COLOR_GRAY2BGR)
#         # output = scv.sr.relay(image=image)
#         return image
#         # return scv.result


# with col1:
#     st.title('Input')
#     webrtc_streamer(key='Input')

# with col2:
#     st.title('Output')
#     webrtc_streamer(key='Output', video_transformer_factory=Receiver)
