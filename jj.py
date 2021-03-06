#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# @Time    : 2020/8/27 14:32
# @Author  : Ryu
# @Site    : 
# @File    : jj.py
# @Software: PyCharm
# @function: 
'''

import datetime
import xml

import requests
from requests.exceptions import RequestException
from pyquery import PyQuery as pq


def get_one_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            response.encoding = 'utf-8'
            return response.text
        return None
    except RequestException:
        return None
from lxml import etree

def spider(fund_id):
    url = 'http://fund.eastmoney.com/%s.html' % fund_id
    html = get_one_page(url)
    Html = requests.get(url)
    Html.encoding = 'utf-8'
    HTML = etree.HTML(Html.text)

    results = HTML.xpath('//*[@class="estimatedchart hasLoading"]/img/@src')
    print(results)
    if html != None:
        doc = pq(html)
        # estimatedchart
        # hasLoading
        name = doc('#body > div:nth-child(12) > div > div > div.fundDetail-header > div.fundDetail-tit > div').text()
        value = doc('#gz_gszzl').text()
        return name, value


def send_wx():
    import itchat

    itchat.login()

    itchat.send(u'你好，文件传输助手', 'filehelper')

from qqbot import _bot as bot

# class SendQq:




# 自定义函数，用来进一步封装qqbot接口
# 获取所有好友列表
def getBuddyByName(nickname):
    return bot.List('buddy', nickname)

# 获取所有群列表
def getGroupByName(groupname):
    return bot.List('group', groupname)

# 给备注（没用备注就是昵称）为nickname的好友发送content消息
def sendToNickname(nickname, content):
    user = getBuddyByName(nickname)
    if user:
        bot.SendTo(user[0], content)
    else:
        print("未找到联系人：" + nickname)

if __name__ == '__main__':

    # result = {}
    # fund_id = {'001766','004075','050023','004851','009777','690007','001410','161725'}
    # # fund_id = {'004348', '005911'}  ###这边改为你的基金代码
    # for id in fund_id:
    #     name, value = spider(id)
    #     result[name] = value
    # now = datetime.datetime.now()
    # print(now)
    # result1 = sorted(result.items(), key=lambda x: x[1])
    # for fund in result1:
    #     print(fund)
    #     print(fund[1] + '\t' + fund[0])

    # 登陆qq，使用配置文件为fantasy
    bot.Login()
    sendToNickname('幕熙','test')
    pass
