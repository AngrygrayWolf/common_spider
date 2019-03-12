import os
import re
import time
import requests


def get_file_content(filepath):
    with open(filepath, 'rb') as f:
        return f.read()


def write_file_content(filepath, content):
    with open(filepath, 'wb+') as f:
        f.write(content)


def get_html(url):
    """
    :param url: 爬取的网址参数，先将爬的内容缓存起来
    :return: 返回一个soup类型
    """
    out_time = time.strftime("%Y%m%d", time.localtime())
    path_url = ''.join(re.findall(r'\w+', url))
    path = 'temp/' + path_url + '-' + out_time
    if not os.path.isfile(path):
        print('writing file')
        content = requests.get(url=url, headers={
            'user-agent': 'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.3; Win64; x64)'}).content
        write_file_content(path, content)
        return content
    else:
        return get_file_content(path)


def get_internal(w):
    # return w if re.search(r'^/', w[0]) is not None else None
    return w if not is_external(w[0]) else None


def get_external(w):
    return w if is_external(w[0]) else None


def is_external(links):
    return re.search(r"(http:|www.).*?$", links)
    # return w if re.search(r'[^http]|[www.*?]', w[0]) else None


def get_property(key, value):
    try:
        return value[key]
    except KeyError:
        return None


# dicts = ['css', 'js', 'ico']
dicts = ['css', 'js', 'ico', 'png']


# FIXME： 进行测试, 函数的使用范围不够广
def exclude(target):
    for k in dicts:
        pattern = r'.*?.' + k
        if re.match(pattern, target):
            return False
    return True
