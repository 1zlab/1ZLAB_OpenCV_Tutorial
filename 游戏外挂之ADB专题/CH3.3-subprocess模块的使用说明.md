
# 凡哥OpenCV基础入门教程（跳一跳专题）-CH3.3-subprocess模块的使用说明

> 原创文章，转载请注明出处！！

> 本文为【凡哥原创教程】VIP教程节选，欢迎加入技术交流群了解会员制度（QQ：627671914）

## 0. 概要

subproces用于执行外部命令，是os.fork() 和 os.execve() 的封装。如果我们想在python中执行命令行就需要借助subprocess 模块。后面实战部分，凡哥带你利用subprocess 封装adb指令，用于我们的跳一跳程序与Android手机交互。

![subprocess](http://image.myfange.com/subprocess.png-fg)

## 1. 引入subprocess模块

```python
import subprocess
```

## 2. subprocess.call

如果我们想执行一个shell指令， 同时又不关心他的**标准输出 stdout**， 例如`cp demo.txt demo-cp.txt` 复制一个文件，复制`demo.txt` 为`demo-cp.txt`.

有三种方式可以实现这个功能。

**方法1：传入数组**

```python
subprocess.call(['cp', 'demo.txt', 'demo-cp.txt'])
```

**方法2：shell=True**

```python
subprocess.call('cp demo.txt demo-cp.txt', shell=True)
```

**方法3：借助shlex模块**

我们引入`shlex` 模块， 调用其`split`方法， 可以将字符串按照shell的方式将其分割成数组。 本质上跟方法1是相同的。

```python
import shlex
cmd = 'cp demo.txt demo-cp.txt'
subprocess.call(shlex.split(cmd))
```

**返回码return code**

我们如何才能知道代码有没有被正确执行呢？`subprocess.call`函数返回一个整数，我们称之为 `return code` , 用来表示指令有没有正确执行。

```python
code = subprocess.call(['cp', 'demo.txt', 'demo-cp.txt'])
```

如果`code==0` 说明程序正确执行， 没有报错。

如果`code!=0 ` 说明运行过程中存在问题(ERROR)

## 3. subprocess.Popen

在subprocess中，子进程的创建与管理交由`Popen`类。

`call()` 其实是对`Popen` 的简化封装。 如果我们想自定义， 想获取标准输出， 标准错误就需要凭借`Popen`.

```python
p = subprocess.Popen(["echo", "hello world"], stdout=subprocess.PIPE)
```

python 与进程的交互我们要借助Popen的`communicate`函数。返回的是一个tuple类型。

```python
stdout, stderr = p.communicate()
```

第一个是标准输出， 第二是标准错误。

```python
print(p.communicate())
```

输出

```
>>>('hello world', None)
```

如何判断是否正确执行， 我们可以获取Popen的

```
p.returncode
```

如果`p.returncode==0` 代表程序正确执行。`p.returncode==1` 代表程序出现错误。

## 4. 实战:ADBHelper

我们在`CH3.1` 中介绍了ADB获取截图跟模拟点击的命令行。 

这里我就要教大家用python实现执行ADB命令行的程序。

### 4.1 模块导入

```python
import subprocess
from subprocess import Popen, PIPE
import shlex
import cv2
import random
```

### 4.2 init构造器函数

因为我们要模拟点击手机屏幕， 需要确定屏幕像素 屏幕高度跟屏幕宽度。

`margin` 指的是离屏幕边缘多少不点击， 边距的意思。

你可以获取一张截图， 然后打印一下图像的信息。确定高度跟宽度。

```python
class ADBHelper:
	def __init__(self, win_width, win_height, margin = 100):
        self.win_width = win_width
        self.win_height = win_height
        # 可以按压的矩形区域 内缩 margin个像素点。
        # 因为屏幕上的边缘 点击会触发别的事件
        # region = (x, y, width, height)
        self.press_region = (margin, margin, win_width-margin, win_height-margin)
```

### 4.3 获取截图getScreebShotByADB

```shell
adb shell screencap -p
```

这个指令的标准输出是png图片的字节流。 

我们需要将字节流存储到`png`文件中。

```python
f = open("tmp.png", "wb")
f.write(output)
```

`w` 代表write写，`b` 代表字节流模式。

```python
cv2.imread("tmp.png")
```

利用opencv读取png图片。 `tmp.png`就类似中间媒介。

**函数**

```python
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
```

### 4.4 模拟点击

模拟点击比较简单， 使用的是`subprocess.call` 函数。

后面添加了随机点击的事件， 而不是固定在一个地方点击。

```python
@staticmethod
def pressOnScreen(ptr1, delay=500):
    '''
        在屏幕上按压 带延时
    '''
    return ADBHelper.pressOnScreenAndMove(ptr1, ptr1, delay)

@staticmethod
def pressOnScreenAndMove(ptr1, ptr2, delay=500):
    # 'adb shell input touchscreen swipe 170 187 170 187 2000'
    cmd = 'adb shell input touchscreen swipe {} {} {} {} {}'.format(ptr1[0], ptr1[1], ptr2[0], ptr2[1], delay)
    # 运行指令
   	rc = subprocess.call(shlex.split(cmd))
    return rc == 0

def randPressOnScreen(self, delay=500):
    # 在屏幕上的可按压区域随意选取一个区域， 进行按压
    (x, y, w, h) = self.press_region
    cx = random.randint(x, x + w)
    cy = random.randint(y, y + h)
    print("Press On  x=%d y=%d , time=%.2f"%(cx, cy, delay))
    return ADBHelper.pressOnScreen((cx, cy), delay)
```

### 4.5 完整源代码

`ADBHelper.py`

源代码看我的github仓库：

https://github.com/mushroom-x/FGJumperMaster/blob/master/ADBHelper.py

## 5. Reference

[python-subprocess 官方文档](https://docs.python.org/3.6/library/subprocess.html#module-subprocess)

https://docs.python.org/3.6/library/subprocess.html

![](http://image.myfange.com/微信公众号底部.png-bk)