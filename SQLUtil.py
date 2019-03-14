"""
ipv6 网址 http://v6directory.twnic.net.tw/directory.cgi 的数据库字典
"""
# todo: 可以优化为用户交互
import pymysql

ipv6_website_tw = {
    "category": "類別",
    "organization": "所屬單位",
    "url": '網站名稱',
    "IPv6": "IPv6位址"
}


def serialization(title_dicts):
    """
    获取某个数据库的属性结构，根据字典表生成
    :return:
    """
    return ','.join([key for key in title_dicts])


# todo: 这个写法不够通用
def concat_sql(results, title_dicts):
    statements = ''
    for result in results:
        statements += '("%s", "%s", "%s", "%s"),' % (
            # 直接插入极其危险
            result[title_dicts['category']], result[title_dicts['organization']], result[title_dicts['url']],
            result[title_dicts['IPv6']])

    print(statements)
    return 'insert into `ipv6_websites_tw` (category, organization, url, ipv6) VALUES ' + statements[:-1]


def insert_sql(sql: object, connection: object):
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            connection.commit()
    except:
        print('error')


def create_connection(host, user, password, db):
    connection = pymysql.connect(host=host,
                                 user=user,
                                 password=password,
                                 db=db)
    return connection
