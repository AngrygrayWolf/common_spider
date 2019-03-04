import chardet

from util.util import get_html
from bs4 import BeautifulSoup


url = 'http://www.gov.cn/'
content = get_html(url)
encoding = chardet.detect(content)['encoding']
html = BeautifulSoup(content, 'lxml')

def has_str_href(tag):
    return tag.has_attr('src') or tag.has_attr('href')


for per in html.find_all(has_str_href):
    if per.has_attr('src'):
        title = per['src']
    elif per.has_attr('href'):
        title = per['href']
    else:
        title = 'None'
    if per.get_text():
        print("%s: %s" % (title, per.get_text()))



