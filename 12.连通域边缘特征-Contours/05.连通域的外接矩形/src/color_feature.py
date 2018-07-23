# -*- coding: utf-8 -*- 
'''
颜色特征识别
'''
import numpy as np
import cv2


def color_block_finder(img, lowerb, upperb, 
                        min_w=0, max_w=None, min_h=0, max_h=None):
    '''
    色块识别 返回矩形信息
    '''
    # 转换色彩空间 HSV
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # 根据颜色阈值转换为二值化图像
    img_bin = cv2.inRange(img_hsv, lowerb, upperb)

    # 寻找轮廓（只寻找最外侧的色块）
    bimg, contours, hier = cv2.findContours(img_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # 声明画布 拷贝自img
    canvas = np.copy(img)
    # 外接矩形区域集合
    rects = []

    if max_w is None:
        # 如果最大宽度没有设定，就设定为图像的宽度
        max_w = img.shape[1]
    if max_h is None:
        # 如果最大高度没有设定，就设定为图像的高度
        max_h = img.shape[0]
        
    # 遍历所有的边缘轮廓集合
    for cidx,cnt in enumerate(contours):
        # 获取联通域的外界矩形
        (x, y, w, h) = cv2.boundingRect(cnt)

        if w >= min_w and w <= max_w and h >= min_h and h <= max_h:
            # 将矩形的信息(tuple)添加到rects中
            rects.append((x, y, w, h))
    return rects

def draw_color_block_rect(img, rects,color=(0, 0, 255)):
    '''
    绘制色块的矩形区域
    '''
    # 声明画布(canvas) 拷贝自img
    canvas = np.copy(img)
    # 遍历矩形区域
    for rect in rects:
        (x, y, w, h) = rect
        # 在画布上绘制矩形区域（红框）
        cv2.rectangle(canvas, pt1=(x, y), pt2=(x+w, y+h),color=color, thickness=3)
    
    return canvas