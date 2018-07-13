# -*- coding: utf-8 -*- 
'''
颜色统计工具包

TODO 在颜色统计条中绘制颜色渐变条
TODO 提供最大值 最小值 均值 众数 的参考值
TODO 添加中文说明（Matplotlib需要配置）
TODO 图像在YUV空间内的投影 3D 跟 2D（U跟V）
TODO 2D图像分布 在两个坐标系位置再添加两个统计图（像素百分比） 还有渐变色图注
'''

from color_space import COLOR_SPACE_DICT
from matplotlib import pyplot as plt
import numpy as np
import cv2
class ImageColorStat:
    
    def __init__(self, image, color_space, roi=None, win_size=3):
        '''
        @image: image为对应色彩空间(color_space)的图片
        @color_space: 色彩空间(字符串)
            支持颜色空间列表
            * RGB
            * BGR
            * GRAYSCALE
            * LAB
            * YUV
        @roi: 感兴趣空间，格式为(x, y, w, h)
        @win_size: 颜色统计窗口间隔 , 设置小了锯齿状较为明显 最小为1 最好可以被256整除

        '''
        
        if color_space not in COLOR_SPACE_DICT.keys():
            print('ERROR: 非法的颜色空间(color_space)取值{}'.format(color_space))
            print('有效的颜色空间取值： {}'.format(list(COLOR_SPACE_DICT.keys())))
            exit(1)

        # 判断colorspace是否合法
        if len(image.shape) == 2 and color_space != 'GRAYSCALE':
            # 图片为灰度图 查看与color_space是否匹配
            print('ERROR: 图片格式与颜色空间标示不匹配\n')
            exit(1)
        
        if roi is None:
            # 赋值原图
            self.image = image
        else:
            x,y,w,h = roi # 提取出ROI的元素
            # 判断ROI是否合法
            if not(x >= 0 and w >0 and x + w < image.shape[1]) or \
                not(y >=0 and h >0 and y + h < image.shape[0]):
                print('ERROR: 非法ROI{}'.format(roi))
                exit(1)
            # 赋值roi图像
            self.image = image[y : y+h, x : x + w]
        
        self.color_space = color_space
        self.win_size = win_size # 统计窗口间隔(尺寸)
        self.win_num = int(256/win_size) # 设定统计窗口bins的总数
        self.xticks_win = 2*win_size # 控制画布的窗口x坐标的稀疏程度. 最密集就设定xticks_win=1

    def draw_image_stat_result(self):
        '''
        在图像中统计对应颜色空间下的颜色分布
        ------
        [Done] 纵向布局，第一个图显示的是image ROI图像
            剩下的为各个通道的统计图
        [Done] 纵向的取值修改为 百分比 /像素总个数， 取值范围为 0-100%
        [Done] 添加Title统计图
        [Done] 线实心填充
        [PASS] 添加中文标题支持
        [Done] 隐藏图片的坐标系
        [PASS] 添加子图之间的pending
        '''
        # plt.subplot(1,1,1)
        # plt.imshow(self.image[:,:,::-1])
        # plt.title('ROI')
        # plt.axis('off')
        
        plt.suptitle('{} Color Space Hist'.format(self.color_space), fontsize=16)
        # 获取通道与颜色的映射
        line_color = COLOR_SPACE_DICT[self.color_space]['line_color']
        # 通道名称
        channels = COLOR_SPACE_DICT[self.color_space]['channels']
        # pixel像素点总的个数
        pixel_num = self.image.size 
        for cidx, color in enumerate(line_color):
            
            axes = plt.subplot(3,1,cidx+1)
            # 设定标题
            axes.set_title(channels[cidx])
            cHist = cv2.calcHist([self.image], [cidx], None, [self.win_num], [0, 256])
            cHist.resize((len(cHist))) # 变换为一维numpy数组
            cHist = cHist / pixel_num # 计算获得百分比 数值归一化0-1
            # 绘制折线图
            axes.plot(cHist, color=color)
            
            x = np.arange(len(cHist))
            # 颜色填充
            axes.fill_between(x, 0, cHist, where=(x>=0), facecolor=color, interpolate=True )
            # 设定画布的范围
            axes.set_xlim([0, self.win_num])
            axes.get_yaxis().set_visible(False) # 隐藏y坐标的表示
            # 设定x轴方向标注的位置
            axes.set_xticks(np.arange(0, self.win_num, self.xticks_win))
            # 设定x轴方向标注的内容
            axes.set_xticklabels(list(range(0, 256, self.win_size*self.xticks_win)),rotation=0)

        # 显示画面
        plt.show()