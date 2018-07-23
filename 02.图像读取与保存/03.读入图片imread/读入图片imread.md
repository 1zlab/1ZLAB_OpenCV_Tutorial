# 读入图片imread

我们读入一张图片的时候, 使用的是`cv2.imread` 函数, 传入的第一个参数是图片的路径. 

我在代码的同级目录下放置了一个`cat.jpg` 小猫的照片.

![0119_cat.jpg](./image/0119_cat.jpg)

**注意，这里容易出错，Linux与Windows的路径格式不同，同时也需要注意相对路径与绝对路径。**

```python
# 导入一张图像 模式为彩色图片
img = cv2.imread('cat.jpg')
```

这样你就读入了这张小猫的图片.

**那opencv都支持导入哪些格式的图片呢?**

具体我们可以通过查阅文档 , 在python终端中输入: 

```python
help(cv2.imread)
```

> PS: 前提你得导入cv2 模块.


**导入RBG彩图 还是是 灰度图?**

第二个参数是图像颜色空间, 默认就是BGR彩图`cv2.IMREAD_COLOR`

上面这个语句跟下面作用是一样的.

```python
# 导入一张图像 模式为彩色图片
img = cv2.imread('cat.jpg', cv2.IMREAD_COLOR)
```

如果你想导入灰度图, 就需要传入 `cv2.IMREAD_GRAYSCALE `

```
img = cv2.imread('cat.jpg', cv2.IMREAD_GRAYSCALE)
```






