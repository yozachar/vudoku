import cv2 as cv
import numpy as np
from pathlib import Path


class ImageBuilder:

    def __init__(self):
        self.dig_map = {}
        self.row = None

    def buildImage(self, board):

        for idx, file in enumerate(sorted(Path('vudoku/assets/images/digit_map/').iterdir())):
            # print('vudoku/assets/images/digit_map/'+file.name)
            self.dig_map[idx] = cv.imread(
                filename=f'vudoku/assets/images/digit_map/{file.name}'
            )

        for idx in range(9):
            for jdx in range(9):
                old_map = self.dig_map[board[idx][jdx]]
                if jdx == 0:
                    new_map = old_map
                    continue
                new_map = np.concatenate((old_map, new_map), axis=0)
            if idx == 0:
                self.row = new_map
                continue
            self.row = np.concatenate((self.row, new_map), axis=1)

        cv.imwrite(filename='vudoku/assets/images/out/solution.jpg', img=self.row)


ibg = ImageBuilder()
