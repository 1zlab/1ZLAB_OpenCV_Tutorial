# -*- coding: utf-8 -*-
'''
测试-统计整个图片的色彩空间分布

依次测试了在不同色彩空间下的统计图
'''
import cv2
from image_color_stat import ImageColorStat

# 读入图片
image_bgr = cv2.imread('blue-color-block.png')

ics = ImageColorStat(image_bgr, 'BGR')
ics.draw_image_stat_result()

# 从BGR色彩空间转换为RGB
image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
ics = ImageColorStat(image_rgb, 'RGB')
ics.draw_image_stat_result()

# 从BGR色彩空间转换为GrayScale灰度图
image_gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)
ics = ImageColorStat(image_gray, 'GRAYSCALE')
ics.draw_image_stat_result()

# 从BGR色彩空间转换为LAB
image_lab = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2LAB)
ics = ImageColorStat(image_lab, 'LAB')
ics.draw_image_stat_result()

# 从BGR色彩空间转换为YUV
image_yuv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2LAB)
ics = ImageColorStat(image_yuv, 'YUV')
ics.draw_image_stat_result()