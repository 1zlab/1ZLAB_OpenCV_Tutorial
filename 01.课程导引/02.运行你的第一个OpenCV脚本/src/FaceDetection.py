# -*- coding:utf-8 -*-
'''
人脸识别FaceDetection
通过HaarCascade模型，进行人脸识别与眼睛识别，在视频流中绘制矩形，标识脸部跟眼睛。

TODO scalar部分  修改为 从frame中获取宽度跟长度
'''
import cv2

# 载入人脸检测的Cascade模型
FaceCascade = cv2.CascadeClassifier('./haar/haarcascade_frontalface_default.xml')
# 载入眼睛检测的Cascade模型
EyeCascade = cv2.CascadeClassifier('./haar/haarcascade_eye.xml')

# 载入视频流
cap = cv2.VideoCapture('face.mp4')
# 创建一个窗口 名字叫做Video
cv2.namedWindow('Video',flags=cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO | cv2.WINDOW_GUI_EXPANDED)

# 图像缩放系数
# why->降低分辨率，可以加快图像识别的速度，提高帧率
scalar = 5

while True:
    # 通过cap对象， 一帧一帧读入
    ret, frame = cap.read()
    # 获取
    height, width,_ = frame.shape
    # 对图像进行缩放
    # 分辨率从原来的 720 × 1280 缩放为 72 * 128
    # resize插值算法采用 INTER_CUBIC 算法
    frame_small =  cv2.resize(frame,(int(width/scalar),int(height/scalar)),interpolation=cv2.INTER_CUBIC)
    # 颜色空间变换，将彩图转换为灰度图
    gray = cv2.cvtColor(frame_small, cv2.COLOR_BGR2GRAY)
    # 检测画面中的人脸
    faces = FaceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5
    )

    # 在脸的周围画框框
    for (x, y, w, h) in faces:
        # 从缩放后的ROI，转换为缩放前的ROI
        x *= scalar
        y *= scalar
        w *= scalar
        h *= scalar
        # 绘制画面中人脸区域的矩形
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 4)    
        # 获取脸部区域的ROI图像
        # 而且仅需要在脸的上半部分检测眼睛
        face_roi = frame[y:y+int(h/2),x:x+w]
        # 将ROI图像转换为灰度图
        face_gray = cv2.cvtColor(face_roi, cv2.COLOR_BGR2GRAY)
        
        # 检测眼睛
        eyes = EyeCascade.detectMultiScale(
            face_gray,
            scaleFactor=1.1,
            minNeighbors=5
        )

        # 遍历返回的眼睛(eye)对象的ROI
        for (ex, ey, ew, eh) in eyes:
            # 绘制眼睛的方框
            cv2.rectangle(frame, (ex+x, ey+y), (ex+x+ew, ey+y+eh), (0, 0, 255), 4)
    
    # 更新Video窗口下的图像
    cv2.imshow('Video', frame)
    # 等待按键按下，如果1ms内没有按键的话，就跳过继续执行 
    # 判断按键是否为q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# 释放VideoCapture
cap.release()
# 关闭所有的窗口
cv2.destroyAllWindows()
