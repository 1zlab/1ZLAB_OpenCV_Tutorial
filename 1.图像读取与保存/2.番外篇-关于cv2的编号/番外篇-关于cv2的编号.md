# 番外篇-关于cv2的编号

大家有没有想过一个问题, 阿凯带大家安装的是opencv3.3版本, 为啥引用这个包的时候, 这个包依然叫cv2呢, 这个问题一直困惑了阿凯很久. 直到阿凯在[OpenCV问答社区](http://answers.opencv.org/question/63405/why-do-python-bindings-for-v3-still-use-package-name-cv2/)里找到了答案.

```
@hoju, actually the 2 does not refer to the version number of OpenCV. Basically it is the difference between the underlying C API, which is denoted by the cv prefix and the C++ API which is denoted by the cv2 prefix. This is mainly a historical matter and it is kept to keep backwards compatibility. It also allows you to combine the C and C++ interface if you really need it, but which is discouraged a lot!
```

意思是, opencv的cv1, cv2 指的不是opencv的版本号, 而是opencv底层开发语言的版本. 最开始opencv1的底层是用C语言开发的.  opencv2 跟opencv3 是用c++写的. 所以cv1 指代的是C版本的opencv. cv2 指的是c++版本的opencv.

阿凯之前看的一本opencv的教程learning opencv 代码讲解就是用C写的, 因为出的比较早.

![0119_learning_opencv.jpg](./image/0119_learning_opencv.jpg)



