import dns.resolver


def dns_query(domain, type):
    result = []
    try:
        A = dns.resolver.query(domain, type)
        for i in A.response.answer:
            for j in i:
                result.append(j)
        return result
    except:
        print(domain + ' 此域名，DNS未响应！')
        return None



