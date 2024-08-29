# contain neural network model definition

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

def create_model():
    # create sequential model (linear stack of layers, each layer has one input tensor and one output tensor)
    model = Sequential()

    # add convolutional layer with 32 filters, 3x3 kernel size, and ReLU activation function
    model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    # flatten the output of the convolutional layer (convert 2D metrics into 1D vector so that output can be fed to conneted layers)
    model.add(Flatten())

    # add dense layers, output layer has 10 units where each unit represents a digit
    model.add(Dense(128, activation='relu'))
    model.add(Dense(10, activation='softmax'))

    # compile model
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    return model