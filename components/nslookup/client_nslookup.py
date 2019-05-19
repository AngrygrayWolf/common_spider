# -*- coding;utf-8 -*-
import subprocess


def get_ip(domain):
    res = subprocess.Popen("nslookup {}".format(domain), stdin=subprocess.PIPE, stdout=subprocess.PIPE).communicate()[0]
    response = res.decode("GBK")
    print(response)
    res_list = response.split("s:")
    print("{}:{}".format(domain, res_list[2].split("\r\n")[:-1]))


if __name__ == "__main__":
    get_ip("www.baidu.com")
