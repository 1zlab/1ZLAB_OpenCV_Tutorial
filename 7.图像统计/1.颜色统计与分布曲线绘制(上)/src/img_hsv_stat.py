# -*- coding: utf-8 -*- 

'''
绘制彩图在HSV颜色空间下的统计直方图
'''

from matplotlib import pyplot as plt
import numpy as np
import cv2
import sys

# 读入图片
img_path = sys.argv[1]
img = cv2.imread(img_path)
# img = cv2.imread('little_chess.png')
if img is None:
    print("图片读入失败, 请检查图片路径及文件名")
    exit()


# 将图片转换为HSV格式
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# 创建画布
fig, ax = plt.subplots()
# Matplotlib预设的颜色字符
hsvColor = ('y', 'g', 'k')
# 统计窗口间隔 , 设置小了锯齿状较为明显 最小为1 最好可以被256整除
bin_win  = 3
# 设定统计窗口bins的总数
bin_num = int(256/bin_win)
# 控制画布的窗口x坐标的稀疏程度. 最密集就设定xticks_win=1
xticks_win = 2
# 设置标题
ax.set_title('HSV Color Space')
lines = []
for cidx, color in enumerate(hsvColor):
    # cidx channel 序号
    # color r / g / b
    cHist = cv2.calcHist([img], [cidx], None, [bin_num], [0, 256])
    # 绘制折线图
    line, = ax.plot(cHist, color=color,linewidth=8)
    lines.append(line)  

# 标签
labels = [cname +' Channel' for cname in 'HSV']
# 添加channel 
plt.legend(lines,labels, loc='upper right')
# 设定画布的范围
ax.set_xlim([0, bin_num])
# 设定x轴方向标注的位置
ax.set_xticks(np.arange(0, bin_num, xticks_win))
# 设定x轴方向标注的内容
ax.set_xticklabels(list(range(0, 256, bin_win*xticks_win)),rotation=45)

# 显示画面
plt.show()
