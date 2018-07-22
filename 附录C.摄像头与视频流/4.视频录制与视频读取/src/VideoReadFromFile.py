#-*- coding: UTF-8 -*-
'''
读入视频并在窗口展示

作者：阿凯@1Z实验室
网站：www.1zlab.com(网站备案中)
QQ交流群 218214240
'''
import numpy as np
import cv2


# 读入视频流
cap = cv2.VideoCapture('demo.avi')

while(True):
    # 逐帧获取画面
    # ret ？ 画面是否获取成功
    ret, frame = cap.read()
    
    if ret:
        # 在窗口展示视频
        cv2.imshow('frame',frame)
    else:
        print("视频读取完毕或者视频路径异常")
        break

    # 这里做一下适当的延迟，每帧延时0.1s钟
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

# 释放资源
cap.release()
cv2.destroyAllWindows()