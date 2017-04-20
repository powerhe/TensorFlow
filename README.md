# TensorFlow
Artificial Intelligence  - Machine Learning Framework

## Installing with native pip
  If the following version of Python is not installed on your machine, install it now:
  
  Python 3.5.x from [python.org](https://www.python.org/downloads/release/python-352/)
  
  TensorFlow only supports version 3.5.x of Python on Windows. Note that Python 3.5.x comes with the pip3 package manager, which is the   
  program you'll use to install TensorFlow.

  To install TensorFlow, start a terminal. Then issue the appropriate pip3 install command in that terminal. To install the CPU-only 
  version of TensorFlow, enter the following command:
  
  ```
  C:\> pip3 install --upgrade tensorflow
  ```
  
  To install the GPU version of TensorFlow, enter the following command:
  ```
  C:\> pip3 install --upgrade tensorflow-gpu
  ```
  
 ## Get A Start from hello tensorflow!
    You can use the [Pycharm for community](https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=windows&code=PCC) for the coding by python
    
    ```
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
    ```
    
    Output:
    ```
    C:\Users\heli3\AppData\Local\Programs\Python\Python35\python.exe D:/MyProg/tensorflow/helloworld.py
    b'Hello, TensorFlow!'
    ```
