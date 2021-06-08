import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase

cap_img = None

st.markdown("<h1 style='text-align: center;'>Vudoku - Visual Sudoku Solver</h1>",
            unsafe_allow_html=True)


class Receiver(VideoProcessorBase):

    def transform(self, frame):
        global cap_img
        cap_img = frame.to_ndarray(format='bgr24')
        return cap_img


class Layout:
    def __init__(self):
        self.sample = None
        # capture < edges < contours < transform < solve
        self.capture = self.edges = self.contours = self.transform = self.solve = False

    def topCols(self):
        col1, col2 = st.beta_columns(spec=2)
        with col1:
            # 1. Input
            st.header(body='Input')
            webrtc_streamer(key='Output', video_transformer_factory=Receiver)

        with col2:
            # 5. Output
            st.header(body='Output')
            self.solve = st.button(label='Solve Sudoku', help='Solve Sudoku')
            if self.solve:
                self.capture = self.edges = self.contours = self.transform = True
                st.image(image=self.sample)

    def midCols(self):
        st.beta_container()
        col1, col2 = st.beta_columns(spec=2)
        with col1:
            # 2. Capture image
            st.header('Captured Image')
            self.capture = st.button(label='Capture Image',
                                     help='Capture Input Image')
            if self.capture:
                st.image(image=self.sample)

        with col2:
            # 3. Detect Edges
            st.header('Detect Edges')
            self.edges = st.button(label='Detect Edges',
                                   help='Uses canny edge detector')
            if self.edges:
                self.capture = True
                st.image(image=self.sample)

    def botCol(self):
        col1, col2 = st.beta_columns(spec=2)
        with col1:
            # 3.Mark contour points
            st.header('Mark Contours')
            self.contours = st.button(label='Mark Contour Points',
                                      help='Mark Contour Points')
            if self.contours:
                self.capture = self.edges = True
                st.image(image=self.sample)

        with col2:
            # 4. Perspective Transform
            st.header('Perspective Transform')
            self.transform = st.button(
                label='Perspective Transform', help='Perspective Transform')
            if self.transform:
                self.capture = self.edges = self.contours = True
                st.image(image=self.sample)
