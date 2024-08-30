# contain neural network model definition

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# this was useful pre model training, left in bc
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

# load trained model, code from here on is post model training
model = load_model("digit_recognition_model.h5")

def preprocess_image(image_data):
    """
    preprocess the incoming image data to match the format expected by the model
    """
    image = np.array(image_data).astype('float32')

    # assuming the image data is a flat list
    image = image.reshape(28, 28)  

    # normalize to range [0, 1]
    image = image / 255.0  

    # add batch dimension
    image = np.expand_dims(image, axis=0) 

    # add channel dimension
    image = np.expand_dims(image, axis=-1)  
    return image

def predict_digit(image_data):
    """
    predict the digit from the given image data
    """
    processed_image = preprocess_image(image_data)
    prediction = model.predict(processed_image)
    return np.argmax(prediction)