import json

import requests


def http_get(url, params):
    try:
        req = requests.get(url, params=params)
        res = str(req.content, encoding='utf8')
    #     TODO: Should complete error information
    except:
        res = ''
        print("error")
    return res


class Client:
    """
    通过virustotal爬取子域名信息
    """
    def __init__(self, key):
        self.key = key
        self.base_url = "https://www.virustotal.com"
        self.search_api_url = "/vtapi/v2/domain/report"

    def get_domain_infos(self, domain):
        """
        通过api的方式获取子域名信息
        :return:
        """
        api_full_url = "{base}{query}".format(base=self.base_url, query=self.search_api_url)
        params = {"apikey": self.key, "domain": domain}
        res = http_get(api_full_url, params)
        return json.loads(res)

    def get_subdomains(self, domains):
        """
        :param domains: 域名数据集合
        :return: 对应的子域名数据{"domain1": ["sub1", "sub2]}, ..
        """
        return {v: self.get_domain_infos(v)["subdomains"] for v in domains}


