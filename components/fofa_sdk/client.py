# -*- coding: utf-8 -*-
import base64
import json
import urllib.parse
# from urllib import request
import requests

def http_get(url, param):
    # param = bytes(param)
    # param = urllib.parse.urlencode(param)
    # url = "%s?%s" % (url, param)
    try:
        req = requests.get(url, params=param)
        res = req.content
        res = str(res, encoding='utf8')
        if "errmsg" in res:
            raise RuntimeError(res)
    #     todo: test the runtime error whether normal
    except RuntimeError as e:
        print("errmsg：", e.content())
        raise e
    return res


class Client:
    """
    通过fofa api爬取数据
    """

    def __init__(self, email, key):
        self.email = email
        self.key = key
        self.base_url = "https://fofa.so"
        self.search_api_url = "/api/v1/search/all"
        self.login_api_url = "/api/v1/info/my"
        self.get_userinfo()  # check email and key

    def get_userinfo(self):
        """
        获取用户信息
        :return:
        """
        api_full_url = "%s%s" % (self.base_url, self.login_api_url)
        param = {"email": self.email, "key": self.key}
        res = http_get(api_full_url, param)
        return json.loads(res)

    def get_data(self, query_str, page=1, fields=""):
        res = self.get_json_data(query_str, page, fields)
        return json.loads(res)

    def get_json_data(self, query_str, page=1, fields=""):
        api_full_url = "%s%s" % (self.base_url, self.search_api_url)
        query_str = bytes(query_str, encoding="utf8")
        param = {"qbase64": base64.b64encode(query_str), "email": self.email, "key": self.key, "page": page,
                 "fields": fields}
        res = http_get(api_full_url, param)

        return res

    def get_domains(self, ip=""):
        query = """ip={0}""".format(ip)
        fileds = "domain"
        raw_domains = self.get_data(query, fields=fileds)["results"]
        domains = list(set([one for one in raw_domains if one is not ""]))
        if not domains:
            return 'No results'
        return domains


