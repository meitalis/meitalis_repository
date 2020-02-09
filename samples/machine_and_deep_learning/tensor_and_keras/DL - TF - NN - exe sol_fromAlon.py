# A nearest neighbor learning algorithm example using TensorFlow library.
# This example is using the MNIST database of handwritten digits
# (http://yann.lecun.com/exdb/mnist/)
# Author: Aymeric Damien
# Project: https://github.com/aymericdamien/TensorFlow-Examples/

from __future__ import print_function

import numpy as np
import tensorflow as tf
tf.compat.v1.disable_eager_execution()
from sklearn import datasets

# # Import MNIST data
# from tensorflow.examples.tutorials.mnist import input_data
# mnist = input_data.read_data_sets("/tmp/data/", one_hot=True)

iris = datasets.load_iris()
rows, cols = iris.data.shape
X = iris.data
y = iris.target
class_names = iris.target_names

# In this example, we limit mnist data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y)
# tf Graph Input
xtr = tf.compat.v1.placeholder("float", [None, cols])
xte = tf.compat.v1.placeholder("float", [cols])
# theta = tf.Variable(tf.compat.v1.random_uniform([m + 1, 1], -1, 1, seed=42), name='theta')

# Nearest Neighbor calculation using L1 Distance
# Calculate L2 Distance
distance = tf.reduce_sum(tf.square(tf.subtract(xtr, xte)), axis=1)
# Prediction: Get min distance index (Nearest neighbor)
pred = tf.math.argmin(distance, 0)

accuracy = 0.

# Initialize the variables (i.e. assign their default value)
init = tf.compat.v1.global_variables_initializer()

# Start training
with tf.compat.v1.Session() as sess:
    # Run the initializer
    sess.run(init)
    # loop over test data
    for i in range(len(X_test)):
        # Get nearest neighbor
        nn_index = sess.run(pred, feed_dict={ xtr: X_train, xte: X_test[i, :]})
        predicted = y_train[nn_index]
        true_class = y_test[i]
        # Get nearest neighbor class label and compare it to its true label
        print("Test", i, "Prediction:", predicted, \
              "True Class:", true_class)
        # Calculate accuracy
        if predicted == true_class:
            accuracy += 1./len(X_test)
    print("Done!")
    print("Accuracy:", accuracy)



# xtr = tf.placeholder("float", [None, 784])
# ytr = tf.placeholder("float", [None, 10])
# xte = tf.placeholder("float", [784])
#
# # Euclidean Distance
# distance = tf.negative(tf.sqrt(tf.reduce_sum(tf.square(tf.subtract(xtr, xte)), reduction_indices=1)))
# # Prediction: Get min distance neighbors
# values, indices = tf.nn.top_k(distance, k=K, sorted=False)
#
# nearest_neighbors = []
# for i in range(K):
#     nearest_neighbors.append(tf.argmax(ytr[indices[i]], 0))
#
# neighbors_tensor = tf.stack(nearest_neighbors)
# y, idx, count = tf.unique_with_counts(neighbors_tensor)
# pred = tf.slice(y, begin=[tf.argmax(count, 0)], size=tf.constant([1], dtype=tf.int64))[0]
#
# accuracy = 0.
#
# # Initializing the variables
# init = tf.initialize_all_variables()
#
# # Launch the graph
# with tf.Session() as sess:
#     sess.run(init)
#
#     # loop over test data
#     for i in range(len(Xte)):
#         # Get nearest neighbor
#         nn_index = sess.run(pred, feed_dict={xtr: Xtr, ytr: Ytr, xte: Xte[i, :]})
#         # Get nearest neighbor class label and compare it to its true label
#         print("Test", i, "Prediction:", nn_index,
#              "True Class:", np.argmax(Yte[i]))
#         #Calculate accuracy
#         if nn_index == np.argmax(Yte[i]):
#             accuracy += 1. / len(Xte)
#     print("Done!")
#     print("Accuracy:", accuracy)