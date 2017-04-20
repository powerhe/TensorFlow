# This gives Python access to all of TensorFlow's classes, methods, and symbols.
# Most of the documentation assumes you have already done this.
import tensorflow as tf

def main():
    # define one constant operation
    hello = tf.constant('Hello, TensorFlow!')
    # define a default session operation
    sess = tf.Session()
    # run the session
    print(sess.run(hello))

if __name__ == "__main__":
    main()