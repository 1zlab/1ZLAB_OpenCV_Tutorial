#-*- coding: UTF-8 -*-
'''
获取特定帧数的照片

作者：阿凯@1Z实验室
网站：www.1zlab.com(网站备案中)
QQ交流群 218214240
'''

import numpy as np
import cv2


# 读取视频流
cap = cv2.VideoCapture('demo.avi')
# 获取视频所有的帧数
amount_of_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
# 设置当前帧的位置 amount_of_frames-1 代表最后一帧
cap.set(cv2.CAP_PROP_POS_FRAMES, amount_of_frames-1)

ret, img = cap.read()

if ret:
    cv2.imwrite('last_frame.png', img)
