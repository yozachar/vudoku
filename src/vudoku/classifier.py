"""Classifier."""

# external
from keras import (
    backend as kb,
    losses,
    optimizers,
)
from keras.datasets import mnist
from keras.layers import Conv2D, Dense, Dropout, Flatten, MaxPooling2D
from keras.models import Sequential
from keras.utils.np_utils import to_categorical

# says something changed to => keras.utils.to_categorical ?np_utils?


class DigitClassifier:
    """Digit Classifier."""

    def __init__(self):
        """Initialize Digit Classifier."""
        # initialize classifier
        self.batch_size = 128
        self.num_classes = 10
        self.epochs = 12

        self.x_train = self.y_train = None
        self.x_text = self.y_test = None
        self.input_shape = None

        self.model: Sequential | None = None

    def pre_process(self):
        """Pre process."""
        # Preprocess input data
        img_rows, img_cols = 28, 28
        (self.x_train, self.y_train), (self.x_test, self.y_test) = mnist.load_data()
        # print(self.x_test.shape)

        if kb.image_data_format() == "channels_first":
            self.x_train = self.x_train.reshape(self.x_train.shape[0], 1, img_rows, img_cols)
            self.x_test = self.x_test.reshape(self.x_test.shape[0], 1, img_rows, img_cols)
            self.input_shape = (1, img_rows, img_cols)
        else:
            self.x_train = self.x_train.reshape(self.x_train.shape[0], img_rows, img_cols, 1)
            self.x_test = self.x_test.reshape(self.x_test.shape[0], img_rows, img_cols, 1)
            self.input_shape = (img_rows, img_cols, 1)

        self.x_train = self.x_train.astype("float32")
        self.x_test = self.x_test.astype("float32")
        self.x_train /= 255
        self.x_test /= 255
        # print('self.x_train shape:', self.x_train[0])
        # print(self.x_train.shape[0], 'train samples')
        # print(self.x_test.shape[0], 'test samples')

        # convert class vectors to binary class matrices
        self.y_train = to_categorical(y=self.y_train, num_classes=self.num_classes)
        self.y_test = to_categorical(y=self.y_test, num_classes=self.num_classes)

    def define_model(self):
        """Define Model."""
        # Define a Sequential self.model
        self.model = Sequential()
        self.model.add(
            Conv2D(32, kernel_size=(3, 3), activation="relu", input_shape=self.input_shape)
        )
        self.model.add(Conv2D(filters=64, kernel_size=(3, 3), activation="relu"))
        self.model.add(MaxPooling2D(pool_size=(2, 2)))
        self.model.add(Dropout(rate=0.25))
        self.model.add(Flatten())
        self.model.add(Dense(units=128, activation="relu"))
        self.model.add(Dropout(rate=0.5))
        self.model.add(Dense(units=self.num_classes, activation="softmax"))

    def compile_and_train(self):
        """Compile and Train."""
        if not self.model:
            return

        # Compile self.model
        self.model.compile(
            loss=losses.categorical_crossentropy,
            optimizer=optimizers.Adadelta(),
            metrics=["accuracy"],
        )

        # Fit self.model on training data
        self.model.fit(
            x=self.x_train,
            y=self.y_train,
            batch_size=self.batch_size,
            epochs=self.epochs,
            verbose=1,
            validation_data=(self.x_test, self.y_test),
        )

    def evaluate_model(self):
        """Evaluate Model."""
        # Evaluate self.model on test data
        if not self.model:
            return

        score = self.model.evaluate(x=self.x_test, y=self.y_test, verbose=0)
        print("Test loss:", score[0])
        print("Test accuracy:", score[1])
        # prediction = self.model.predict(self.x_test)

    def save_model(self):
        """Save Model."""
        # creates a HDF5 file
        if not self.model:
            return
        self.model.save(filepath="vudoku/assets/models/mnist_trained_model_v1.h5")
