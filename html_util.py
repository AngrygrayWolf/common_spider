# 匹配域名 解析一级域名
import re

import requests

R_Domain = r'(http|https)://(www.)?(\w+(\.)?)+'

# 匹配中文英文
R_Content = r'[\u2E80-\u9FFF]+(\w+)[\u2E80-\u9FFF]+'


def normalize_url(url):
    """
    对url进行处理：
    符合： [http|https]://www.(\w+.)+/.*?
    :return:
    """
    if re.match(r'^[http|https]', url) is None:
        url = 'http://' + url
    return url


def normalize_content(content):
    """
    对网页信息进行基本收集： 包含中英文字符的集合
    :param content:
    :return:
    """
    k = re.search(R_Content, content)
    if k is None:
        return ''
    return k.group()


def is_valid(content):
    return True if content.status_code == 200 else False


def is_valid_proxy(proxy_host):
    test_url = 'http://www.baidu.com'
    try:
        html = requests.get(test_url, proxies=proxy_host, timeout=10,
                            headers={'user-agent': 'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.3; Win64; x64)'})
        if html.status_code == 200:
            print('success', proxy_host)
            return True
        else:
            print('Failed', proxy_host)
            return False
    except Exception:
        return 'error'


def get_table_content(table):
    if table.find('thead') is None:
        trs = table.find_all('tr')
        first_tr = trs[0]
        others_tr = trs[1:]
        titles = [th.get_text() for th in first_tr.find_all('th')]
        results = []
        for one_other in others_tr:
            temp = [t.get_text().replace('\n', '') for t in one_other.find_all('td')]
            per = {titles[k]: temp[k] for k in range(0, len(titles) - 1)}
            results.append(per)
    else:
        thead = table.thead
        tbodys = table.find_all('tbody')
        titles = [td.get_text() for td in thead.find_all('th')]
        results = []
        for tbody in tbodys:
            temp = [td.get_text() for td in tbody.find_all('td')]
            per = {titles[k]: temp[k] for k in range(0, len(titles) - 1)}
            results.append(per)
        return results
