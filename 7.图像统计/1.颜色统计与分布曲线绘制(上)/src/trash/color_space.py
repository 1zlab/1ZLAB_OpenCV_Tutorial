# -*- coding: utf-8 -*- 
'''
颜色空间与颜色标识

[Done] 修改LAB与YUV的配色

'''

COLOR_SPACE_DICT = {
    'RGB': {
        'channels': ('R', 'G', 'B'),
        'line_color': ('r', 'g', 'b'),
    },
    'BGR': {
        'channels': ('B', 'G', 'R'),
        'line_color': ('b', 'g', 'r'),
    },
    'GRAYSCALE': {
        'channels': ('GRAYSCALE'),
        'line_color': ('k'),
    },
    'LAB': {
        'channels': ('L', 'A', 'B'),
        'line_color': ('k', 'y', 'g'),
    },
    'YUV': {
        'channels': ('Y', 'U', 'V'),
        'line_color': ('k', 'y', 'pink'),
    }
}
