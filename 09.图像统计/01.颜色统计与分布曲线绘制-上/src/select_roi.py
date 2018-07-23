# -*- coding: utf-8 -*- 
'''
选取ROI区域
回车或者空格确认选择
c键 撤销选择
'''
import numpy as np
import cv2
import sys


# 文件路径
# img_path = 'blue-color-block.png'
img_path = sys.argv[1]

# 读入图片
img = cv2.imread(img_path)
# 创建一个窗口
cv2.namedWindow("image", flags= cv2.WINDOW_NORMAL | cv2.WINDOW_FREERATIO)
cv2.imshow("image", img)
# 是否显示网格 
showCrosshair = True

# 如果为Ture的话 , 则鼠标的其实位置就作为了roi的中心
# False: 从左上角到右下角选中区域
fromCenter = False
# Select ROI
rect = cv2.selectROI("image", img, showCrosshair, fromCenter)

print("选中矩形区域")
(x, y, w, h) = rect

# Crop image
imCrop = img[y : y+h, x:x+w]

# Display cropped image
cv2.imshow("image_roi", imCrop)
cv2.imwrite("image_roi.png", imCrop)
cv2.waitKey(0)