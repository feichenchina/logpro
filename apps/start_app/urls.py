#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# @Time    : 2020/8/18 15:22
# @Author  : Ryu
# @Site    : 
# @File    : urls.py
# @Software: PyCharm
# @function: 
'''
from django.conf.urls import url

from apps.start_app import views

urlpatterns = [
    url('run',views.run),
    # 单文件上传
    url('upload',views.upload),
    # 多文件上传
    url('more',views.more_upload),
    # 单文件下载
    url('download',views.download),
    url('upload_page',views.change_page),
    # 对 sql 注入进行方式验证
    url('valivate_sql',views.valivate_sql),
    #
    url('save_photo',views.save_photo),
]