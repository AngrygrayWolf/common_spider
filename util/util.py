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