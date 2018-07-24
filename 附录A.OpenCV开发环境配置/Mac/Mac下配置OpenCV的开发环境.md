# Mac下配置OpenCV的开发环境



作者：国家弟震菊

编辑：阿凯-1Z实验室



 ![dizhenju](/home/zr/%E6%96%87%E6%A1%A3/OpenCV-1ZLab/%E9%99%84%E5%BD%95A.OpenCV%E5%BC%80%E5%8F%91%E7%8E%AF%E5%A2%83%E9%85%8D%E7%BD%AE/Mac/image/dizhenju.jpg)

> 阿凯说： @国家弟震菊 是我的大学同学，专业是电子信息， 目前在杭电读研。
>
> 同时，他还是一个CG（电脑绘图）大师哦， 大家可以在B站上看到他录制的CG教学视频。
>
> [B站-国家弟震菊](https://space.bilibili.com/14002349)

## 概要

本文适合于有一台`macbook pro`,并且没有安装ubuntu虚拟机, 同时又想学习opencv的同学。

然后恭喜各位, **mac环境配置opencv极其简单**,甚至不需要在终端输入任何一条安装代码,只要跟着本文的指导一
步一步往下做,就可以配置成功。



## 目录

OpenCV开发环境配置流程主要分一下三步

1. [安装Python3.6（Anaconda）](#1安装python3)
2. [安装OpenCV](#2安装OpenCV)
3. [安装PyCharm （IDE）](3安装PyCharm)



## 1安装python3

 mac自带python2.7，但是最新的opencv不支持python2.7了，所以最好的办法就是安装python3.6，非常简单。

首先去 [Anaconda官网下载-MacOS版本的Anaconda](https://www.anaconda.com/download/#macos), 选择`python3.6 version`下载。



![mac-01](/home/zr/文档/OpenCV-1ZLab/附录A.OpenCV开发环境配置/Mac/image/mac-01.png)

![mac-02](/home/zr/文档/OpenCV-1ZLab/附录A.OpenCV开发环境配置/Mac/image/mac-02.png)

下载完成以后得到安装包,双击即可
然后一路`next`即可,大概会占用你2个多G的空间,**但是会节省你很多的时间.**



![mac-03](/home/zr/文档/OpenCV-1ZLab/附录A.OpenCV开发环境配置/Mac/image/mac-03.png)

安成以后得到**图标**, `python3.6`也安装好了了.

![mac-04](/home/zr/文档/OpenCV-1ZLab/附录A.OpenCV开发环境配置/Mac/image/mac-04.png)



打开**终端Terminal** (mac的终端在lanuchpad ->其他)

在终端中输入:

```bash
python -V
```



如果显示`python 3.6.?` 那么恭喜,python3.6已经安装成功了。



![mac-05](/home/zr/文档/OpenCV-1ZLab/附录A.OpenCV开发环境配置/Mac/image/mac-05.png)



## 2安装OpenCV

打开刚才安装的`anacond-Navigator`

![mac-04](/home/zr/文档/OpenCV-1ZLab/附录A.OpenCV开发环境配置/Mac/image/mac-04.png)



![mac-06](/home/zr/文档/OpenCV-1ZLab/附录A.OpenCV开发环境配置/Mac/image/mac-06.png)



> 因为我在根目目录已经安装了了opencv,所以我新建了一个环境来展示,图省事的同学可以直
>
> 接在base(root)中安装



选择` Environments—>Not installed—>搜索opencv`
选择`py-opencv`下载,期间会提醒你安装一系列列的包,静静地等待安装完成。 



![mac-07](/home/zr/文档/OpenCV-1ZLab/附录A.OpenCV开发环境配置/Mac/image/mac-07.png)

安装完成以后 你可以在installed 中找到了了py-opencv,这时候打开终端,先输入入python进入python
操作界面面输入

```python
import cv2
```

 如果没有跳出错误,再输入

```python
cv2.version
```

弹出` 3.4.1`那说明opencv已经成功安装了。

![mac-08](/home/zr/文档/OpenCV-1ZLab/附录A.OpenCV开发环境配置/Mac/image/mac-08.png)



## 3安装PyCharm

pycharm是一款很专为python开发的ide,会为python开发提供很多的便利。
首先进入官网并且下载mac版pytharm

[PyCharm下载网址](https://www.jetbrains.com/pycharm/)

https://www.jetbrains.com/pycharm/

![mac-09](/home/zr/文档/OpenCV-1ZLab/附录A.OpenCV开发环境配置/Mac/image/mac-09.png)

有专业版和社区版,我们下载社区版就好了.

> ps: 因为专业版本需要收费啦， 对于初学者，专业的功能你暂时也用不到。

至于安装过程,非常容易,就不一一叙述了。安装成功后打开pycharm。

新建工程`Create New Project`, 给工程起个名字。

![mac-10](/home/zr/文档/OpenCV-1ZLab/附录A.OpenCV开发环境配置/Mac/image/mac-10.png)



![mac-11](/home/zr/文档/OpenCV-1ZLab/附录A.OpenCV开发环境配置/Mac/image/mac-11.png)

然后新建一个python的脚本文件， 例如`opencv-demo.py`。

![mac-12](/home/zr/文档/OpenCV-1ZLab/附录A.OpenCV开发环境配置/Mac/image/mac-12.png)

随便输入一个简单的opencv测试程序。例如

> 运行脚本之前， 请找一个png图片， 重命名为`demo.png` 然后拖动在工程里面， 跟py文件放置在同一路径下。

``opencv-demo.py`

```python
# -*- coding: utf-8 -*-  
import cv2
# 读入图片
img = cv2.imread('demo.png')
# 创建窗口并展示图片
cv2.imshow('image', img)
# 等待任意一个按键按下
cv2.waitKey(0)
# 关闭所有的窗口
cv2.destroyAllWindows()
```



>  如果发现有红色色线条提示有问题,不用在意。

然后执行`run` 。

> 运行按钮是右上角的绿色三角形。



![mac-13](/home/zr/文档/OpenCV-1ZLab/附录A.OpenCV开发环境配置/Mac/image/mac-13.png)

果然出错了,提示说**没有cv2 这个模块**,这是因为pycharm并不知道从哪里导入这个cv2,所
以还需要**为pycharm配置opencv环境**. 



> 下面是一系列图片,根据图片中的信息操作,肯定不会出问题: 



1. 选择`file -> defaults Settings`  修改默认设置。

![mac-14](/home/zr/文档/OpenCV-1ZLab/附录A.OpenCV开发环境配置/Mac/image/mac-14.png)

2. 选择左边侧边栏的`Project Interpreter` 项目的**脚本解释器配置**。

   默认的是python2.7,所以肯定不对,选择` Add Local` , **添加本地的Python路径**。

   

![mac-15](/home/zr/文档/OpenCV-1ZLab/附录A.OpenCV开发环境配置/Mac/image/mac-15.png)



3. 选择`Existing environment` ， 找到你**anaconda3的安装目录**,根据图片里面的位置找到最终的python文件,ok即可.

![mac-16](/home/zr/文档/OpenCV-1ZLab/附录A.OpenCV开发环境配置/Mac/image/mac-16.png)



现在python版本变成了`3.6`,还多了很多的包,这就是anaconda3配置出来的Python科学计算开发环境。

![mac-17](/home/zr/文档/OpenCV-1ZLab/附录A.OpenCV开发环境配置/Mac/image/mac-17.png)

然后选择 `run ->EditConfigurations`

> 运行环境配置在IDE的右上角。

![mac-19](/home/zr/文档/OpenCV-1ZLab/附录A.OpenCV开发环境配置/Mac/image/mac-19.png)

选择我们刚刚弄出来的`python3.6`,然后点击`ok`,就可以运行程序了。

![mac-20](/home/zr/文档/OpenCV-1ZLab/附录A.OpenCV开发环境配置/Mac/image/mac-20.png)



![mac-18](/home/zr/文档/OpenCV-1ZLab/附录A.OpenCV开发环境配置/Mac/image/mac-18.png)