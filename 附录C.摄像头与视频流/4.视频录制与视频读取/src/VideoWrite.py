#-*- coding: UTF-8 -*-

'''
功能描述：视频录制演示代码

作者：阿凯@1Z实验室
网站：www.1zlab.com(网站备案中)
QQ交流群 218214240
'''
import numpy as np
import cv2

# 创建一个VideoCapture对象
cap = cv2.VideoCapture(0)

# 指定视频编解码方式为MJPG
codec = cv2.VideoWriter_fourcc(*'MJPG')
fps = 20.0 # 指定写入帧率为20
frameSize = (640, 480) # 指定窗口大小
# 创建 VideoWriter对象
out = cv2.VideoWriter('demo.avi', codec, fps, frameSize)

print("按键Q-结束视频录制")
while(cap.isOpened()):
    
    ret, frame = cap.read()
    # 如果帧获取正常
    if ret==True:
        # 镜像反转 flip
        # frame = cv2.flip(frame, 1)
        
        # 不断的向视频输出流写入帧图像
        out.write(frame)
        # 在窗口中展示画面
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break

# 释放资源
cap.release()
out.release()
cv2.destroyAllWindows()