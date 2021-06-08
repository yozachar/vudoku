# This the project entry point
'''
The project path is laid out as follows:

Video Input --> Sudoku Grabber -->  Solver --> Visualizer
'''

from solver import slr
from builder import ibg
from extractor import dex, np
from scavenger import srg, cv

import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase

btn_pressed = False
capture_img = dilated_img = contour_img = flipped_img = None
sampled_img = cv.cvtColor(src=cv.imread(
    filename='src/assets/images/sample/sudoku04.jpg'), code=cv.COLOR_BGR2RGB)


st.markdown("<h1 style='text-align: center;'>Vudoku - Visual Sudoku Solver</h1>",
            unsafe_allow_html=True)


class Receiver(VideoProcessorBase):
    # Overridden class

    def transform(self, frame):
        # Overridden function
        global capture_img
        capture_img = frame.to_ndarray(format='bgr24')
        return capture_img


col1, col2 = st.beta_columns(spec=2)
with col1:
    # 1. Input
    st.header(body='Input')
    webrtc_streamer(key='Output', video_transformer_factory=Receiver)

with col2:
    # 5. Output
    st.header(body='Output')
    btn_pressed = st.button(label='Solve Sudoku')
    if btn_pressed:
        isSolved = False
        bw_sdk = p_board = p_string = None

        # returns a black and white sudoku grid
        bw_sdk = srg.relay(image=sampled_img)
        p_string = dex.miner(image=bw_sdk)
        print(len(p_string), p_string)
        isSolved, p_board = slr.gateway(
            string=p_string)  # returns a 81 bit string
        if isSolved:
            ibg.buildImage(p_board)

        p_board = cv.cvtColor(src=cv.imread(
            filename='src/assets/images/out/solution.jpg'), code=cv.COLOR_BGR2RGB)
        st.image(image=p_board)


col1, col2 = st.beta_columns(spec=2)
with col1:
    # 2. Capture image
    st.header('Captured Image')
    if btn_pressed:
        sampled_img = capture_img if capture_img else sampled_img
        st.image(image=sampled_img)

with col2:
    # 3. Detect Edges
    st.header('Detect Edges')
    if btn_pressed:
        dilated_img = cv.cvtColor(src=cv.imread(
            filename='src/assets/images/out/dilated.jpg'), code=cv.COLOR_BGR2RGB)
        st.image(image=dilated_img)


col1, col2 = st.beta_columns(spec=2)
with col1:
    # 3.Mark contour points
    st.header('Mark Contours')
    if btn_pressed:
        contour_img = cv.cvtColor(src=cv.imread(
            filename='src/assets/images/out/contours.jpg'), code=cv.COLOR_BGR2RGB)
        st.image(image=contour_img)

with col2:
    # 4. Perspective Transform
    st.header('Perspective Transform')
    if btn_pressed:
        flipped_img = cv.cvtColor(src=cv.imread(
            filename='src/assets/images/out/flipped.jpg'), code=cv.COLOR_BGR2RGB)
        st.image(image=flipped_img)
