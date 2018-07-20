# -*- coding: utf-8 -*- 
'''
根据颜色阈值找到色块所在位置
'''
import numpy as np
import cv2

# 图片路径
img_path = "blue-color-block.png"

# 颜色阈值下界(HSV) lower boudnary
lowerb = (96, 210, 85) 
# 颜色阈值上界(HSV) upper boundary
upperb = (114, 255, 231) 

# 读入素材图片 BGR
img = cv2.imread(img_path, cv2.IMREAD_COLOR)

# 转换色彩空间 HSV
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# 根据颜色阈值转换为二值化图像
img_bin = cv2.inRange(img_hsv, lowerb, upperb)

# 寻找轮廓（只寻找最外侧的色块）
bimg, contours, hier = cv2.findContours(img_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# 声明画布 拷贝自img
canvas = np.copy(img)

# 遍历所有的边缘轮廓集合
for cidx,cnt in enumerate(contours):
    # 获取联通域的外界矩形
    (x, y, w, h) = cv2.boundingRect(cnt)
    # 打印矩形信息
    print('RECT: x={}, y={}, w={}, h={}'.format(x, y, w, h))
    # 原图绘制圆形
    cv2.rectangle(canvas, pt1=(x, y), pt2=(x+w, y+h),color=(0, 0, 255), thickness=3)
    # 截取ROI图像
    # cv2.imwrite("roi_cidx_{}.png".format(cidx), img[y:y+h, x:x+w])

# 展示二值化图像
cv2.namedWindow('binary', flags=cv2.WINDOW_NORMAL | cv2.WINDOW_FREERATIO)
cv2.imshow('binary', img_bin)

# 在HighGUI窗口 展示最终结果
cv2.namedWindow('result', flags=cv2.WINDOW_NORMAL | cv2.WINDOW_FREERATIO)
cv2.imshow('result', canvas)

# 等待任意按键按下
cv2.waitKey(0)
# 关闭其他窗口
cv2.destroyAllWindows()
