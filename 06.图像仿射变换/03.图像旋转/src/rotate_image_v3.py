# -*- coding: utf-8 -*- 
'''
围绕画面中的任意一点旋转
'''
import numpy as np
import cv2
from math import cos,sin,radians
from matplotlib import pyplot as plt

img = cv2.imread('cat.jpg')

height, width, channel = img.shape

theta = 45

def getRotationMatrix2D(theta, cx=0, cy=0):
    # 角度值转换为弧度值
    theta = radians(theta)

    M = np.float32([
        [cos(theta), -sin(theta), (1-cos(theta))*cx + sin(theta)*cy],
        [sin(theta), cos(theta), -sin(theta)*cx + (1-cos(theta))*cy]])
    return M

# 求得图片中心点， 作为旋转的轴心
cx = int(width / 2)
cy = int(height / 2)

# 进行2D 仿射变换
# 围绕原点 逆时针旋转30度
M = getRotationMatrix2D(30, cx=cx, cy=cy)
rotated_30 = cv2.warpAffine(img, M, (width, height))

# 围绕原点 逆时针旋转45度
M = getRotationMatrix2D(45, cx=cx, cy=cy)
rotated_45 = cv2.warpAffine(img, M, (width, height))

# 围绕原点 逆时针旋转60度
M = getRotationMatrix2D(60, cx=cx, cy=cy)
rotated_60 = cv2.warpAffine(img, M, (width, height))

plt.subplot(221)
plt.title("Src Image")
plt.imshow(img[:,:,::-1])

plt.subplot(222)
plt.title("Rotated 30 Degree")
plt.imshow(rotated_30[:,:,::-1])

plt.subplot(223)
plt.title("Rotated 45 Degree")
plt.imshow(rotated_45[:,:,::-1])

plt.subplot(224)
plt.title("Rotated 60 Degree")
plt.imshow(rotated_60[:,:,::-1])

plt.show()