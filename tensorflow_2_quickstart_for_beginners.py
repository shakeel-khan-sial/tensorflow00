# -*- coding: utf-8 -*-
"""TensorFlow_2_quickstart_for_beginners.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZB9b14cpzRacdHxdhHaft0teIPVdEIE3

# Set up TensorFlow
"""

# imports
import tensorflow as tf
print("TensorFlow version:",  tf.__version__)

"""# Load  a dataset"""

mnist = tf.keras.datasets.mnist

(x_train, y_train),(x_test, y_test) = mnist.load_data()



print(len(x_train), len(x_test), len(y_train), len(y_test))

"""# Building Machine Learning Model"""

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape = (28,28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10)
])



model.summary()

x_train.shape

predictions = model(x_train[:1]).numpy()
predictions

tf.nn.softmax(predictions).numpy()

"""# loss functions"""

loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

loss_fn(y_train[:1], predictions).numpy()

"""# compile model"""

# comile mode

model.compile(optimizer='adam',
              loss = loss_fn,
              metrics= ['accuracy'])

"""# train and evaluate the model"""

model.fit(x_train, y_train, epochs = 20)

model.evaluate(x_test, y_test, verbose=2)

# probability model
probability_model = tf.keras.Sequential([
                                         model,
                                         tf.keras.layers.Softmax()
])

probability_model(x_test[:5])

