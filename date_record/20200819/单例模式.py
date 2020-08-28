#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# @Time    : 2020/8/19 14:39
# @Author  : Ryu
# @Site    : 
# @File    : 单例模式.py
# @Software: PyCharm
# @function: 
'''
# 第一种方案
class Singleton:
    def __new__(cls, *args, **kw):
        # print(cls)
        if not hasattr(cls, '_instance'):
            cls._instance = object.__new__(cls, *args, **kw)
        return cls._instance

one = Singleton()
two = Singleton()

two.a = 3
# print(one.a)
# 3
# one和two完全相同,可以用id(), ==, is检测
# print(id(one))
# # 29097904
# print(id(two))
# # 29097904
# print(one == two)
# # True
# print(one is two)


# 第二种方案 装饰器
def Singleton(cls):
    _instance = {}
    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]
    return _singleton

@Singleton
class A(object):
    def __init__(self, x=0):
        self.x = x

a1 = A(2)
a2 = A(3)
# print(a1 is a2)
# # True
# print(a1.x)
# # 2
# print(a2.x)
# 2

# 第三种方案 metaclass
import threading

class SingletonType(type):
    _instance_lock = threading.Lock()
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            with SingletonType._instance_lock:
                if not hasattr(cls, "_instance"):
                    cls._instance = super(SingletonType,cls).__call__(*args, **kwargs)
        return cls._instance

class Foo(metaclass=SingletonType):
    def __init__(self,name):
        self.name = name


obj1 = Foo('name')
obj2 = Foo('name')
print(obj1 is obj2)
