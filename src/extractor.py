import cv2 as cv
import numpy as np
from PIL import Image
from keras import models


class DigitExtractor:
    def __init__(self):
        self.cells = []
        self.temp_digit = None

    def splitGrid(self, frame) -> list:
        rows = np.array_split(frame, 9, 0)
        for row in rows:
            columns = np.array_split(row, 9, 1)
            for column in columns:
                self.cells.append(column)

        #cv.imshow('grid', cv.imread('result.jpg'))
        # margin = 4
        # crop_img = cells[5][margin:-margin, margin:-margin].copy()
        # cv.imshow('cell1', crop_img)
        # cv.imwrite(filename='cell1.jpg', img=crop_img)
        # cv.waitKey(10**5)

        basewidth = 28
        resized_img = Image.fromarray(self.cells[9])
        w_percent = (basewidth / float(resized_img.size[0]))
        h_size = int((float(resized_img.size[1]) * float(w_percent)))
        resized_img = resized_img.resize((basewidth, h_size), Image.ANTIALIAS)
        self.temp_digit = np.asarray(resized_img)  # dtype=np.float32

        # cv.imshow(winname='python', mat=self.cell_digit)
        # cv.waitKey(10**5)
        # print(pipe.predict(self.cell_digit.reshape(1,-1)))

        cv.imwrite(filename='sample/cell1.jpg', img=self.temp_digit)

        return self.temp_digit

    def genString(self):
        model = models.load_model(filepath='mnist_trained_model.h5')

        reshaped_img = self.temp_digit.reshape(1, 28, 28, 1)
        # extract_digits.cv.imshow('r', self.temp_digit)
        # new_img = x_train[0].reshape(1, 28, 28, 1)
        # extract_digits.cv.imshow('x', x_train[0])
        predictions = model.predict(reshaped_img)
        digit = predictions[0].tolist().index(max(predictions[0].tolist()))
        print(digit)
        # extract_digits.cv.waitKey(10**5)

        # College all digit, the empty cells are marked as zero the converted into a string
    
    def miner(self, image):
        return ''


# img = cv.imread(filename='result.jpg')
# frame = cv.cvtColor(src=img, code=cv.COLOR_BGR2GRAY)
de = DigitExtractor()
# de.splitGrid(frame=frame)
