# -*- coding: utf-8 -*- 
import cv2
from akai_cv_utils import display_image


if __name__ == "__main__":
    # 读入图片 默认是BGR格式
    image = cv2.imread("demo_img.jpg")
    # 读入图片 灰度图 
    # image = cv2.imread("demo_img.png", cv2.IMREAD_GRAYSCALE)
    display_image(image)