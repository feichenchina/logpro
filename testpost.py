#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# @Time    : 2020/8/24 9:50
# @Author  : Ryu
# @Site    : 
# @File    : testpost.py
# @Software: PyCharm
# @function: 
'''
import socket
import time

def runtastic_heart_rate_pro(func):

    def inner(ip,port):
        # 此时的参数 IP ，port 均为 port_opend 方法的参数
        res = False
        temp = func(ip,port)
        if temp:
            return True
        else:
            for i in range(3):
                time.sleep(3)
                print('第%s次进入循环发送'%i)
                time.sleep(3)
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    print('进入1正常环境')
                    s.connect_ex((ip, port))
                    s.shutdown(2)
                    res = True
                    break
                except:
                    print('进入1异常环境')
                    continue
            return res
    return inner



@runtastic_heart_rate_pro
def port_opend(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect_ex((ip, port))
        s.shutdown(2)
        return True
    except:
        return False


if __name__ == '__main__':
    res = port_opend(1,2)
    print(res)