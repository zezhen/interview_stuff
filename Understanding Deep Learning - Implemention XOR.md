# Understanding Deep Learning - Implemention XOR
----


![[Archive/Machine Learning/_resources/Understanding_Deep_Learning_-_Implemention_XOR.resources/unknown_filename.png]]


**P xor Q = (P or Q)  and not (P and Q)** \=> we need three operations for XOR

1.  p and q => n1
2.  p or q => n2
3.  not (p and q) => n

One hidden layer with two neural can represent these three operations.

XOR cannot be solved by logic regression, which is linear classification model, while combine two logic regression can reach non-linear model and solve the problem. This is one epitome of deep learning, with help of multiple nodes and layers can reach more powerful model and solve more complicated problems.

import tensorflow as tf

\# Place hodler for input and labels
X = tf.placeholder(tf.float32, shape=\[4,2\], name="input")
Y = tf.placeholder(tf.float32, shape=\[4,1\], name="labels")

\# Weights/bias for hidden layer
W1 = tf.Variable(tf.random\_uniform(\[2,2\], -1, 1), name="W1")
b1 = tf.Variable(tf.zeros(\[2\]), name="b1")

\# Weights/bias for output layer
W2 = tf.Variable(tf.random\_uniform(\[2,1\], -1, 1), name="W2")
b2= tf.Variable(tf.zeros(\[1\]), name="b2")

\# Computational graph
A2 = tf.sigmoid(tf.matmul(X, W1) + b1)
YHat = tf.sigmoid(tf.matmul(A2, W2) + b2)

\# Cost function
loss = tf.reduce\_mean(( (Y \* tf.log(YHat)) +
((1 - Y) \* tf.log(1.0 - YHat)) ) \* -1)

\# Optimizer
train\_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

\# Input and labels
XOR\_X = \[\[0,0\],\[0,1\],\[1,0\],\[1,1\]\]
XOR\_Y = \[\[0\],\[1\],\[1\],\[0\]\]

\# Create session
sess = tf.Session()
sess.run(tf.global\_variables\_initializer())
for i in range(20000):
sess.run(train\_step, feed\_dict={X: XOR\_X, Y: XOR\_Y})
cost, yhat = sess.run(\[loss, YHat\], feed\_dict={X: XOR\_X, Y: XOR\_Y})
print i, cost, yhat

----

- Date: 2017-05-10
- Tags: #deep/learning #machineLearning 



