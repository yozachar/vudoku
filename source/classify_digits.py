# 1. Install Keras
# 2. Install tensorflow GPU

# 3. Import libraries and modules
# Trains a simple convnet on the MNIST dataset.
# Gets to 99.25% test accuracy after 12 epochs

# from __future__ import print_function
import extract_digits
# from pprint import pprint
# import keras
from keras import models
# from keras.datasets import mnist
# from keras.models import Sequential
# from keras.layers import Dense, Dropout, Flatten
# from keras.layers import Conv2D, MaxPooling2D
# from keras import backend as K

# # # batch_size = 128
# num_classes = 10
# # # epochs = 12

# # # 4. Load pre-shuffled MNIST data into train and test sets
# # # input image dimensions
# img_rows, img_cols = 28, 28

# # the data, split between train and test sets
# (x_train, y_train), (x_test, y_test) = mnist.load_data()

# # 5. Preprocess input data
# if K.image_data_format() == 'channels_first':
#     x_train = x_train.reshape(x_train.shape[0], 1, img_rows, img_cols)
#     x_test = x_test.reshape(x_test.shape[0], 1, img_rows, img_cols)
#     input_shape = (1, img_rows, img_cols)
# else:
#     x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1)
#     x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)
#     input_shape = (img_rows, img_cols, 1)

# x_train = x_train.astype('float32')
# x_test = x_test.astype('float32')
# x_train /= 255
# x_test /= 255
# print('x_train shape:', x_train.shape)
# print(x_train.shape[0], 'train samples')
# print(x_test.shape[0], 'test samples')

# # # 6. Preprocess class labels
# # # convert class vectors to binary class matrices
# y_train = keras.utils.to_categorical(y=y_train, num_classes=num_classes)
# y_test = keras.utils.to_categorical(y=y_test, num_classes=num_classes)

# # 7. Define model architecture
# model = Sequential()
# model.add(Conv2D(32, kernel_size=(3, 3),
#                  activation='relu',
#                  input_shape=input_shape))
# model.add(Conv2D(filters=64, kernel_size=(3, 3), activation='relu'))
# model.add(MaxPooling2D(pool_size=(2, 2)))
# model.add(Dropout(rate=0.25))
# model.add(Flatten())
# model.add(Dense(units=128, activation='relu'))
# model.add(Dropout(rate=0.5))
# model.add(Dense(units=num_classes, activation='softmax'))


# # 8. Compile model
# model.compile(loss=keras.losses.categorical_crossentropy,
#               optimizer=keras.optimizers.Adadelta(),
#               metrics=['accuracy'])


# # 9. Fit model on training data
# model.fit(x=x_train, y=y_train,
#           batch_size=batch_size,
#           epochs=epochs,
#           verbose=1,
#           validation_data=(x_test, y_test))

# 12. Load Model
model = models.load_model(filepath='mnist_trained_model.h5')

# 10. Evaluate model on test data
# score = model.evaluate(x=x_test, y=y_test, verbose=0)
# print('Test loss:', score[0])
# print('Test accuracy:', score[1])

# prediction = model.predict(x_test)

# print(prediction)
# value= extract_digits.np.argmax(prediction, axis = 1)[:5] 
# label = extract_digits.np.argmax(y_test,axis = 1)[:5] 
new_img = extract_digits.number.reshape(1,28,28,1)
ans = model.predict(new_img)
ans = ans[0].tolist().index(max(ans[0].tolist()))
print(ans)

# print(extract_digits.number)

# print(value)


# 11. Save model
# model.save(filepath='mnist_trained_model.h5')  # creates a HDF5 file
