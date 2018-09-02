# -*- coding: utf-8 -*- 
'''
围绕原点处旋转　(图片左上角)　正方向为逆时针
利用getRotationMatrix2D函数生成仿射矩阵
'''
import numpy as np
import cv2
from math import cos,sin,radians
from matplotlib import pyplot as plt

img = cv2.imread('cat.jpg')

height, width, channel = img.shape

# 求得图片中心点， 作为旋转的轴心
cx = int(width / 2)
cy = int(height / 2)
# 旋转的中心
center = (cx, cy)

new_dim = (width, height)

# 进行2D 仿射变换
# 围绕原点 逆时针旋转30度
M = cv2.getRotationMatrix2D(center=center,angle=30, scale=1.0)
rotated_30 = cv2.warpAffine(img, M, new_dim)

# 围绕原点 逆时针旋转30度
M = cv2.getRotationMatrix2D(center=center,angle=45, scale=1.0)
rotated_45 = cv2.warpAffine(img, M, new_dim)

# 围绕原点  逆时针旋转30度
M = cv2.getRotationMatrix2D(center=center,angle=60, scale=1.0)
rotated_60 = cv2.warpAffine(img, M, new_dim)

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