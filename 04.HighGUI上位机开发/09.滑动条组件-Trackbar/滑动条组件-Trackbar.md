

# 滑动条组件Trackbar



## 创建滑动条

首先我们需要创建一个Trackbar , 调用createTrackbar 这个函数

    cv2.createTrackbar(trackbar_name,window_name,min_value,max_value,callback_func)

 依次传入的函数

- trackbar_name 滑条的名称，获取这个滑条的数值也是通过名称
- window_name 滑条所在窗口 (window) 的名称
- min_value 滑条最小值
- max_value 滑条最大值
- callback_func 回调函数，这个参数其实类似C语言中的函数指针，我传入的是函数名称，每次滑条被拖动的时候，都会执行这个函数．　

例如：　

```python
# 这个nothing的意思就是啥也不做。
def nothing(x):
    pass
cv2.createTrackbar('gray_value','image',0,255,nothing)
```



这里的nothing(x) ,  被传入的x 实际上是滑条的当前取值。

你也可以改成这样， 看一下x 的值。

```python
# 这个nothing的意思就是啥也不做。
def nothing(x):
    print(x)
cv2.createTrackbar('gray_value','image',0,255,nothing)
```

x 是我命名的值， 你可以命名为任意名称。



**Trackbar的使用实例可以见通过HighGUI的Trackbar制作可变色背景**

![灰度调色盘滑条(完整版)](./image/灰度调色盘滑条(完整版).gif)





## 设置滑动条的位置

初始化滑动条的位置需要用到`setTrackbarPos`这个函数。



```python
cv2.setTrackbarPos('trackbar_name','window_name', value)
```

依次传入`Trackbar`的名字，`Trackbar`所在的窗口的名字， 还有`Trackbar`的初始值。

*使用样例*

```python
cv2.setTrackbarPos('gray_value','image'， 10)
```





## 获取滑动条的位置



除了在回调函数中获取Trackbar的取值， 还可以通过`getTrackbarPos` 函数获取`Trackbar`的取值。

依次传入`Trackbar`的名字，`Trackbar`所在的窗口的名字, 返回当前Trackbar的取值。

```python
value = cv2.getTrackbarPos('trackbar_name','window_name')
```



*使用样例*

```python
gvalue = cv2.getTrackbarPos('gray_value','image')
```



