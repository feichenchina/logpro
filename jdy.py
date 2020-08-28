#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# @Time    : 2020/8/24 15:49
# @Author  : Ryu
# @Site    : 
# @File    : 简道云.py
# @Software: PyCharm
# @function: 
'''
import datetime
import requests
import time
from apscheduler.schedulers.blocking import BlockingScheduler
import win32api
import win32con
import json
# dingding = 'https://oapi.dingtalk.com/robot/send?access_token=596970b8d299f68c81efd0a2193ef14ada8beb74b631c57facb8dc3c15dd16b5'
dingding = 'https://oapi.dingtalk.com/robot/send?access_token=5c9f62f242132a8ddeafe3b46c7e364f55615388a9e6cc30f5a0dcf263538a3c'
# 发送消息
def sendMessage(text, tels):
    data = {
        "msgtype": "text",
        "text": {
                "content": "发送:" + text
        },
        "at": {
            "atMobiles": tels
        }
    }
    res = requests.post(dingding, headers={'Content-Type': 'application/json; charset=utf-8'}, data=json.dumps(data))
    print(res.text)

def run(url):
    '''
    请求表单并填充信息
    :param url:
    :return: 若成功返回 True ，若失败，则返回状态码
    '''
    # 获取时间戳
    t1, stamp = get_stamp()
    date = f"孙亚楠{t1}-13782113850"

    # 公司简道云提交 headers 头信息
    headers = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
        "x-csrf-token":"Fg6MfMrz-aebbgn4KJtGg5qy6UrFdEQXgYY8",
        "cookie":"gr_user_id=106daca2-7fa9-4437-8837-eff7496c4baf; _csrf=s%3AWO9XyDY1ek6x_DXD6kTCfNjK.MlinhLf5VV56Atl%2FH8xlc82F5bLGoamXrZHMb%2B3polQ; Hm_lvt_48ee90f250328e7eaea0c743a4c3a339=1598256762; JDY_SID=s%3AvvvSnefMpr2_p8LAuEnyNlSPKgO2xGr-.IvwlSYYT%2F1Y%2FtLThfVuH%2BbGu6Tk21W3fat2PcsctegQ; fx-lang=zh_cn; help_btn_visible=true; Hm_lpvt_48ee90f250328e7eaea0c743a4c3a339=1598428840; formpass=s%3A13521252605.0h4kzr8lmtGTccysL5Bha1L%2FVQUHD8d5gH8x6Ub7AP4",
    }
    # 自己简道云的 headers 头信息
    # headers = {
    #     "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    #     "x-csrf-token": "rkKNRQsH-7d4emM3nvTaUrOoloR7pJDnHkok",
    #     "cookie": "gr_user_id=106daca2-7fa9-4437-8837-eff7496c4baf; _csrf=s%3AJQkhgrVHllT-JtsSq-kvb8jo.h9YXkqhISzi6E2RnUouHF7rM8PfFlfbVwCwjtXoUKVc; Hm_lvt_48ee90f250328e7eaea0c743a4c3a339=1596692293,1597139793,1598254939,1598255178; gr_session_id_84ec528f25e5476d=560d8d72-67a5-40b8-a9c3-87de634155f7; gr_session_id_84ec528f25e5476d_560d8d72-67a5-40b8-a9c3-87de634155f7=true; JDY_SID=s%3AOWVWWYVWcJCGdtD0gmqYm9_LOCNh2Ppi.imvSVBxCd4Qbqr3Dxhm16YKPODQPbGG9Xo7wpd8Xb28; fx-lang=zh_cn; gr_cs1_560d8d72-67a5-40b8-a9c3-87de634155f7=user_id%3A5f2b72782aa427000633378d; help_btn_visible=true; Hm_lpvt_48ee90f250328e7eaea0c743a4c3a339=1598255297; formpass=s%3A123456789.XkOpPR1lPArYsIwlElHQ5Xuip1GoSXN%2B5D%2B%2ByLgyuwI",
    # }
    #
    # # 自己简道云的传输数据
    # data = {
    #     "values":
    #         {
    #             "_widget_1596682895014":{"data":"123","visible":'true'},
    #             "_widget_1596682895091":{"data":"123","visible":'true'}
    #         },
    #     "appId":"5f2b728aaa99b00006603331",
    #     "entryId":"5f2b72907e7e62000658ab13",
    #     "hasResult": 'true',
    #     "formId":"5f2b72907e7e62000658ab13",
    #     "fx_access_token":"5f2b72907e7e62000658ab14",
    #     "fx_access_type":"form_public"
    # }

    # 公司简道云提交数据
    data = {
        "values": {"_widget_1580490412711": {"data": 13782113850, "visible": 'true'},
                    "_widget_1579966423757": {"data": "孙亚楠", "visible": 'true'},
                    "_widget_1580359990010": {"data": "信息中心＆数字工程公司", "visible": 'true'},
                    "_widget_1580582698023": {"data": "郑州分公司", "visible": 'true'},
                    "_widget_1580359990429": {"data": "信息中心＆数字工程公司", "visible": 'false'},
                    "_widget_1576481068260": {"data": stamp, "visible": 'true'},
                    "_widget_1580382189120": {"data": "手动选择", "visible": 'true'},
                    "_widget_1580382189009": {"data": {"province": "河南省", "city": "郑州市", "district": "金水区"},
                                              "visible": 'true'},
                    "_widget_1579927440924": {"data": "正常", "visible": 'true'},
                    "_widget_1583415667636": {"data": "正常", "visible": 'true'},
                    "_widget_1581177603935": {"data": "否", "visible": 'true'},
                    "_widget_1580300861144": {"data": "已返程", "visible": 'true'},
                    "_widget_1580309817154": {"data": "否", "visible": 'true'},
                    "_widget_1581177601824": {"data": "否", "visible": 'true'},
                    "_widget_1586575736268": {"data": "否", "visible": 'true'},
                    "_widget_1579966423907": {"data": date, "visible": 'true'},
},
         "appId": "5dcbc0346b20480006548037",
         "entryId": "5e316fae5309b8000683567c",
         "formId": "5e316fae5309b8000683567c",
         "hasResult": 'true',
         "fx_access_token": "5e316fae5309b8000683567d",
         "fx_access_type": "form_public"
    }
    res = requests.post(url,json = data,headers = headers)
    print(res.status_code)
    print(res.content.decode('utf-8'))
    if int(res.status_code) == 200:
        return 200
    else:
        return res.content.decode('utf-8')

def job():
    '''
    在此写入任务，方便下面定时调用
    :return: 无返回，只是将填报信息弹窗提醒
    '''
    # 自己的简道云地址
    # url = "https://s4y1h74pzh.jiandaoyun.com/_/data/create"

    # 公司的简道云地址
    url = "https://to3bh0ij7c.jiandaoyun.com/_/data/create"
    res = run(url)

    # print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    # print(res)
    # 弹框提醒是否填写成功
    tels = ['13782113850']
    if res == 200:
        sendMessage('每日填报已成功填写', tels)
        # win32api.MessageBox(0, "已成功填写", "每日填报", win32con.MB_OK)
    else:
        sendMessage(f'每日填报填写出现异常情况，请处理\n{res}', tels)
        # win32api.MessageBox(0, f"填写失败\n{res}", "每日填报", win32con.MB_OK)


# def setText(aString):
#     """设置剪贴板文本"""
#     w.OpenClipboard()
#     w.EmptyClipboard()
#     w.SetClipboardData(win32con.CF_UNICODETEXT, aString)
#     w.CloseClipboard()
#
# def send_qq(to_who, msg):
#     """发送qq消息
#     to_who：qq消息接收人
#     msg：需要发送的消息
#     """
#     # 将消息写到剪贴板
#     setText(msg)
#     # 获取qq窗口句柄
#     qq = win32gui.FindWindow(None, to_who)
#     # 投递剪贴板消息到QQ窗体
#     win32gui.SendMessage(qq, 258, 22, 2080193)
#     win32gui.SendMessage(qq, 770, 0, 0)
#     # 模拟按下回车键
#     win32gui.SendMessage(qq, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
#     win32gui.SendMessage(qq, win32con.WM_KEYUP, win32con.VK_RETURN, 0)

def get_stamp():
    # 获取当前时间
    t = datetime.datetime.now()

    # 获取当前日期
    t1 = t.strftime('%Y%m%d')
    # 转为秒级时间戳
    start_time = time.mktime(time.strptime(t1, '%Y%m%d'))
    # 转换Wie毫秒级时间戳
    stamp = str(start_time * 1000).split(".")[0]
    print(t1)
    print(stamp)
    return t1,stamp


if __name__ == '__main__':
    # job()
    # BlockingScheduler：在进程中运行单个任务，调度器是唯一运行的东西
    scheduler = BlockingScheduler()

    # 采用阻塞的方式
    # 采用date的方式，在特定时间只执行一次
    # 采用 interval 的方式，每过 1 分钟执行一次
    # weeks：周。整形。
    # days：一个月中的第几天。整形。
    # hours：小时。整形。
    # minutes：分钟。整形。
    # seconds：秒。整形。
    # start_date：间隔触发的起始时间。
    # end_date：间隔触发的结束时间。
    # jitter：触发的时间误差。
    scheduler.add_job(job, 'interval', seconds=10)

    # 每天 16:46 分执行一次
    # scheduler.add_job(job, 'cron', day_of_week='0-6', hour=14, minute=00)
    # myjob = schedule.every(2).seconds
    # myjob.job_func = job
    # schedule.jobs.append(job)
    # result = myjob.run()
    # print(result)
    # 开启定时任务
    scheduler.start()

