import tensorflow as tf

# Load the MNIST dataset
mnist = tf.keras.datasets.mnist
(x_train, y_train),(x_test, y_test) = mnist.load_data()

# reshape dimensions to [samples][width][height][channels]
x_train = x_train.reshape((x_train.shape[0], 28, 28, 1)).astype('float32')
x_test = x_test.reshape((x_test.shape[0], 28, 28, 1)).astype('float32')

# Normalize the training values
x_train, x_test = x_train/255.0, x_test/255.0

# one hot encode (Convert Categorical Data to Numerical Data) outputs
y_train = tf.keras.utils.to_categorical(y_train)
y_test = tf.keras.utils.to_categorical(y_test)

class myCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        # If you are using Tensorflow 1.x, replace 'accuracy' for 'acc' in the next line
    
        if(logs.get('accuracy')>0.99):
            print("\nReached 99.0% accuracy so cancelling training!")
            self.model.stop_training = True

# Create a model
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(30, (5,5), input_shape=(28, 28, 1), activation='relu'),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Conv2D(15, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(50, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=25, callbacks=[myCallback()])

# Evaluate the model
model.evaluate(x_test, y_test)

# Save the Model
model.save('models/my_mnist_model.h5')
converter = tf.compat.v1.lite.TFLiteConverter.from_keras_model_file('models/my_mnist_model.h5')
tflite_model = converter.convert()
open("models/converted_mnist_model.tflite", "wb").write(tflite_model)