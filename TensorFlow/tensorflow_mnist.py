from __future__ import absolute_import, division, print_function, unicode_literals
from tensorflow import keras
import tensorflow as tf

mnist = tf.keras.datasets.mnist
#load and prepare the MNIST dataset: digit images (60,000 training)
(x_train, y_train), (x_test, y_test) = mnist.load_data()
#conver the samples from integers to floating point numbers
x_train, x_test = x_train / 255.0, x_test / 255.0

#build the tf.keras.Sequential model by stacking layers
#and choose an optimizer and loss function for training
model = tf.keras.models.Sequential([
tf.keras.layers.Flatten(input_shape=(28,28)),
tf.keras.layers.Dense(128, activation='relu'),
tf.keras.layers.Dropout(0.2),
tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',
metrics=['accuracy'])

#train and evaluate the model
model.fit(x_train, y_train, epochs=5)
model.evaluate(x_test, y_test, verbose=2)
