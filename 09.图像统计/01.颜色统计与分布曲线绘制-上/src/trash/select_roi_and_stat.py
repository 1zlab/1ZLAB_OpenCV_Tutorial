# -*- coding: utf-8 -*- 
'''
选择ROI图像，并获取颜色统计图
c键 撤销选择
'''
import numpy as np
import cv2
from image_color_stat import ImageColorStat

# 设定图片文件路径
img_path = 'blue-color-block.png'
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

# 获取ROI图像
imCrop = img[y : y+h, x:x+w]
# 显示ROI图像
cv2.imshow("image_roi", imCrop)
# 保存ROI图像
cv2.imwrite("image_roi.png", imCrop)

# 统计ROI图像的颜色
ics = ImageColorStat(imCrop, 'BGR')
ics.draw_image_stat_result()

# 统计ROI图像的颜色
ics = ImageColorStat(cv2.cvtColor(imCrop, cv2.COLOR_BGR2YUV), 'YUV')
ics.draw_image_stat_result()


cv2.waitKey(0)