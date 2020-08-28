#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# @Time    : 2020/8/19 15:01
# @Author  : Ryu
# @Site    : 
# @File    : test__call__.py
# @Software: PyCharm
# @function: 
'''


class Entity:
    '''调用实体来改变实体的位置。'''
    def __init__(self, size, x, y):
        self.x, self.y = x, y
        self.size = size

    def __call__(self, x, y):
        '''改变实体的位置'''
        self.x, self.y = x, y
        return 3

e = Entity(1,2,3)
e(4, 5)
print(e.x)
print(e.y)
print(e.size)