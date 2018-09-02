# -*- coding: utf-8 -*- 
'''
围绕原点处旋转　(图片左上角)　正方向为逆时针
'''
import numpy as np
import cv2
import math
from matplotlib import pyplot as plt

img = cv2.imread('cat.jpg')

height, width, channel = img.shape

def getRotationMatrix2D(theta):
    # 角度值转换为弧度值
    # 因为图像的左上角是原点 需要×-1
    theta = math.radians(-1*theta)

    M = np.float32([
        [math.cos(theta), -math.sin(theta), 0],
        [math.sin(theta), math.cos(theta), 0]])
    return M

# 进行2D 仿射变换
# 围绕原点 顺时针旋转30度
M = getRotationMatrix2D(30)
rotated_30 = cv2.warpAffine(img, M, (width, height))

# 围绕原点 顺时针旋转45度
M = getRotationMatrix2D(45)
rotated_45 = cv2.warpAffine(img, M, (width, height))

# 围绕原点 顺时针旋转60度
M = getRotationMatrix2D(60)
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