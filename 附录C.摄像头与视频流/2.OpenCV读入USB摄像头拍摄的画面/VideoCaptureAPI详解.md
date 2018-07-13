

# OpenCV从USB摄像头读取实时图像或者视频流



主要分为三个主要部分

* 视频读取 read
* 视频存储 write
* 视频展示 display



## 源码解析



VideoCapture 类的方法 传入参数  可以是usb摄像头编号（整数） 也可以是视频的地址

 cvSetCaptureProperty





初始化capture

```python
cap.open()
cap.isOpened() # 检查capture是否已经初始化
```



颜色空间的转换 cv2 cvtColor

```python
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
```



cv2.imshow GUI 画面显示 desctroyAllWindows

同时连接多个 双目 嘿嘿嘿



视频流保存为video

## 视频读取源代码

```python
import numpy as np
import cv2

# 0 : camera on my laptop
# 1 : usb camera
cap = cv2.VideoCapture(1)


while(True):
    # Capture frame-by-frame
    # 逐帧获取画面
    # ret ？ 画面是否获取成功
    ret, frame = cap.read()
    
    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    # cv2.imshow('frame',gray)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
# 释放Capture  ？ 具体都做了哪些呢
cap.release()
cv2.destroyAllWindows()
```



## VideoCapture

> 在OpenCV的C接口中，这个名称为`CvCapture` 在C++的接口中，数据类型为`VideoCapture`， 两个接口不可混用



Class for video capturing from video files, image sequences or cameras. The class provides C++ API for capturing video from cameras or for reading video files and image sequences. 

## Video Property 视频的18个属性 



访问属性的方法

```python
cap.get(featureId)
# 例如
cap.get(1)
# 设置属性 cap.set(featuerId, value)
```

如何设定USB摄像头的预处理  宽高 分辨率 

> TODO 能不能不用3 4 改用  cv2.CAP_PROP_FRAME_WIDTH

```python
cap.set(3, 320) # 设定宽度
cap.set(4, 240) # 设定高度
```



所有的属性设置 见文档 https://docs.opencv.org/3.1.0/d8/dfe/classcv_1_1VideoCapture.html

> 感觉可以用OpenCV写一个视频播放器



> TODO 这里面的属性有的是针对video的， 有的是针对camera的 分开列一下



> 每个参数所代表的含义， QT 实时交互 拖动参数 widget，查看样式



自动增益 白平衡？ 具体所代表的含义



- **CAP_PROP_POS_MSEC** Current position of the video file in milliseconds or video capture timestamp. 当前画面在video中的时间戳

- **CAP_PROP_POS_FRAMES** 0-based index of the frame to be decoded/captured next.

- **CAP_PROP_POS_AVI_RATIO** Relative position of the video file: 0 - start of the film, 1 - end of the film. 

  ？ 视频里面的相对位置

- **CAP_PROP_FRAME_WIDTH** Width of the frames in the video stream. 画面宽度

- **CAP_PROP_FRAME_HEIGHT** Height of the frames in the video stream. 画面高度

- **CAP_PROP_FPS** Frame rate. 帧率

- **CAP_PROP_FOURCC** 4-character code of codec.

  视频保存的编码

- **CAP_PROP_FRAME_COUNT** Number of frames in the video file.  帧在视频流中的编号

- **CAP_PROP_FORMAT** Format of the [Mat](https://docs.opencv.org/3.1.0/d3/d63/classcv_1_1Mat.html) objects returned by [retrieve()](https://docs.opencv.org/3.1.0/d8/dfe/classcv_1_1VideoCapture.html#a9ac7f4b1cdfe624663478568486e6712) .

- **CAP_PROP_MODE** Backend-specific value indicating the current capture mode.

- **CAP_PROP_BRIGHTNESS** Brightness of the image (only for cameras). 亮度

- **CAP_PROP_CONTRAST** Contrast of the image (only for cameras). 对比度

- **CAP_PROP_SATURATION** Saturation of the image (only for cameras). 饱和度

- **CAP_PROP_HUE** Hue of the image (only for cameras). 色调

- **CAP_PROP_GAIN** Gain of the image (only for cameras). 增益

- **CAP_PROP_EXPOSURE** Exposure (only for cameras). 曝光度

- **CAP_PROP_CONVERT_RGB** Boolean flags indicating whether images should be converted to RGB. 布尔值，是否要转换为RGB值

- **CAP_PROP_WHITE_BALANCE** Currently not supported 白平衡

- **CAP_PROP_RECTIFICATION** Rectification flag for stereo cameras (note: only supported by DC1394 v 2.x backend currently) 

  TODO

> TODO Property的取值/取值范围

## 视频文件读取源码



```python
import numpy as np
import cv2

cap = cv2.VideoCapture('vtest.avi')

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```



## 视频写入源代码



```python

import numpy as np
import cv2
# 返回的是CvCapture的指针？
cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
# 指定视频编码方式
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,0)

        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
```

> TODO 主流都有哪些编码方式 



## 参考



OpenCV文档-Getting Started with Videos

https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html



二.使用OpenCv操纵摄像头采集一幅图像

http://blog.csdn.net/scottly1/article/details/22921735

