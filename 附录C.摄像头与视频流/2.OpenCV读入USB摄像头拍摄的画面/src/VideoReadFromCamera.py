#-*- coding: UTF-8 -*-
'''
代码功能描述
    从摄像头逐帧(frame-by-frame)读入图片并通过HighGUI展示
作者
    阿凯@1Z实验室
教程网站
    www.1zlab.com(网站备案中)
相关课程
    * 通过HIGH GUI展示图片
    http://www.1zlab.com(网站备案中)/p/opencv-highgui-imshow
    * 图像基础变换(仿射变换)
'''

import numpy as np # 引入numpy 用于矩阵运算
import cv2 # 引入opencv库函数

## VideCapture里面的序号
# 0 : 默认为笔记本上的摄像头(如果有的话) / USB摄像头 webcam
# 1 : USB摄像头2
# 2 ：USB摄像头3 以此类推
# -1：代表最新插入的USB设备 

# 创建一个video capture的实例
cap = cv2.VideoCapture(0)

# 查看Video Capture是否已经打开
print("摄像头是否已经打开 ？ {}".format(cap.isOpened()))

## 设置画面的尺寸
# 画面宽度设定为 1920
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
# 画面高度度设定为 1080
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

## 创建一个名字叫做 “image_win” 的窗口
# 窗口属性 flags
#   * WINDOW_NORMAL：窗口可以放缩
#   * WINDOW_KEEPRATIO：窗口缩放的过程中保持比率
#   * WINDOW_GUI_EXPANDED： 使用新版本功能增强的GUI窗口
cv2.namedWindow('image_win',flags=cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO | cv2.WINDOW_GUI_EXPANDED)

# 图像计数 从1开始
img_count = 1

# 帮助信息
helpInfo = '''
=======阿凯贴心小助手=======
提示-按键前需要选中当前画面显示的窗口

按键Q： 退出程序
按键C： Capture 拍照
'''
print(helpInfo)
while(True):
    ## 逐帧获取画面
    # 如果画面读取成功 ret=True，frame是读取到的图片对象(numpy的ndarray格式)
    ret, frame = cap.read()
    
    if not ret:
        # 如果图片没有读取成功
        print("图像获取失败，请按照说明进行问题排查")
        ## 读取失败？问题排查
        # **驱动问题** 有的摄像头可能存在驱动问题，需要安装相关驱动，或者查看摄像头是否有UVC免驱协议
        # **接口兼容性问题** 或者USB2.0接口接了一个USB3.0的摄像头，也是不支持的。
        # **设备挂载问题** 摄像头没有被挂载，如果是虚拟机需要手动勾选设备
        # **硬件问题** 在就是检查一下USB线跟电脑USB接口
        break
    
    ## 颜色空间变换
    # 将BGR彩图变换为灰度图
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    ## 图片镜像
    # * 水平翻转 flipCode = 1
    # * 垂直翻转 flipCode = 0
    # * 同时水平翻转与垂直翻转 flipCode = -1
    # 
    # flipCode = -1
    # frame = cv2.flip(frame, flipCode)
    
    # 更新窗口“image_win”中的图片
    cv2.imshow('image_win',frame)
    
    # 等待按键事件发生 等待1ms
    key = cv2.waitKey(1)
    if key == ord('q'):
        # 如果按键为q 代表quit 退出程序
        print("程序正常退出...Bye 不要想我哦")
        break
    elif key == ord('c'):
        ## 如果c键按下，则进行图片保存
        # 写入图片 并命名图片为 图片序号.png
        cv2.imwrite("{}.png".format(img_count), frame)
        print("截图，并保存为  {}.png".format(img_count))
        # 图片编号计数自增1
        img_count += 1

# 释放VideoCapture
cap.release()
# 销毁所有的窗口
cv2.destroyAllWindows()
