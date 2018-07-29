# -*- coding:utf-8 -*-
'''
人脸识别FaceDetection
通过HaarCascade模型，进行人脸识别与眼睛识别，在视频流中绘制矩形，标识人脸
'''
import cv2

# 载入人脸检测的Cascade模型
FaceCascade = cv2.CascadeClassifier('./haar/haarcascade_frontalface_default.xml')

# 载入带有人脸的图片
img = cv2.imread('face.png')
# 将彩色图片转换为灰度图
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 创建一个窗口 名字叫做Face
cv2.namedWindow('Face',flags=cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO | cv2.WINDOW_GUI_EXPANDED)

# 检测画面中的人脸
faces = FaceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5
)

# 遍历返回的face数组
for face in faces:
    # 解析tuple类型的face位置数据
    # (x, y): 左上角坐标值
    # w: 人脸矩形区域的宽度
    # h: 人脸矩形区域的高度
    (x, y, w, h) = face
    # 在原彩图上绘制矩形
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 4)

# 在窗口Face上面展示图片img
cv2.imshow('Face', img)
# 等待任意按键按下
cv2.waitKey(0)
# 关闭所有的窗口
cv2.destroyAllWindows()