
# 窗口展示(imshow)

在HighGUI展示图像， 需要使用到 `imshow` 函数， 第一个参数， 我们传入窗口的名称，第二个参数就是 `Image` 对象。

```python
# 展示图像
cv2.imshow('image',img)
```



如果`image`这个窗口之前并没有被声明， 那么同时会先创建一个名字叫做`image`的窗口.
