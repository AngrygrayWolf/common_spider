import chardet
from util.util import get_html, is_external, get_property, exclude, get_internal, get_external
from bs4 import BeautifulSoup


url = 'http://www.samsan.com.tw'
content = get_html(url)
encoding = chardet.detect(content)['encoding']
html = BeautifulSoup(content, 'lxml')





def has_str_href(tag):
    return tag.has_attr('src') or tag.has_attr('href')


def analyze_one_page(html, url):
    results = [(get_links(per), per.get_text()) for per in html.find_all(has_str_href)]
    print(results)
    # The results must initialized to prevent the value changed
    results = list(filter(None, map(lambda x: x if exclude(x[0]) else None, results)))
    internal_links = filter(None, map(lambda x: get_internal(x), results))
    external_links = filter(None, map(lambda x: get_external(x), results))
    return {url: {"internal": list(internal_links), "external": list(external_links)}}


def get_links(per):
    return get_property('src', per) or get_property('href', per)


print(analyze_one_page(html, 'test'))


# for per in html.find_all(has_str_href):
#     if per.has_attr('src'):
#         title = per['src']
#     elif per.has_attr('href'):
#         title = per['href']
#     else:
#         title = 'None'
#     if per.get_text():
#         results.append((title, per.get_text()))

