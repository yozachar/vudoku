import cv2 as cv
import numpy as np
from PIL import Image
from keras import models


class DigitExtractor:
    def __init__(self):
        self.cells = []
        self.temp_digit = None
        self.string = ''

    def preprocess(self, image):
        # resize image
        basewidth = 28
        resized_img = Image.fromarray(self, image)
        w_percent = (basewidth / float(resized_img.size[0]))
        h_size = int((float(resized_img.size[1]) * float(w_percent)))
        resized_img = resized_img.resize((basewidth, h_size), Image.ANTIALIAS)

        # clean and center digits

        self.temp_digit = np.asarray(resized_img)  # dtype=np.float32 ?

        #cv.imshow('grid', cv.imread('result.jpg'))
        # margin = 4
        # crop_img = cells[5][margin:-margin, margin:-margin].copy()
        # cv.imshow('cell1', crop_img)
        # cv.imwrite(filename='cell1.jpg', img=crop_img)
        # cv.waitKey(10**5)

        # cv.imshow(winname='python', mat=self.cell_digit)
        # cv.waitKey(10**5)
        # print(pipe.predict(self.cell_digit.reshape(1,-1)))

    def splitGrid(self, frame):
        # perform additional preprocessing if required
        rows = np.array_split(ary=frame, indices_or_sections=9, axis=0)
        for row in rows:
            columns = np.array_split(ary=row, indices_or_sections=9, axis=1)
            for column in columns:
                self.preprocess(image=column)
                self.cells.append(self.temp_digit)

    def genString(self):
        # check if model exists if not, prompt user to run classifier
        model = models.load_model(filepath='mnist_trained_model.h5')

        for cell in self.cells:
            # Mark empty cells are marked as zero the converted into a string
            rs_cell = cell.reshape(1, 28, 28, 1)
            predictions = model.predict(rs_cell)
            digit = predictions[0].tolist().index(max(predictions[0].tolist()))
            self.string += str(digit)

    def miner(self, image):
        self.splitGrid(frame=image)
        self.genString()
        return self.string
