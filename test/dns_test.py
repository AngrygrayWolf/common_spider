from components.nslookup.client import dns_query

print(dns_query('baidu.com', 'NS'))
print(dns_query('www.baidu.com', 'A'))
print(dns_query('www.a.shifen.com', 'A'))

dns_query('163.com', 'MX')
print(dns_query('163.com', 'CNAME'))
print(dns_query('www.uwintech.cn', 'CNAME')[0])