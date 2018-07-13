
# 凡哥OpenCV基础入门教程（跳一跳专题）-CH3.4-实战篇 手动模式玩跳一跳

> 原创文章，转载请注明出处！！

> 本文为【凡哥原创教程】VIP教程节选，欢迎加入技术交流群了解会员制度（QQ：627671914）

## 0. 概要

前阶段CH1一直到CH3, 我们学会了图像的基本操作,学会了HighGUI键盘事件与鼠标事件的监听, 然后学了绘图相关的操作. CH3前面的部分都是在介绍如何使用ADB以及用subprocess模块调用ADB对手机屏幕截图与按压屏幕模拟. 是时候实战一波了.

凡哥给大家做好了手动模式版本玩跳一跳的源代码与使用教程, 好好研读代码哦.

## 1. 代码使用说明

### 1.1 创建一个文件夹用于存放样本

你可以在代码根目录创建一个文件夹名字叫做`label`  或者起另外的名字.

### 1.2  修改代码中的样本存放路径

修改文件`markSampleLabelFromPhone.py`

根据step1中选择的文件夹修改对应的值.

```python
# 图片保存路径 使用前先创建此文件夹/更新此参数
save_path = "./label/"
# 样本标注信息文件名 使用前先创建此文件/更新此参数
label_filename = "./label/labels.txt"
slabel = SampleLabel(save_path, label_filename)
```

### 1.3 设定手机屏幕分辨率

修改文件`markSampleLabelFromPhone.py`

```python
# 初始化 ADBHelper, 填入手机屏幕宽度跟高度. (宽度,高度)
adb = ADBHelper(1080, 1920)
```

> ? 如何才能知道自己屏幕的分辨率

