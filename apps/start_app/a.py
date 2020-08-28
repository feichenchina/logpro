#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# @Time    : 2020/8/18 15:18
# @Author  : Ryu
# @Site    : 
# @File    : a.py
# @Software: PyCharm
# @function: 
'''
# import sys
from typing import overload
# from overloader import overload
# print('这是apps下的a')
# print(sys.modules,sep=',',file=sys.stdout)

# msg = ("the 'package' argument is required to perform a relative "
#                    "import for {!r}")
# raise TypeError(msg.format('name'))

class A:

    def __init__(self,name,age):
        self.name = name
        self.age = age
        print('进入__init__方法')
        print(">>>>>>>>>>>>>>>")

    def __new__(cls, *args, **kwargs):
        print(cls)
        print(args)
        args = list(args)
        # print(**kwargs)
        print('进入__new__方法')
        print(">>>>>>>>>>>>>>>")
        if args[1] <= 25:
            args[1] = 30
        name = args[0] if len(args) >= 1 else 'syn'
        age = args[1] if len(args) == 2 else 0
        if age  >= 25:
            return cls.__init__(cls,name,age)
        else:
            return object.__new__(cls)

    @classmethod
    def class_method(cls,name,year):
        print(cls)
        print('进入classmethod方法')
        print(">>>>>>>>>>>>>>>")
        return cls(name,year)

    @staticmethod
    def static_method(name,year):
        print('进入静态方法')
        print(">>>>>>>>>>>>>>>")
        return A(name,year)

    def run(self):
        print(self)
        print('进入实例方法')
        print(">>>>>>>>>>>>>>>")


# 测试重载
# @overload
@overload
def utf8(value: None) -> None:
    return
@overload
def utf8(value: str) -> str:
    return '123'
# @overload
def utf8(value: int) -> bytes:
    print(type(value))
    if not (isinstance(value,int)):
        raise TypeError('value 参数必须为int类型')
    return bytes(123)


def test_overload_main():
    res = utf8('123')
    print(res)
    pass

# 对方法里面的类进行测试
def test_inner_class(temp):
    if temp == 'sun':
        class Foo:
            pass
        return Foo
    else:
        class Voo:
            pass
        return Voo

class Foo:
    # print('进入外部的Foo类')
    def __init__(self,name,year):
        self.name = name
        self.year = year

    def __new__(cls, *args, **kwargs):
        return Foo.__init__(cls,1,2)

def test_inner_class_main():
   a = test_inner_class('sun')
   print(a)
   print(a.__name__)
   # print(a.getattr)
   print(int(123).bit_length())
   a = int('11', base=10)
   print(a)
   print(a.__sizeof__())
   print(a.__truediv__(3))
   print(a/3)
   print(a//3)
   print(a)
   print(a.__rfloordiv__(33))


if __name__ == '__main__':
    # a = A('sun',26)
    # print(A.age)
    # 对方法内部类进行测试
    # test_inner_class_main()

#     对重载进行测试
    test_overload_main()

