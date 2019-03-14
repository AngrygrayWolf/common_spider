import random
import time

import bs4
import logging

from SQLUtil import concat_sql, create_connection, insert_sql
from html_util import is_valid_proxy, get_table_content
from util.util import get_html

ipv6_websites_tw = {
    "category": "類別",
    "organization": "所屬單位",
    "url": '網站名稱',
    "IPv6": "IPv6位址"
}

ipv6_url = 'http://v6directory.twnic.net.tw/directory.cgi'
connection = create_connection(host='127.0.0.1',
                               user='proxypool',
                               password='Proxypool123.',
                               db='proxypoolDB')


def save_ipv6_db(url, db_connection):
    proxy_host = {'http': 'socks5://127.0.0.1:1081'}
    print(url)
    test = get_html(url, proxy=proxy_host)
    content = bs4.BeautifulSoup(test, 'lxml')
    table = content.table
    results = get_table_content(table)
    sql = concat_sql(results, ipv6_websites_tw)
    insert_sql(sql, db_connection)


for x in range(117, 121):
    # proxy_host = {'http': 'socks5://127.0.0.1:1080'}
    one_url = ipv6_url + '?more=' + str(x*100)
    t = random.randint(1, 7)
    time.sleep(t)
    # content = get_html(one_url, proxy=proxy_host)
    save_ipv6_db(one_url, connection)
    print("has saved " + str(x))

