# 导入opencv模块

> TODO 其实都没有告诉用户在哪里输入这个指令
> Jupyter Notebook 链接 与 演示 


python-opencv 在python中的包名称叫做 `cv2` 

```python
import cv2
```

如果你导入的时候, 系统提示你没有这个包, 啊, GG了, 你没有正确安装opencv.

有可能你装在了python2上了, 也有可能你编译源代码的时候, cmake的编译选型不对. 也有可能..... 可能的问题多了好嘛!!! 所以,跟着阿凯配环境吧, 我咋配的你就咋配的不就好了, 阿凯要让大家快速入手, 而不是纠结在用哪个操作系统, 用哪种安装方式上. 

戳下面这个链接, 走起.

[Ubuntu下利用Anaconda安装opencv](http://www.myfange.com/p/install-opencv-on-ubuntu-by-anaconda)
> TODO 更换URL

>这篇文章一来教大家如何使用anaconda 来搜索包， 添加channel , 二来也演示配置opencv开发环境的过程。 我们安装来自conda-forge , 我们选择的opencv版本是opencv=3.3.0. 另外, 当你安装完anaconda之后, 管理python包的工具就从pip转变为conda 文章写的比较仓促, 为anaconda指令讲解不是很详细, 请多包涵.

我们可以查看opencv的版本

```python
In [2]: import cv2
In [3]: cv2.__version__
Out[3]: '3.3.0'
```

> PS: 请大家注意, 这里的version两面是 **double** 两个下划线`__ `而不是单个下划线` _`

