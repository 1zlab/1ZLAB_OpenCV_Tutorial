
# 凡哥OpenCV基础入门教程（跳一跳专题）-CH3.1-ADB安装过程与ADB部分指令介绍

> 原创文章，转载请注明出处！！

> 本文为【凡哥原创教程】VIP教程节选，欢迎加入技术交流群了解会员制度（QQ：627671914）

## 0. 概要

本期凡哥给大家简单介绍了什么是ADB, 以及ADB在不同操作系统的安装方法. 

以凡哥的小米5C为例,教大家Android设备打开USB调试功能的整个过程, 以及注意事项. 

课程的后面,凡哥教大家使用ADB指令对手机进行截屏, 录屏与模拟点击事件的操作.

![http://image.myfange.com/](http://image.myfange.com/ADB  the Android Debug   Google Search.jpeg-fg)

## 1. 何为ADB？

这里只是简单提一下什么是`ADB`， ADB全称为`Android Debug Bridge` 。 我们可以通过`ADB`用命令行的方式，在PC上向Android设备发送接收数据， 传送指令。 使用命令行模拟点击等事件。

因为凡哥没有做过Android相关的开发工作， 对`ADB`的理解也停留在概念上， 关于原理解析的部分。 大家可以参考简书的这篇文章。

[android adb介绍与命令大全-简书](https://www.jianshu.com/p/c4a6c9297b33)

> Android Debug Bridge，Android调试桥接器，简称ADB，是用于管理模拟器或真机状态的万能工具，通俗一点讲adb就是pc和移动设备通信的桥梁，它采用了c/s模型，包括三个部分：
>
> 1、客户端部分，运行在开发用的电脑上，可以在命令行中运行adb命令来调用该客户端，像ADB插件和DDMS这样的Android工具也可以调用adb客户端，需要说明的是客户端与手机或者模拟器是一对多的关系，也就是说不管连接多少设备客户端就只有唯一的一个实例存在。
>
> 2、服务端部分，是运行在开发用电脑上的后台进程，用于管理客户端与运行在模拟器或真机的守护进程通信。
>
> 3、守护进程部分，运行于模拟器或手机的后台（简称adb daemon）。
>
> 作者：Memebox链接：https://www.jianshu.com/p/c4a6c9297b33
>

**ADB的原理图**

[图片来源-Android adb实现原理](http://blog.csdn.net/ysh149216447/article/details/53334015)  

![20161125145815193.png](http://image.myfange.com/20161125145815193.png-fg)

![20180129-adb-theory.png](http://image.myfange.com/20180129-adb-theory.png-fg)


## 2. 及时答疑

### 2.1 不是说好USB摄像头么？ 凡哥你欺骗我的感情

哎呀， 本来是想用USB摄像头来着。。。

实话讲, 机械结构都做出来了， 就是一直没敢下手。

**整整花了两天做机械结构， 不说了， 都是泪**

![wlz_tiaoyitiao_01.jpg](http://image.myfange.com/wlz_tiaoyitiao_01.jpg-fg)

![wlz_tiaoyitiao_02.jpg](http://image.myfange.com/wlz_tiaoyitiao_02.jpg-fg)

当然， 图像我们也采集成功了。

图片来自于 [在VirtualBox虚拟机里使用Opencv获取USB摄像头的图像-凡哥带你配置OpenCV开发环境](http://www.myfange.com/p/virtualbox-opencv-usb-camera-video-capture)

![http://image.myfange.com/VisualBox%E6%8B%93%E5%B1%95%E7%9A%84%E4%B8%8B%E8%BD%BD%E4%B8%8E%E5%AE%89%E8%A3%85%E4%B8%8EUSB%E6%91%84%E5%83%8F%E5%A4%B4%E8%AF%BB%E5%8F%96_20180117213930.JPG-fg](http://image.myfange.com/VisualBox%E6%8B%93%E5%B1%95%E7%9A%84%E4%B8%8B%E8%BD%BD%E4%B8%8E%E5%AE%89%E8%A3%85%E4%B8%8EUSB%E6%91%84%E5%83%8F%E5%A4%B4%E8%AF%BB%E5%8F%96_20180117213930.JPG-fg)

最大的问题就在于，点击这个部分.

1. 锡箔纸，**容易划伤屏幕**。舵机万一用力，那就出现奇迹了不是。  
2. 物理点击**效果不稳定**，经常点击不到, 或者有延时。
3. **图像质量**， 从USB摄像头获取的图像， 畸变比较明显。 这块问题的处理， 凡哥打算在下个课程中好好给大家讲解， 如何标定摄像头， 去除图像畸变。 

所以啊， 在这个问题里面， 凡哥觉得我们 **用ADB挺好，稳定安全。** 我们要安全开车。

### 2.2 你让苹果手机用户怎么想？

这个啊，IOS应该也有对应的debug模式与命令行。 无奈凡哥没用过啊，大家可以自行搜索。 

如果配置好了， 写成教程分享在群里， 凡哥也会很感激的。

## 3. 打开手机的USB调试模式

### 3.1 找到隐藏的开发者选项

这块的内容呢， 是最蛋疼的。 国内各个手机厂商都会修改自定制Android操作系统。 你的手机型号对应的操作方式呢， 请自行百度。

因为凡哥的手机是小米`5c`, 所以就用这个来演示一下。 目前我的版本是`MIUI9.1` 

![xiaomi5c.jpg](http://image.myfange.com/mi-5c-review.jpg-fg)

`小米5c ` 的开发者选项，默认是隐藏的， 即便你点击进入设置页， 你也看不到这个选项。

> 你的手机可能也是这样的哦

这里引用一下`@豪大大老师`这个老司机的经验：

> 国产UI就这个德性， 悄悄的改， 根本不告诉你开发者选项的入口在哪里。
>
> 有的需要连续点击基带版本， 有的需要点击内核版本， 总之， 找不到就各种点。

这里，` 小米5c` 的这个情况， 我们需要，点击**[设置]** ， 然后选择**[全部参数]** ， 连续打击5次`MIUI`版本， 就会弹出**[开发者选项]**,, 你的手机， 可以去手机官方论坛去搜索一下进入方式。

[[求助\]](http://www.miui.com/forum.php?mod=forumdisplay&fid=618&filter=typeid&typeid=4866) [MIUI9怎么找不到开发者选项了？？](http://www.miui.com/thread-9700057-1-1.html)

![Screenshot_2018-01-24-19-40-50-006_com.android.se](http://image.myfange.com/Screenshot_2018-01-24-19-40-50-006_com.android.se.png-fg)

如果成功的话， 这里会提示你， **您现在已经处于开发者模式**

下次我们进入的时候， 可以进入**[设置]**  ->  **[更多设置]** -> **[开发者选项]**

接下来， 我们需要勾选几个选项。

### 3.2 设置1 ： 勾选USB调试功能

![Screenshot_2018-01-24-19-42-49-213_com.android.se](http://image.myfange.com/Screenshot_2018-01-24-19-42-49-213_com.android.se.png-fg)

![Screenshot_2018-01-24-19-42-53-026_com.android.se](http://image.myfange.com/Screenshot_2018-01-24-19-42-53-026_com.android.se.png-fg)

点击确定即可。

### 3.3 设置2 ： 打开USB调试（安全设置）

打开这个选项之后，手机就会允许你通过USB调试修改权限或者模拟点击。

在我们这个应用中是需要用到这个权限的。

![Screenshot_2018-01-24-19-46-08-383_com.miui.secur](http://image.myfange.com/Screenshot_2018-01-24-19-46-08-383_com.miui.secur.png-fg)

### 3.4 设置3：允许添加电脑RSA的指纹

接下来， 将手机通过USB插到电脑上。 

**注意： 你手机的USB线， 确保要没有问题啊！！！，如果老断开连接的话， 就是质量有问题了。**

![adb-ubuntu.png](http://image.myfange.com/adb-ubuntu.png-fg)

如果你是第一次这么做的话， 需要你同意将电脑的RSA指纹添加到手机里。

如果你想删除这个电脑对这个手机的USB调试授权， 你可以在开发者选项里面点击**撤销USB调试授权**

如果你的手机没有出现这个对话框， 你可能需要搜索（百度/google）

```
手机型号 + 无RSA密钥指纹提示对话框
```

**贴心凡哥的温馨提示**

**提示1：你的windows里的虚拟机与windows本身， 会有两个RSA指纹，两者不同。**

PS 如果你使用的是虚拟机的话， 需要挂载这个USB设备

![virtualbox-select-android](http://image.myfange.com/virtualbox-select-android.png-fg)

勾选这个安卓设备，接下来手机出现的添加RSA指纹，才是你这个虚拟机对应的RSA指纹．**点同意**．

**提示2 : 如果你使用的是windows，请在连接手机的时候，关闭流氓手机管家**

关闭你电脑上的流氓软件， 例如**应用宝， 各种手机助手， 手机管家类似软件** ， 否则你添加USB授权的话，极其容易被捆绑安装各种软件， 千万记得。 小心。

**那么问题来了什么是RSA ？**

> RSA作为一种加密算法，最基本的作用自然是确保信息传递的安全。当被传输的信息被加密之后，即使在传输过程中被窃密，也要使窃密者几乎不可能将密文破译。
>
> 具体看知乎吧，我们先讨论重要的部分。
>
> https://zhuanlan.zhihu.com/p/25854699

## 4. ADB驱动的安装

这里呢，凡哥在这里仅提供`Ubuntu` 与`Archlinux` 的配置方法。

同学们如果用`windows` 或者`mac` ， 大家探索成功之后， 告诉我， 凡哥会完善这篇帖子。

### 4.1 在Window下的安装

> TODO 

你可以直接访问`ADB`的官网下载安装

http://adbshell.com/downloads

[How to use ADB shell commands on Windows](http://adbshell.com/commands)

### 4.2 在Ubuntu上安装ADB

在Ubuntu下安装ADB的教程呢， 凡哥主要参考下面这篇文章

[How to Install ADB & Fastboot on Ubuntu 16.04, 16.10, 14.04](https://www.linuxbabe.com/ubuntu/how-to-install-adb-fastboot-ubuntu-16-04-16-10-14-04)

需要的安装包有 `android-tools-adb ` 与 `android-tools-fastboot`

```python
sudo apt update
sudo apt install android-tools-adb android-tools-fastboot
```

如果你用的是虚拟机， 我们需要对虚拟机做一些设置。

通过usb线将电脑与手机连接在一起。 需要在虚拟机中usb设备列表中**勾选此Android 设备**。

### 4.3 在Archlinux上安装ADB

在`ArchLinux` 下安装ADB设备比较简单。 

我们输入命令

```python
sudo yaourt -S android-sdk-platform-tools 
```

当然你也可以使用`pacman` 安装。

**安装日志**

```bash
scorpion@tl ~/D/f/G/ADBDriver> sudo yaourt -S android-sdk-platform-tools 
[sudo] password for scorpion: 
resolving dependencies...
looking for conflicting packages...

Packages (1) android-sdk-platform-tools-r27.0.1-1

Total Download Size:    3.18 MiB
Total Installed Size:  16.41 MiB

:: Proceed with installation? [Y/n] Y
:: Retrieving packages...
 android-sdk-platform-tools-r27.0.1-...     3.2 MiB  8.10M/s 00:00 [####################################] 100%
(1/1) checking keys in keyring                                     [####################################] 100%
(1/1) checking package integrity                                   [####################################] 100%
(1/1) loading package files                                        [####################################] 100%
(1/1) checking for file conflicts                                  [####################################] 100%
(1/1) checking available disk space                                [####################################] 100%
:: Processing package changes...
(1/1) installing android-sdk-platform-tools                        [####################################] 100%
You need to source /etc/profile or relogin to add the Android SDK platform tools to your path.
:: Running post-transaction hooks...
(1/1) Arming ConditionNeedsUpdate...
error: missing 'marble-data' dependency for 'marble-common'
```

这里提示我们需要source一下`/etc/profile` 所以执行下面这个语句。

```bash
source /etc/profile
```

> 提示： 如果你用的是fish， 请先切换到bash，再执行这个操作。 `fish`跟`bash`的语法不兼容。
>
> 如果你不知道啥是fish， 暂时也不需要知道。跳过就好。

## 5.服务器的开启与关闭

Android手机或者模拟器是客户端， PC是服务器端（server） ， 他们之间通过TCP通信。 也就是说，我们运行ADB需要开启电脑的Server。

每次启动电脑 ， 我们必须开启`adb server` ， 这样`adb`的功能才可以被使用。

```bash
sudo adb start-server
```

关闭server

```bash
sudo adb kill-server
```

## 6. 查看ADB设备列表

### 6.1 查看ADB版本号

**查看adb有没有正确安装， 我们可以通过查看其版本号来确定。**

```bash
adb version
```

然后就会显示我的`adb` 版本信息。

```bash
scorpion@tl ~/D/fange_opencv_tutorial> adb version 
Android Debug Bridge version 1.0.39
Version 8.1.0_r7
Installed as /usr/bin/adb
```

如果你的电脑提示没有`adb` 这个指令，哎呀， 是不是忘记source了。教程上面说过的哦， 不得不再提示一遍。

> archlinux需要， ubuntu不需要

```bash
source /etc/profile
```

### 6.2 查看设备列表

查看设备列表的指令是

```bash
adb devices
```

如果你之前没有启动adb server， 运行`adb devices` 的时候， 会自动开启server， 但是会有权限问题。

还有一种可能是因为你没有允许添加**RSA指纹**。 详情见上文的 **打开手机的USB调试模式 ->  设置3：允许添加电脑RSA指纹**

```bash
scorpion@tl ~/D/fange_opencv_tutorial> adb devices
List of devices attached
a9e0d12a        no permissions; see [http://developer.android.com/tools/device.html]
```

这个时候， 你需要关闭server， 重新用管理员权限，sudo开启。

```bash
sudo adb kill-server
```

```
scorpion@tl ~/D/fange_opencv_tutorial> sudo adb start-server
* daemon not running; starting now at tcp:5037
* daemon started successfully
```

然后我们重新，执行一下

```bash
adb devices
```

设备正常

```
scorpion@tl ~/D/fange_opencv_tutorial> adb devices
List of devices attached
a9e0d12a        device

```

![ubuntu-查看android设备](http://image.myfange.com/ubuntu-查看android设备.png-fg)

## 7. ADB的shell指令

ADB的所有指令都可以在官网查询

http://adbshell.com/commands

这里， 我们因为只用到了两个指令， 截图与模拟点击， 所以就不做过多讲解。

### 7.1 获取手机截图

截图并保存在手机里，　通过usb传给电脑的三部曲．

```bash
# 截图并保存在手机的/sdcard文件夹下
adb shell screencap -p /sdcard/screen.png
# 传输图片　将图片/sdcard/screen.png传送给PC，放置在当前的路径下
adb pull /sdcard/screen.png
# 删除手机本地的临时图片
adb shell rm /sdcard/screen.png
```

你可能觉得这个过程比较繁琐。

那我们可以一部到位：

```bash
# 截图传输字节流给电脑， 保存在PC当前目录下的screenshot.png文件中
adb shell screencap -p > screenshot.png
```

`>` 箭头代表数据流向。 我在之前的linux基础课中有提到过。

![ADB手机截屏演示](http://image.myfange.com/ADB手机截屏演示V2.gif-bk)

### 7.2 手机录屏

> 这个不是必须掌握的, 只是跟截屏类似, 这里提一下

录制视频的指令

```bash
adb shell screenrecord /sdcard/jumponejump.mp4
```

录制视频, 放置在`/sdcard/jumponejump.mp4`  在终端`CTRL + C` 结束录制.

接下来我们使用pull指令, 下拉视频. 下载到我们的桌面上.

```
adb pull /sdcard/jumponejump.mp4
```

最后打开桌面上的视频 , 展示效果.

动图比较长, 请耐心看完.

![ADB手机截屏演示](http://image.myfange.com/ADB手机录屏演示V2.gif-bk)

### 7.3 模拟点击与延时抬起手指

我们需要触摸屏幕 滑动的指令

```bash
adb shell input touchscreen swipe x1 y1 x2 y2 delay_time
```

`input touchscreen` 代表我们的输入方式， 是通过模拟触屏的方法。

`swipe` 这个动作的名称叫滑动。 

那么从哪里滑动到哪里呢？

从点1`(x1, y1)` 滑动到 点2`(x2, y2)`

中间滑动事件是多少呢？ `delay_time` 毫秒

如果你不是滑动, 而是在同一个位置按压一定的时间, 你可以使 `x1 = x2` `y1 = y2`

测试这个功能呢, 你可以打开`跳一跳`游戏, 输入指令

```bash
adb shell input touchscreen swipe 400 400 400 400 1000
```

按压点(400, 400) , 延时1s.

感受一下.

## 8. CH3.1 作业

### TASK01 - 基础 - 获取一组跳一跳的截图

手机运行跳一跳程序, 玩一把, 并使用adb去获取五张运行截图.

打包在作业里.

### TASK02 - 教学回顾 - 在跳一跳游戏截图上作标记

选取任意一张运行截图, 利用highgui的鼠标事件,  先后标注棋子的脚下的中心与box的中心. 

用不同颜色标注, 并且将两个中心的坐标打印在终端.

同时打印一下图片的高度跟宽度, 从而获知自己手机的分辨率.

同时也可以通过我们之前教授的opencv几何图形绘制与文字绘制, 将坐标信息绘制在圆点周围.

![2018-01-25-20-43-13.png](http://image.myfange.com/2018-01-25-20-43-13.png-fg)

### TASK03 - 探索性作业 Python中执行命令行

刚才我们指令执行都是在`Terminal`中运行的, 那么有没有方法, 可以让我们在python中去调用命令行, 去获取到对应的数据流呢. 

例如adb获取截图, 我们是否可以通过python程序去执行? 如何做, 数据如何解析?

之前我们还讲到 adb 获取截图返回的数据类型是字节流 , 而不是字符. 

在Python中我们如何将字节流数据, 导入到`png`图片中? 

这个内容就留给大家思考, 请自行查阅相关资料.

![](http://image.myfange.com/微信公众号底部.png-bk)