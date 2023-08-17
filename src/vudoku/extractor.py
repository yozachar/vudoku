"""Extractor."""

# external
import cv2 as cv
from cv2.typing import MatLike
from keras import models
import numpy as np


class DigitExtractor:
    """Digit Extractor."""

    def __init__(self):
        """Initialized Digit Extractor."""
        self.cells: list[MatLike] = []
        self.string = ""

    def split_grid(self, frame: MatLike):
        """Split Grid."""
        # perform additional preprocessing if required
        rows = np.array_split(ary=frame, indices_or_sections=9, axis=0)
        for idx, row in enumerate(rows):
            columns = np.array_split(ary=row, indices_or_sections=9, axis=1)
            for jdx, column in enumerate(columns):
                resized_img = cv.resize(
                    column[3:-3, 3:-3],  # the 3:-3 slice removes the borders from each image
                    dsize=(28, 28),
                    interpolation=cv.INTER_CUBIC,
                )
                cv.imwrite(
                    filename=f"vudoku/assets/images/out/cells/cell{idx}{jdx}.jpg", img=resized_img
                )
                self.cells.append(resized_img)

    def gen_string(self):
        """Generate String."""
        # check if model exists if not, prompt user to run classifier
        model = models.load_model(filepath="vudoku/assets/models/mnist_trained_model_v1.h5")

        for cell in self.cells:
            # Mark empty cells are marked as zero the converted into a string
            rs_cell = cell.reshape(1, 28, 28, 1)
            predictions = model.predict(rs_cell)
            digit = predictions[0].tolist().index(max(predictions[0].tolist()))
            self.string += str(digit)

    def miner(self, image: MatLike):
        """Miner."""
        self.split_grid(frame=image)
        self.gen_string()
        return self.string


dex = DigitExtractor()
