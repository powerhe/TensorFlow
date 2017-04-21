# MNIST For ML

## Read MNIST Data from [MNIST Databas](http://yann.lecun.com/exdb/mnist/)

### FILE FORMATS FOR THE MNIST DATABASE
  The data is stored in a very simple file format designed for storing vectors and multidimensional matrices. 
  General info on this format is given at the end of this page, but you don't need to read that to use the data files.
  All the integers in the files are stored in the MSB first (high endian) format used by most non-Intel processors. 
  Users of Intel processors and other low-endian machines must flip the bytes of the header.
```
TRAINING SET LABEL FILE (train-labels-idx1-ubyte):

[offset] [type]          [value]          [description] 
0000     32 bit integer  0x00000801(2049) magic number (MSB first) 
0004     32 bit integer  60000            number of items 
0008     unsigned byte   ??               label 
0009     unsigned byte   ??               label 
........ 
xxxx     unsigned byte   ??               label
The labels values are 0 to 9.

TRAINING SET IMAGE FILE (train-images-idx3-ubyte):

[offset] [type]          [value]          [description] 
0000     32 bit integer  0x00000803(2051) magic number 
0004     32 bit integer  60000            number of images 
0008     32 bit integer  28               number of rows 
0012     32 bit integer  28               number of columns 
0016     unsigned byte   ??               pixel 
0017     unsigned byte   ??               pixel 
........ 
xxxx     unsigned byte   ??               pixel
Pixels are organized row-wise. Pixel values are 0 to 255. 0 means background (white), 255 means foreground (black).
```

### Start here with these TWO lines of code which will download and read in the data automatically:
```
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
```
## Softmax Regressions

We know that every image in MNIST is of a handwritten digit between zero and nine. 
So there are only ten possible things that a given image can be. 
We want to be able to look at an image and give the probabilities for it being each digit. 

### TWO Step as follow:
  1. add up the evidence of our input being in certain classes
  2. convert that evidence into probabilities
  
### Source Code
Step ONE: Creat the model
```
# Create the model
  x = tf.placeholder(tf.float32, [None, 784])
  W = tf.Variable(tf.zeros([784, 10]))
  b = tf.Variable(tf.zeros([10]))
  y = tf.matmul(x, W) + b
```

Step TWO: How to train the model
ask TensorFlow to minimize cross_entropy 
using the gradient descent algorithm with a learning rate of 0.5. 
Gradient descent is a simple procedure
```
# Define loss and optimizer
  y_ = tf.placeholder(tf.float32, [None, 10])

# outputs of 'y', and then average across the batch.
  cross_entropy = tf.reduce_mean(
      tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y))
  train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

  sess = tf.InteractiveSession()
  tf.global_variables_initializer().run()
  
# Train : We'll run the training step 1000 times!
```
  for _ in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
```

## Test our model
Simply just use the tf.equal to check if our prediction matches the truth(label)
```
# Test trained model
  correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
  accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
  print(sess.run(accuracy, feed_dict={x: mnist.test.images,
                                      y_: mnist.test.labels}))
```

## Output
Let's check the model's test result
This is should be about 92%
Maybe, it is not very good, we shoud try the better model in the future.



