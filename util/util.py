import logging
import os
import re
import time
import requests
from bs4 import BeautifulSoup

# 匹配域名 解析一级域名
from html_util import is_valid

R_Domain = r'(http|https)://(www.)?(\w+(\.)?)+'

# 匹配中文英文
R_Content = r'[\u2E80-\u9FFF]+(\w+)[\u2E80-\u9FFF]+'
logging.basicConfig(filename='../log/out/output.log', level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S')


def get_file_content(filepath):
    with open(filepath, 'rb') as f:
        return f.read()


def write_file_content(filepath, content):
    with open(filepath, 'wb+') as f:
        f.write(content)


def get_html(url, proxy=None):
    """
    :param proxy: 代理
    :param url: 爬取的网址参数，先将爬的内容缓存起来
    :return: 返回一个soup类型
    """
    out_time = time.strftime("%Y%m%d", time.localtime())
    path_url = ''.join(re.findall(r'\w+', url))
    path = 'temp/' + path_url + '-' + out_time
    if not os.path.isfile(path):
        logging.info('the %s is not exist' % url)
        if proxy is None:
            content = requests.get(url=url, headers={'user-agent': 'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT '
                                                                   '6.3; Win64; x64)'})
        else:
            # todo: 考虑代理失效的情况
            content = requests.get(url=url, proxies=proxy, headers={'user-agent': 'Mozilla/5.0 (compatible; MSIE 8.0; '
                                                                                  'Windows NT '
                                                                                  '6.3; Win64; x64)'})
            if is_valid(content):
                logging.info('%s SUCCESS' % url)
                content = content.content
            else:
                logging.warning('%s ERROR %s' % (url, content.status_code))
                return 'error'

        write_file_content(path, content)
        return content
    else:
        return get_file_content(path)


def get_content(url):
    content = get_html(url)
    return BeautifulSoup(content, 'lxml')


def has_str_href(tag):
    return tag.has_attr('src') or tag.has_attr('href')


def get_internal(w):
    # return w if re.search(r'^/', w[0]) is not None else None
    return w if not is_external(w[0]) else None


def get_external(w):
    return w if is_external(w[0]) else None


def is_external(links):
    return re.search(r"(http:|www.).*?$", links)
    # return w if re.search(r'[^http]|[www.*?]', w[0]) else None


def remove_slash(url):
    if re.match(r'.*/$', url):
        return url[:-1]
    return url


def get_property(key, value):
    # print(value)
    # if key in value:
    #     return value[key]
    # else:
    #     return None
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
