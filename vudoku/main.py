# This the project entry point
'''
The project path is laid out as follows:

Video Input --> Sudoku Grabber -->  Solver --> Visualizer
'''

from solver import slr
from builder import ibg
from extractor import dex, np
from scavenger import srg, cv

import av
import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase

btn_pressed = False
capture_img = dilated_img = contour_img = flipped_img = None


st.markdown("<h1 style='text-align: center;'>Vudoku - Visual Sudoku Solver</h1>",
            unsafe_allow_html=True)


class OpenCVVideoProcessor(VideoProcessorBase):
    # Overridden class
    def recv(self, frame: av.VideoFrame) -> av.VideoFrame:
        # Overridden function
        global capture_img
        capture_img = frame.to_ndarray(format='bgr24')
        return av.VideoFrame.from_ndarray(capture_img, format="bgr24")


col1, col2 = st.columns(spec=2)
with col1:
    # 1. Input
    st.header(body='Input')
    webrtc_streamer(
        key='Input', video_processor_factory=OpenCVVideoProcessor)

with col2:
    # 5. Output
    st.header(body='Output')
    btn_pressed = st.button(label='Solve Sudoku')
    if btn_pressed:
        isSolved = False
        bw_sdk = p_board = p_string = None
        sampled_img = capture_img or cv.cvtColor(
            src=cv.imread(filename='vudoku/assets/images/sample/sudoku10.jpg'),
            code=cv.COLOR_BGR2RGB,
        )


        # returns a black and white sudoku grid
        bw_sdk = srg.relay(image=sampled_img)
        p_string = dex.miner(image=bw_sdk)
        # print(len(p_string), p_string)
        p_board = slr.gateway(
            string=p_string)  # returns a 81 bit string
        ibg.buildImage(p_board)

        solution = cv.cvtColor(src=cv.imread(
            filename='vudoku/assets/images/out/solution.jpg'), code=cv.COLOR_BGR2RGB)
        st.image(image=solution)


col1, col2 = st.columns(spec=2)
with col1:
    # 2. Capture image
    st.header('Captured Image')
    if btn_pressed:
        sampled_img = capture_img or sampled_img
        st.image(image=sampled_img)

with col2:
    # 3. Detect Edges
    st.header('Detect Edges')
    if btn_pressed:
        dilated_img = cv.cvtColor(src=cv.imread(
            filename='vudoku/assets/images/out/dilated.jpg'), code=cv.COLOR_BGR2RGB)
        st.image(image=dilated_img)


col1, col2 = st.columns(spec=2)
with col1:
    # 3.Mark contour points
    st.header('Mark Contours')
    if btn_pressed:
        contour_img = cv.cvtColor(src=cv.imread(
            filename='vudoku/assets/images/out/contours.jpg'), code=cv.COLOR_BGR2RGB)
        st.image(image=contour_img)

with col2:
    # 4. Perspective Transform
    st.header('Perspective Transform')
    if btn_pressed:
        flipped_img = cv.cvtColor(src=cv.imread(
            filename='vudoku/assets/images/out/flipped.jpg'), code=cv.COLOR_BGR2RGB)
        st.image(image=flipped_img)
