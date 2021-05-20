import cv2 as cv
import numpy as np
import pickle as pkl
from PIL import Image

from sklearn import preprocessing
from sklearn.datasets import load_digits
from sklearn.datasets import fetch_openml
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


class DigitRecognizer:
    def __init__(self, train_path, label_path, frame, digit):
        self.train_path = train_path
        self.label_path = label_path
        self.frame = frame
        self.cells = []
        self.cell_digit = digit

    # def trainClassifier(self):
    #     # save model after classifying
    #     # digits = load_digits()
    #     # digits = fetch_openml('mnist_784')
    #     digits = None
    #     # log_reg = LogisticRegression()
    #     # with open(file='MNIST.pkl', mode='wb') as f:
    #     #     pkl.dump(digits, f)
    #     with open(file='MNIST.pkl', mode='rb') as f:
    #         digits = pkl.load(f)
    #     x_train, x_test, y_train, y_test = train_test_split(
    #         digits.data, digits.target, test_size=1/7.0, random_state=0)

    #     pipe = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))

    #     pipe.fit(x_train, y_train)

    #     print(pipe.score(x_test, y_test))

    #     with open(file='linearRegrDigitModel.pkl',mode='wb') as trained_model:
    #         pkl.dump(pipe, trained_model)
    #     # with open(file='linearRegrDigitModel.pkl', mode='rb') as model:
    #     #     pipe = pkl.load(model)
        
    #     # cv.imshow('number', x_test[4].reshape(8, 8))
    #     # print(log_reg.predict(x_test))

    def classifyDigits(self) -> int:
        # use saved model in production
        pipe = None
        with open(file='linearRegrDigitModel.pkl', mode='rb') as model:
            pipe = pkl.load(model)
        basewidth = 28
        img = Image.fromarray(self.cell_digit)
        wpercent = (basewidth / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((basewidth, hsize), Image.ANTIALIAS)
        self.cell_digit = np.asarray(img)
        cv.imshow(winname='python', mat=self.cell_digit)
        cv.waitKey(10**5)
        print(pipe.predict(self.cell_digit.reshape(1,-1)))


def splitGrid(frame) -> list:
    cells = []
    rows = np.array_split(frame, 9, 0)
    for row in rows:
        columns = np.array_split(row, 9, 1)
        for column in columns:
            cells.append(column)
    # cv.imshow('grid', cv.imread('result.jpg'))
    # cv.imshow('cell1', self.cells[80])
    # cv.waitKey(10**5)
    return cells[1]


img = cv.imread(filename='result.jpg')
frame = cv.cvtColor(src=img, code=cv.COLOR_BGR2GRAY)
# print(frame.shape)
result = DigitRecognizer('', '', frame, splitGrid(frame=frame))
# result.trainClassifier()
result.classifyDigits()
