# 读入图片(imread)

实际上`imread` 也属于`HighGUI`的部分。

在`CH1.2` 中凡哥讲解了`imread`函数， 这里就不赘述。 

还是读入那张猫的图片。

```python
# 导入一张图像 模式为彩色图片
img = cv2.imread('cat.jpg', cv2.IMREAD_COLOR)
```