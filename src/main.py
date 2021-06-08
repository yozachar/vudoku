# This the project entry point
'''
The project path is laid out as follows:

Video Input --> Sudoku Grabber -->  Solver --> Visualizer
'''

from solver import slr
from extractor import dex, np
from scavenger import srg, cv

import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase


# capture < edges < contours < transform < solve
# capture = edges = contours = transform = solve = False
capture_img = dilated_img = contour_img = flipped_img = None

btn_pressed = isSolved = False
bw_sdk = p_string = s_board = None
sampled_img = cv.cvtColor(src=cv.imread(
            filename='src/assets/images/sample/sudoku10.jpg'), code=cv.COLOR_BGR2RGB)

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
    solve = st.button(label='Solve Sudoku', help='Solve Sudoku')
    if solve:
        btn_pressed = True
        st.image(image=sampled_img)


col1, col2 = st.beta_columns(spec=2)
with col1:
    # 2. Capture image
    st.header('Captured Image')
    capture = st.button(label='Capture Image',
                        help='Capture Input Image')
    if capture:
        btn_pressed = True
        sampled_img = capture_img if capture_img else sampled_img
        st.image(image=sampled_img)

with col2:
    # 3. Detect Edges
    st.header('Detect Edges')
    edges = st.button(label='Detect Edges',
                      help='Uses canny edge detector')
    if edges:
        btn_pressed = True
        dilated_img = cv.cvtColor(src=cv.imread(
            filename='src/assets/images/out/dilated.jpg'), code=cv.COLOR_BGR2RGB)
        st.image(image=dilated_img)


col1, col2 = st.beta_columns(spec=2)
with col1:
    # 3.Mark contour points
    st.header('Mark Contours')
    contours = st.button(label='Mark Contour Points',
                         help='Mark Contour Points')
    if contours:
        btn_pressed = True
        contour_img = cv.cvtColor(src=cv.imread(
            filename='src/assets/images/out/contours.jpg'), code=cv.COLOR_BGR2RGB)
        st.image(image=contour_img)

with col2:
    # 4. Perspective Transform
    st.header('Perspective Transform')
    transform = st.button(
        label='Perspective Transform', help='Perspective Transform')
    if transform:
        btn_pressed = True
        flipped_img = cv.cvtColor(src=cv.imread(
            filename='src/assets/images/out/flipped.jpg'), code=cv.COLOR_BGR2RGB)
        st.image(image=flipped_img)

if btn_pressed:
    bw_sdk = srg.relay(image=sampled_img)  # returns a black and white sudoku grid
    p_string = dex.miner(image=bw_sdk)  # returns a 81 bit string
    isSolved, s_board = slr.gateway(string=p_string)