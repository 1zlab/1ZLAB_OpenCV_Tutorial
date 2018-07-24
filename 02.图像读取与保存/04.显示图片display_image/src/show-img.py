# -*- coding: utf-8 -*-  
import cv2
# 读入图片
img = cv2.imread('demo_img.jpg')
# 创建窗口并展示图片
cv2.imshow('image', img)
# 等待任意一个按键按下
cv2.waitKey(0)
# 关闭所有的窗口
cv2.destroyAllWindows()
