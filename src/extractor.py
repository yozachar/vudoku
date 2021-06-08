import cv2 as cv
import numpy as np
from keras import models


class DigitExtractor:
    def __init__(self):
        self.cells = []
        self.string = ''

    def splitGrid(self, frame):
        # perform additional preprocessing if required
        rows = np.array_split(ary=frame, indices_or_sections=9, axis=0)
        for idx, row in enumerate(rows):
            columns = np.array_split(ary=row, indices_or_sections=9, axis=1)
            for jdx, column in enumerate(columns):
                resized_img = cv.resize(column[3:-3, 3:-3],  # the 3:-3 slice removes the borders from each image
                                        dsize=(28, 28),
                                        interpolation=cv.INTER_CUBIC)
                cv.imwrite(
                    filename=f'src/assets/images/out/cells/cell{idx}{jdx}.jpg', img=resized_img)
                self.cells.append(resized_img)

    def genString(self):
        # check if model exists if not, prompt user to run classifier
        model = models.load_model(filepath='src/mnist_trained_model.h5')

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


dex = DigitExtractor()