我在`CH1.1` 中就讲解了如何获取图像属性. [CH1.1_读入图片并显示图片的相关属性](http://www.myfange.com/p/opencv-imread-propoerty)

你可以利用ADB命令行读入一张图片, 然后获取其属性.

### 1.4 修改距离转变为时间的ratio

你可以根据你的手机分辨率与实际跳跃效果调大或者调小`ratio`.

```python
# 将距离转换成时间
def distance2time(distance):
    ratio = 1.53
    # 时间必须是整数类型
    return int(distance * ratio)
```

### 1.5 打开ADB 服务器

**连接手机.**

启动adb server

```bash
scorpion@tl ~/D/f/CH3_图像采集与样本标注> sudo adb start-server
[sudo] password for scorpion: 
* daemon not running; starting now at tcp:5037
* daemon started successfully
```

手机端选择USB模式 这里我们要选择**传输照片模式**, 我这里是PTP,　你的手机可能是MTP

**默认是USB供电** 

![open_ptp_on_android.png](http://image.myfange.com/open_ptp_on_android.png-fg)

查看一下设备列表

```bash
scorpion@tl ~/D/f/CH3_图像采集与样本标注> adb devices
List of devices attached
a9e0d12a        device

```

说明正确连接手机．

**详细步骤见CH3.1的使用说明．**

### 1.6 运行主程序

手机端打开跳一跳的小程序.

进入代码主目录，执行

```bash
python markSampleLabelFromPhone.py
```

如果有些帧不是你想要的, 或者游戏过程中的中间画面, 按`n` 键, 更新画面

![Screenshot_20180202_102354.png](http://image.myfange.com/Screenshot_20180202_102354.png-fg)

### 1.7 查看帮助工具

点击窗口，按h键，就可以看到帮助信息．

```
标注工具-帮助菜单
==================================
键盘 n - next 下一张图片 需要手动更新!!!
键盘 c - cancel 撤销标注
键盘 s - save 保存样本标注与跳跃
键盘 h - help 帮助菜单
键盘 e - exit 保存标记并退出系统
```

### 1.8 标注两点然后跳跃

首先标注棋子底部，用红色点表示.

![Screenshot_20180202_102647.png](http://image.myfange.com/Screenshot_20180202_102647.png-fg)

接下来我们再标注盒子中心．

![Screenshot_20180202_102956.png](http://image.myfange.com/Screenshot_20180202_102956.png-fg)

你可以选择撤销标注, 更新画面, 按`c`键.

确定标注, 保存样本图片并跳跃按`s`键.

中间你可能会遇到这种半截的图片.

![Screenshot_20180202_103423.png](http://image.myfange.com/Screenshot_20180202_103423.png-fg)

按`n` next ,切换到下一张图片. **哈哈, 我知道你有更好的办法, 去改代码吧.**

更新后, 就会显示成这样, 往复执行.

![Screenshot_20180202_103827.png](http://image.myfange.com/Screenshot_20180202_103827.png-fg)

**人有多大胆, 地有多大产.**  

基本上我玩到300多就已经手抖了. 大家还是不要沉迷,以采集样本为根本目的, 见好就收.

![2018-02-01-19-07-17-425189.png](http://image.myfange.com/2018-02-01-19-07-17-425189.png-fg)

### 1.9 查看标注样本

我们可以看到文件夹中采集的图片, 然后还有对应的日志.

![Screenshot_20180202_104828.png](http://image.myfange.com/Screenshot_20180202_104828.png-fg)

关键代码如下

```python
def label2string(self):
    '''
        将标签转换为字符串, 用于保存在label.txt中
    '''
    (x1, y1) = self.fchess
    (x2, y2) = self.cbox
    return ",".join([self.img_name, str(x1), str(y1), str(x2), str(y2)]) + '\n'
```

日志结构, 第一个元素是图片名称(采用时间戳生成), 接下来是棋子底部中心的x坐标与y坐标

接下来是跳一跳盒子的中心x坐标与y坐标.

## 2. 源代码

### 2.1 `SampleLabel.py`

```python
'''
程序说明:
    程序类用于通过鼠标手动标注两个关键点坐标
    1. 棋子中心
    2. 下一跳盒子的中心
'''

import cv2
import numpy as np
import datetime
import math
import copy
from ADBHelper import ADBHelper

# MP : Mark Process 标注过程
MP_UNMARK = 0 # 0 : 未进行标注
MP_MARKED_FCHESS = 1  # 1 : 标注了小人的底部
MP_MARKED_CBOX = 2 # 2 : 标注了box的中心点

'''
手动标注 两个标签

'''
def markChessAndBoxByHand(event,x,y,flags,sampleLabel):
    
    if event == cv2.EVENT_LBUTTONDOWN:
        print("click: x= {}, y={}".format(x, y))
        sampleLabel.addLabel(x, y)
    
class SampleLabel:
    def __init__(self, save_path='./', label_filename='label.txt'):
        self.img = None # 原来的图片
        self.canvas = None # 画布
        self.img_name = None # 图片名称
        self.mp = 0 # 标注的进程 mark process
        self.fchess = (0, 0) # 棋子底部中心
        self.cbox = (0, 0) # 下一条盒子的中心
        self.save_path = save_path # 图像的保存路径
        self.label_filename = label_filename #　标签记录文件的文件名
        # self.label_file = open(label_filename, 'w+') # 文件对象
        self.winname = 'label'
        
        # 创建一个窗口
        cv2.namedWindow(self.winname, flags= cv2.WINDOW_NORMAL | cv2.WINDOW_FREERATIO)
        # 设置鼠标事件的回调函数
        cv2.setMouseCallback(self.winname, markChessAndBoxByHand, self)

    def updateImg(self, img, img_name = None):
        # 更新当前源图像 - 深度拷贝
        self.img = img.copy()
        # 更新画布 - 深度拷贝
        self.canvas = img.copy()
        # 重置 棋子底部坐标
        self.fchess = (0, 0)
        # 重置盒子的中心
        self.cbox = (0, 0)

        if img_name == None:
            # 根据时间戳　生成文件名
            self.img_name = f"{datetime.datetime.now():%Y-%m-%d-%H-%M-%S-%f.png}"
        else:
            # 如果有名字的话就直接赋值
            self.img_name = img_name

        # 重置标注状态
        self.mp = MP_UNMARK
        # 更新画布
        self.updateCanvas()

    def printProcessOnCanvas(self, info):
        '''
            在画布上显示帮助信息
        '''
        # 首先更新画布
        # self.updateCanvas()
        self.canvas[50:150,:] = 255
        # 选择字体
        font = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 1
        cv2.putText(self.canvas, text=info, org=(100, 100), fontFace=font, fontScale=fontScale, thickness=1, 
                     lineType=cv2.LINE_AA, color=(0, 0, 255))
        
        cv2.imshow(self.winname, self.canvas)

    def updateCanvas(self):
        '''
            根据状态更新画布　与文字提示
        '''
        # Use Deep Copy
        self.canvas = self.img.copy()

        rmarker = 10 # 标记半径
        if self.mp >= MP_MARKED_FCHESS:
            # 绘制chess中心
            # 绘制棋子底部的中心点 红色实心
            cv2.circle(img=self.canvas, center=self.fchess, radius=rmarker, color=(0, 0, 255), thickness=-1)
            
        if self.mp >= MP_MARKED_CBOX:
            # 绘制下一条盒子中心
            cv2.circle(img=self.canvas, center=self.cbox, radius=rmarker, color=(0, 255, 0), thickness=-1)

        if self.mp == MP_UNMARK:
            self.printProcessOnCanvas("step-0 unmarked, mark chess footer first.")

        elif self.mp == MP_MARKED_FCHESS:
            self.printProcessOnCanvas("step-1  you need to mark next box center.") 
    
        elif self.mp == MP_MARKED_CBOX:
            self.printProcessOnCanvas("step-2 mark done, save (s) or cancel (u)")
        
        cv2.imshow(self.winname, self.canvas)
        
    def addLabel(self, x, y):
        '''
            添加标签
        '''
        if self.mp == MP_UNMARK:
            # 当前标注的是棋子脚底
            self.fchess = (x, y)
            # 更新状态码
            self.mp = MP_MARKED_FCHESS
        
        elif self.mp == MP_MARKED_FCHESS:
            # 当前标注的是盒子的中心
            self.cbox = (x, y)
            # 更新状态码
            self.mp = MP_MARKED_CBOX
        else:
            print("标注已完成")

        '''
        # 打印标注信息
        print("fchess")
        print(self.fchess)
        print("cbox")
        print(self.cbox)
        print("mp")
        print(self.mp)
        '''
        self.updateCanvas()
        
    def isMarkDone(self):
        '''
            返回是否标注完成
        '''
        return self.mp == MP_MARKED_CBOX

    def saveImg(self):
        '''
            保存图片
        '''
        # 保存样本素材
        cv2.imwrite(self.save_path + self.img_name, self.img)
        # 保存标注后的图片
        cv2.imwrite(self.save_path + 'log/' + self.img_name, self.canvas)

    def label2string(self):
        '''
            将标签转换为字符串, 用于保存在label.txt中
        '''
        (x1, y1) = self.fchess
        (x2, y2) = self.cbox
        return ",".join([self.img_name, str(x1), str(y1), str(x2), str(y2)]) + '\n'
    
    def saveLabelInfo(self):
        '''
            添加标注信息 追加模式
        '''
        with open(self.label_filename, 'a+') as f:
            f.write(self.label2string())
        
    def onDestroy(self):
        # 关闭窗口
        cv2.destroyWindow(self.winname)
```

### 2.2 `ADBHelper.py`

```python
'''
    在Python中执行ADB的命令行, 实现对Android设备的操控
'''

from subprocess import Popen, PIPE
import shlex
import cv2
import random
import subprocess

class ADBHelper:
    
    def __init__(self, win_width, win_height, margin = 100):
        '''
            构造器函数
            确认 窗口宽度高度与可按压范围.
        '''
        self.win_width = win_width
        self.win_height = win_height
        # 可以按压的矩形区域 内缩 margin个像素点。
        # 因为屏幕上的边缘 点击会触发别的事件        # region = (x, y, width, height)
        self.press_region = (margin, margin, win_width-margin, win_height-margin)
    @staticmethod
    def getScreenShotByADB():
        '''
            在手机上截图并返回opencv格式的ndarray
        '''
        # ADB截图的命令
        cmd = "adb shell screencap -p"
        # 运行指令
        p = Popen(shlex.split(cmd), stdin=PIPE, stdout=PIPE, stderr=PIPE)        
        # output与err返回的均是字节
        output, err_info = p.communicate()
        rc = p.returncode

        '''
            Return Code:
                0: 读取成功
                1: 读取失败
        '''
        if rc == 1:
            # 截图读取失败
            print("截图读取失败")
            print("ERROR INFO")
            # 打印报错信息
            print(err_info)
            return None
        # 先写入文件 tmp.png
        f = open("tmp.png", "wb")
        f.write(output)
        # 使用opencv读取图片 返回ndarray
        return cv2.imread("tmp.png")
    
    @staticmethod
    def pressOnScreen(ptr1, delay=500):
        '''
            在屏幕上按压 带延时
        '''
        return ADBHelper.pressOnScreenAndMove(ptr1, ptr1, delay)

    @staticmethod
    def pressOnScreenAndMove(ptr1, ptr2, delay=500):
        '''
            按压屏幕并且移动
        '''
        # 命令样例: 'adb shell input touchscreen swipe 170 187 170 187 2000'
        cmd = 'adb shell input touchscreen swipe {} {} {} {} {}'.format(ptr1[0], ptr1[1], ptr2[0], ptr2[1], delay)

        # 运行指令
        rc = subprocess.call(shlex.split(cmd))

        return rc == 0
    
    def randPressOnScreen(self, delay=500):
        '''
            在屏幕上的可按压区域随意选取一个区域， 进行按压
        '''
        (x, y, w, h) = self.press_region

        cx = random.randint(x, x + w)
        cy = random.randint(y, y + h)
        print("Press On  x=%d y=%d , time=%.2f"%(cx, cy, delay))
        return ADBHelper.pressOnScreen((cx, cy), delay)

```

### 2.3 `markSampleLabelFromPhone.py`

```python
'''
程序说明:
    从ADB中读取手机截图,并通过鼠标标注点, 保存标注文件
'''
import cv2
import numpy
import math
import os

# 样本标注
from SampleLabel import SampleLabel
# 凡哥写的ADBHelper类
from  ADBHelper import ADBHelper

# 图片保存路径 使用前先创建此文件夹/更新此参数
save_path = "./label/"
# 样本标注信息文件名 使用前先创建此文件/更新此参数
label_filename = "./label/labels.txt"

slabel = SampleLabel(save_path, label_filename)

# 初始化 ADBHelper, 填入手机屏幕宽度跟高度.
adb = ADBHelper(1080, 1920)

# 将距离转换成时间
def distance2time(distance):
    ratio = 1.53
    # 时间必须是整数类型
    return int(distance * ratio)

# 计算两点之间的距离
def cal_distance(pt1, pt2):
    '''
        获取棋子与下一跳盒子的距离
    '''
    (x1, y1) = pt1
    (x2, y2) = pt2
    return math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))

# 更新下一张图片 从ADB读入
def nextImg(slabel):
    '''
        使用迭代器， 遍历数组
    '''
    global adb
    try:
        # 从ADB读入图片
        img = adb.getScreenShotByADB()
        # 确认图片是否成功读入
        if img is None:
            return False
        else:
            slabel.updateImg(img, img_name=None)
            
            # 读入就将原来 unlabel的文件删除
        return True
    except StopIteration:
        print("遍历结束")
        return False

# 初始读入第一个
nextImg(slabel)
while True:
    keyValue = cv2.waitKey(0)
    # slabel.responseToKeyEvent(k, img=img)

    if keyValue == ord('e'):
        print('销毁窗口并保存')
        # 关闭窗口
        slabel.onDestroy()
        break

    elif keyValue == ord('n'):
        print("跳过，下一张图片")
        if not nextImg(slabel):
            # 如果获取失败， 退出
            break
    elif keyValue == ord('c'):
        print("取消标注")
        # update frame
        slabel.updateImg(slabel.img)

    elif keyValue == ord('s'):
        print("保存")
        if slabel.isMarkDone():
            # 保存样本
            slabel.saveImg()
            # 保存样本标注信息
            slabel.saveLabelInfo()
            # 显示提示信息 : 保存完成
            slabel.printProcessOnCanvas("Save Done")
            # 随机点击屏幕, 设置对应的延时时间.
            delay_time = distance2time(cal_distance(slabel.cbox, slabel.fchess))

            # 这里可以添加个延时
            # TODO

            adb.randPressOnScreen(delay_time)
            
            # 显示提示信息 : 自动载入下一张图片
            if not nextImg(slabel):
                # 如果获取失败， 退出
                break
        else:
            # 标注未完成， 无法保存
            slabel.printProcessOnCanvas("Error: mark undone, could not save")

    elif keyValue == ord('h'):

            print('''
            标注工具-帮助菜单
            ==================================
            键盘 n - next 下一张图片 需要手动更新!!!
            键盘 c - cancel 撤销标注
            键盘 s - save 保存样本标注与跳跃
            键盘 h - help 帮助菜单
            键盘 e - exit 保存标记并退出系统
            ''')
```

## 3. 作业CH3.4

如果给你提供一系列没有标注的图片, 例如你搜集的样本图片, 搜集的时候并没有标注

你有什么办法可以读取文件夹中的图片,并且生成我们`label.txt`的标注文本么?

这跟`markSampleLabelFromPhone.py` 类似, 只不过文件读取来源由通过ADB读取截图变成了从文件中读取截图.

这跟CH3.1的作业, 其实很像. 

你可以在凡哥的代码`SampleLabel.py` 基础上调用并实现, 也可以从0开始写自己的实现代码.

![](http://image.myfange.com/微信公众号底部.png-bk)