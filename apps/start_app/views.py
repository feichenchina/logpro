import logging
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from Common.sql_info import getCursorConn, closeCurseConn

default_database = settings.DATABASES["default"]
# print(default_database)
# c = connections[default_database['NAME']]

logger = logging.getLogger("mdjango")
# Create your views here.
ipset = []

def run(request):
    temp = request.GET['temp']
    if int(temp) == 1:
        logger.info('成功请求接口')
        pass
    else:
        logger.error('错误请求接口')
        pass
    return HttpResponse(temp)

def upload(request):
    '''
    function: 对单个文件进行上传
    :param request:
    :return:
    '''
    # 返回的数据
    data = {'code':0,'msg':'','data':{}}
    print('进入upload')
    filename = request.FILES["file"].name
    try:
        path = f'upload/{filename}'
        with open(path,'wb') as f:
            for i in request.FILES["file"].chunks():
                f.write(i)
        data['code'] = 1
        data['msg'] = 'success'
    except Exception as e:
        print(e)
        if os.path.exists(path):  # 如果文件存在
            # 删除文件，可使用以下两种方法。
            os.remove(path)
        data['code'] = 0
        data['msg'] = 'error'
    return JsonResponse(data)


def more_upload(request):
    '''
    function: 对多个文件进行上传
    :param request:
    :return:
    '''
    # 返回的数据
    data = {'code':0,'msg':'','data':{}}
    try:
        # 获取前端传过来的文件流列表
        files = request.FILES.getlist('file')
    except Exception as e:
        print(e)
        data['code'] = 0
        data['msg'] = '读取文件列表发生异常'
        return JsonResponse(data)

    # 判断前端是否传入文件列表
    if not len(files):
        data['code'] = 0
        data['msg'] = '请确认文件是否选取'
        return JsonResponse(data)

    # 标记一下传输过来的文件列表写入时是否发生异常，若发生异常，需要将此次上传文件删除
    temp = True
    # 对文件列表进行分批写入
    for file in files:
        # 获取每个文件的名称
        filename = file.name
        try:
            # 文件保存路径
            path = f'upload/{filename}'
            # 以二进制方式写入
            with open(path,'wb') as f:
                # 对文件分批写入
                for i in file.chunks():
                    f.write(i)
            data['code'] = 1
            data['msg'] = 'success'
        except Exception as e:
            temp = False
            break

    # 判断文件写入是否有异常,发生异常删除已上传文件
    if not temp:
        for file in files:
            filename = file.name
            path = f'upload/{filename}'
            if os.path.exists(path):  # 如果文件存在
                # 删除文件，可使用以下两种方法。
                os.remove(path)
            else:
                continue

        data['code'] = 0
        data['msg'] = 'error'
    return JsonResponse(data)

from django.http import StreamingHttpResponse


def download(request):
    '''
    function：下载文件
    :param request:
    :return:
    '''
    # do something...
    global ipset
    filename = request.GET['filename']

    if 'HTTP_X_FORWARDED_FOR' in request.META.keys():
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']

    if '-'.join([ip,filename]) not in ipset:
        ipset.append(ip)
    else:
        data = {'code':1,'msg':'你已经在下载该资源了，是否要重复下载','data':{}}
        return JsonResponse(data)

    def file_iterator(file_name, chunk_size=1024):
        with open(file_name,'rb') as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    the_file_name = filename
    path = f'upload/{filename}'
    response = StreamingHttpResponse(file_iterator(path))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)
    if '-'.join([ip,filename]) in ipset:
        ipset.remove('-'.join([ip,filename]))

    return response

def change_page(request):
    '''
    转发到上传页面
    :param request:
    :return:
    '''
    return render(request,'upload.html')

def valivate_sql(request):
    username = request.GET['username']
    sql = 'select * from auth_user where username = %s'
    cursor,conn = getCursorConn()
    cursor.execute(sql,username)
    result = cursor.fetchone()
    # print("执行的sql语句：",connections.queries)
    closeCurseConn(cursor, conn)
    print("结果：",result)
    return HttpResponse('OK')



