#轮廓点集的绘制(drawContours)

```python
# 绘制轮廓
cv2.drawContours(image=canvas, contours=contours, contourIdx=-1, color=(0,255,0), thickness=3)
```

**参数解析**

* `image` :画布
* `contours` 轮廓数组
* `contourIdx` : 要绘制的轮廓序号　-1代表所有
* `color` 颜色
* `thickness` 线条宽度


**学习编程, 最重要的是阅读源代码, 并且修改参数, 并实验. 输入(Input)决定输出(Output), 所以同学们, 接下来的三个程序, 好好阅读源码**



## `draw_contours_v0.py`

```python
import numpy as np
import cv2

gray = cv2.imread('cute_princess.png', cv2.IMREAD_GRAYSCALE)

# 设定模式
mode = cv2.RETR_TREE
# 获取边缘信息
image, contours, hierarchy = cv2.findContours(image=gray,mode=mode, method=cv2.CHAIN_APPROX_SIMPLE)

# 创建画布
canvas = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
# 绘制轮廓
cv2.drawContours(image=canvas, contours=contours, contourIdx=-1, color=(0,255,0), thickness=3)

# 保存画布
cv2.imwrite('countours_part_all_mode_%d.png'%(mode), canvas)
# 打印继承矩阵
print(hierarchy)
```



## `draw_contours_v1.py`

**注意：drawContours函数会直接在传入的画布上绘制, 返回的也是这个画布.**

如果你不想影响原来的图片,可以传入一个图片的拷贝 `np.copy(img)`

```python
all_cnt_img = cv2.drawContours(np.copy(img), contours, -1, (0,255,0), 3)
```



```python
import numpy as np
import cv2

img = cv2.imread('cute_princess.png')
# 读入灰度图
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# 转化为二值化图
ret,thresh = cv2.threshold(gray,127,255,0)
# 获取边缘信息
image, contours, hierarchy = cv2.findContours(image=thresh,mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)


all_cnt_img = cv2.drawContours(np.copy(img), contours, -1, (0,255,0), 3)

cv2.imwrite('countours_part_all.png', all_cnt_img)
```



## `draw_contours_v2.py`

接下来的这个代码, 分别绘制每个轮廓并保存在不同的图片中. 教程里上部分的图片就是由这个程序生成的.

```python
import numpy as np
import cv2

img = cv2.imread('cute_princess.png')
# 读入灰度图
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# 转化为二值化图
ret,thresh = cv2.threshold(gray,127,255,0)
# 获取边缘信息
image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for idx,cnt in enumerate(contours):
    tmp = cv2.drawContours(np.copy(img), [cnt], 0, (0,255,0), 3)
    print("Contour No.%d"%(idx))
    print(cnt)
    cv2.imwrite('contours_part_%d.png'%(idx), tmp)
```

