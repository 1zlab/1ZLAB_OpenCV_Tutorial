# -*- coding: utf-8 -*- 
import numpy as np
import cv2
# 引入Python的可视化工具包 matplotlib
from matplotlib import pyplot as plt


def display_image(image):
    '''
    显示从opencv读入的图片对象(ndarray) 单个image
    '''
    if image is None:
        # 图片为空，读入失败
        print("Error: 图片未空(NoneType)，请检查图片路径。")
        return
    
    if len(image.shape) == 2:
        # 通道数为1,灰度图
        # 需要添加colormap 颜色映射函数为gray
        plt.imshow(image, cmap="gray")
    elif image.shape[2] == 3:
        # 如果图像通道数为3 默认读入的是BGR颜色空间的图片
        # opencv读取到的图片是BGR格式的，Matplotlib按照RGB格式解析的
        # 所以我们需要将颜色空间转换
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    
    plt.show()