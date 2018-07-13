# 创建一个窗口 -namedWindow



我们刚刚创建了一个窗口， 名字叫做`image_win` 

```python
# 创建一个名字叫做 image_win的窗口
cv2.namedWindow('image_win')
```



我们也可以传入一些参数（`flags`） 来实现窗口的一些设定。

flags其实是一个整数， 用这个二进制的特定的`位`， 来表示某个选项是A选项（二进制 0）还是B选项（二进制1）。 



**设置选项1： 窗口大小**

`WINDOW_NORMAL` **1** 代表允许拖动窗口变换窗口大小。

`WINDOW_AUTOSIZE`  **0 默认** 根据屏幕跟图片的大小， 自动缩放。 不允许手动变化窗口大小。



**设置选项2： 设置宽高比**

`WINDOW_FREERATIO`  **256** 不固定宽高比。

`WINDOW_KEEPRATIO`  **0  默认**固定宽高比， 也就是窗口拖拽缩放， 必须保持原来的宽高比。 



**设置选项3 : 窗口GUI版本**

`WINDOW_GUI_NORMAL` **16** 旧版窗口组件。 不支持statusbar跟toolbar。 就是窗口上方的状态栏，工具栏。

`WINDOW_GUI_EXPANDED`  **0 默认** 新版本功能增强的GUI窗口。





我们可以通过按位或的方式，通过一个参数， 同时传入多个选项的值。 

`flags`的值默认为0 ， 也就相当于`WINDOW_AUTOSIZE | WINDOW_KEEPRATIO | WINDOW_GUI_EXPANDED`



所以上面的语句等同于: 

```python
# 创建一个名字叫做 image_win的窗口
cv2.namedWindow('image_win'， flags=cv2.WINDOW_AUTOSIZE | cv2.WINDOW_KEEPRATIO | cv2.WINDOW_GUI_EXPANDED)
```



如果我想设定，窗口可以自由拖动， 那么我就需要这么写

```python
# 创建一个名字叫做 image_win的窗口
cv2.namedWindow('image_win'， flags=cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO | cv2.WINDOW_GUI_EXPANDED)
```

又因为另外两个选项均为默认选项， 值为0, 所以写法等同于

```python
# 创建一个名字叫做 image_win的窗口
cv2.namedWindow('image_win'， flags=cv2.WINDOW_NORMA)
```



如果我想让这个窗口，即可以拖放又可以不固定宽高比（ratio）， 那我其实应该这样写。

```python
# 创建一个名字叫做 image_win的窗口
cv2.namedWindow('image_win'， flags=cv2.WINDOW_NORMA | cv2.WINDOW_FREERATIO)
```





如果窗口什么也不显示, 窗口其实是一个占位符(Placeholder)的作用. 

`CH1.3_Blank_Window.py`

```python
import numpy as np
import cv2

# 创建一个名字叫做 image_win的窗口
cv2.namedWindow('image_win', cv2.WINDOW_NORMAL)

# windows下啥也不放置

# 检测按下的按钮
print("请按任意键关闭窗口")

# 如果没有下面的waitKey, 窗口会一闪而过, 后面会讲解
key_pressed = cv2.waitKey(0)

# cv2.destroyAllWindows()
cv2.destroyWindow('image_win')
```





![0120_blank_windows.png](http://image.myfange.com/0120_blank_windows.png-fg)