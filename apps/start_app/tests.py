# from django.test import TestCase

# Create your tests here.
import requests


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

result = get_img('http://j4.dfcfw.com/charts/pic6/050023.png')
print(result)
