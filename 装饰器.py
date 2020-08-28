#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# @Time    : 2020/8/24 10:32
# @Author  : Ryu
# @Site    : 
# @File    : 装饰器.py
# @Software: PyCharm
# @function: 
'''


def deco(func):
    print(1, func)
    def inner(a,b):
        print(2, a,b)
        print('inner')
        return func(a,b)

    return inner


def test(fun):
    print('test:', fun)
    return 1,2


@deco
def main(a,b):
    return a+b
if __name__ == '__main__':
    res = main(1,2)
    print(res)