# 抓取天天基金自己关注的基金详情
import datetime
import xml
import requests
from requests.exceptions import RequestException
from pyquery import PyQuery as pq
import os
import time

def judgment_catalog(catalog_path):
    '''
    判断目录是否存在，若不存在则创建
    :return:
    '''
    if not os.path.exists(catalog_path):
        os.makedirs(catalog_path)

def judgment_file(file_path):
    '''
    判断文件是否存在，若不存在则创建
    :return:
    '''
    if not os.path.exists(file_path):
        os.system("touch {}".format(file_path))  #调用系统命令行来创建文件

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

def get_str_time_now():
    '''
    获取当前时间的字符串格式
    :return: 当前时间的字符串格式数据
    '''
    # 获取当前时间
    t = datetime.datetime.now()
    # 获取当前日期的字符串格式
    t1 = t.strftime('%Y%m%d')
    return t1


def get_ten_stamp():
    '''
    获得当前时间的十位时间戳
    :return: 当前时间的十位时间戳
    '''
    t = datetime.datetime.now()
    # 获取当前日期
    t1 = t.strftime('%Y%m%d %H%M%S')
    # 转为秒级时间戳
    start_time = time.mktime(time.strptime(t1, '%Y%m%d %H%M%S'))
    return start_time

def get_img(img_url):
    '''
    得到图片
    :param img_url:
    :return: 图片的二进制文件
    '''
    try:
        response = requests.get(img_url)
        content = response.content
    except Exception as e:
        content = ''
    return content

def save_img(img_respose='',filename='syn'):
    '''
    将图片二进制文件保存到本地
    :param img_respose:
    :return:
    '''
    if img_respose == '':
        # 未获取到图片的二进制文件
        return 201
    # 将他拷贝到本地文件 w 写  b 二进制  wb代表写入二进制文本
    #  获取当前时间的字符串格式数据
    now_date = get_str_time_now()
    # now_ten_time = str(get_ten_stamp()).split('.')[0]
    filename = '_'.join([filename,now_date])
    # 保存路径
    catalog_path = r'G:\code\python\logpro\img\%s' %now_date
    # 判断目录是否存在，若不存在则创建
    judgment_catalog(catalog_path)
    file_path = r'G:\code\python\logpro\img\%s\%s.png' %(now_date,filename)
    # 判断文件是否存在，若不存在则创建
    judgment_file(file_path)
    try:
        # 写入文件
        with open(file_path, 'wb') as f:
            f.write(img_respose)
        return 0
    except Exception as e:
        # 文件写入出现问题
        return 202


def spider(fund_id):
    url = 'http://fund.eastmoney.com/%s.html' % fund_id
    html = get_one_page(url)
    Html = requests.get(url)
    Html.encoding = 'utf-8'
    HTML = etree.HTML(Html.text)
    # print(Html.text)
    # print(html)
    results = HTML.xpath('//*[@id="gz_gszzl"]/text()')
    # print(results)
    if html != None:
        doc = pq(html)
        # estimatedchart
        # hasLoading
        name = doc('#body > div:nth-child(12) > div > div > div.fundDetail-header > div.fundDetail-tit > div').text()
        value = doc('#gz_gszzl').text()
        # print('查询出来的 value 值:',value)
        return name, value

def start_spider():
    result = {}
    # 关注的基金 id
    fund_id = {'001766', '004075', '050023', '004851', '009777', '690007', '001410', '161725'}
    # fund_id = {'004348', '005911'}  ###这边改为你的基金代码
    for id in fund_id:
        name, value = spider(id)
        # print(name)
        result[name] = value
        img_url = ''.join(['http://j4.dfcfw.com/charts/pic6/',id,'.png'])
        content = get_img(img_url)
        save_result = save_img(content,name.split('(')[0])
        if save_result != 0:
            print('保存文件错误')

    now = datetime.datetime.now()
    # print(now)
    result1 = sorted(result.items(), key=lambda x: x[1])
    for fund in result1:
        # print(fund)
        # print(fund[1] + '\t' + fund[0])
        pass

def save_photo(request):
    start_spider()
    return HttpResponse('OK')
