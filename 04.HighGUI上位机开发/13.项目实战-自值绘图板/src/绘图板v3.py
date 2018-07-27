# -*- coding: utf-8 -*-
'''
 鼠标按下绘制线条 可以调整线条粗细 变换颜色
 线条也更流畅
'''
import cv2
import numpy as np  

isMouseLBDown = False # 判断鼠标是否摁下的标志
circleColor = (0, 0, 0) # 画笔的颜色
circleRadius = 5 # 画笔的粗细
lastPoint = (0, 0)

# 鼠标回调函数  绘制图像 
# x, y 都是相对于窗口内的图像的位置
def draw_circle(event,x,y,flags,param): 
    # 判断事件是否为 Left Button Double Clicck 
    # print(event)
    global img
    global isMouseLBDown
    global color
    global lastPoint
    
    if event == cv2.EVENT_LBUTTONDOWN:
        # 检测到鼠标左键按下
        # print("mouse down")
        isMouseLBDown = True
        cv2.circle(img,(x,y), int(circleRadius/2), circleColor,-1)
        lastPoint = (x, y)
    elif event == cv2.EVENT_LBUTTONUP:
        # 检测到鼠标左键抬起
        isMouseLBDown = False
        # print("mouse up")
    elif event == cv2.EVENT_MOUSEMOVE:
        if isMouseLBDown:
            # print("drawing")
            cv2.line(img, pt1=lastPoint, pt2=(x, y), color=circleColor, thickness=circleRadius)
            lastPoint = (x, y)
            # cv2.circle(img,(x,y), circleRadius, circleColor,-1)

# 更新颜色
def updateCircleColor(x):
    global circleColor
    global colorPreviewImg

    r = cv2.getTrackbarPos('Channel_Red','image')
    g = cv2.getTrackbarPos('Channel_Green','image')
    b = cv2.getTrackbarPos('Channel_Blue','image')

    circleColor = (b, g, r)
    colorPreviewImg[:] = circleColor

# 更新画笔的宽度
def updateCircleRadius(x):
    global circleRadius
    global radiusPreview

    circleRadius = cv2.getTrackbarPos('Circle_Radius', 'image')
    # 重置画布
    radiusPreview[:] = (255, 255, 255)
    # 绘制圆形
    cv2.circle(radiusPreview, center=(50, 50), radius=int(circleRadius / 2), color=(0, 0, 0), thickness=-1)

# 创建一个画布，并绑定窗口和鼠标回调函数

img = np.ones((512,512,3), np.uint8)
img[:] = (0, 0, 0)

# 用于预览画笔的颜色
colorPreviewImg = np.ones((100, 100, 3), np.uint8)
colorPreviewImg[:] = (0,  0, 0)
# 用于预览画笔的粗细
radiusPreview = np.ones((100, 100, 3), np.uint8)
radiusPreview[:] = (255, 255, 255)

# 用于展示绘图区域的窗口
cv2.namedWindow('image')
# 用于预览颜色的窗口
cv2.namedWindow('colorPreview')
# 用于预览画笔宽度的窗口
cv2.namedWindow('radiusPreview')

# 在window‘image’ 上创建一个滑动条，起名为Channel_XXX， 设定滑动范围为0-255, 
# onChange事件回调 啥也不做
cv2.createTrackbar('Channel_Red','image',0,255,updateCircleColor)
cv2.createTrackbar('Channel_Green','image',0,255,updateCircleColor)
cv2.createTrackbar('Channel_Blue','image',0,255,updateCircleColor)

cv2.createTrackbar('Circle_Radius','image',1,20,updateCircleRadius)
# 设置鼠标事件回调
cv2.setMouseCallback('image',draw_circle)  

while(True):
    cv2.imshow('colorPreview', colorPreviewImg)
    cv2.imshow('radiusPreview', radiusPreview)
    cv2.imshow('image',img)  
    if cv2.waitKey(1) == ord('q'):  
        break

cv2.destroyAllWindows()
cv2.imwrite("MousePaint03.png",  img)
