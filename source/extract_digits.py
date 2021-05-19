import cv2 as cv
import numpy as np

class DigitRecognizer:
    def __init__(self, train_path, label_path, frame):
        self.train_path = train_path
        self.label_path = label_path
        self.frame = frame
        self.cells = []
        self.digits = []
    
    def splitGrid(self) -> list:
        rows = np.array_split(self.frame, 9, 0)
        for row in rows:
            columns = np.array_split(row, 9, 1)
            for column in columns:
                self.cells.append(column)
        # cv.imshow('grid', cv.imread('result.jpg'))
        # cv.imshow('cell1', self.cells[80])
        # cv.waitKey(10**5)
        return self.cells
    
    def extractDigit(self):
        pass

    def trainClassifier(self):
        pass

    def classifyDigits(self) -> int:
        pass


img = cv.imread(filename='result.jpg')
frame = cv.cvtColor(src=img, code=cv.COLOR_BGR2GRAY)
print(frame.shape)
digits = DigitRecognizer('', '', frame)
print(len(digits.splitGrid()))