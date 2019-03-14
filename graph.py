from util.util import get_content, get_property, exclude, get_internal, get_external, has_str_href, remove_slash
# 仅仅适用于静态网页


def get_link(per):
    return get_property('src', per) or get_property('href', per)


class Vertex:
    def __init__(self,  url='', title='test'):
        self.title = title
        self.url = remove_slash(url)
        self.content = get_content(url)
        self.connectedTo = {}
        self.results = self.get_results()
        self.internal_links = self.get_internal()
        self.external_links = self.get_external()
        self.text = self.content.body.get_text()

    def add_neighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.url) + ' connectedTo:' + str([x.url for x in self.connectedTo])

    def get_connections(self):
        return self.connectedTo.keys()

    def get_url(self):
        return self.url

    def get_weight(self, nbr):
        return self.connectedTo[nbr]

    def get_results(self):
        # print(self.content.get_text())

        results = [(get_link(per), per.get_text()) for per in self.content.find_all(has_str_href)]

        # The results must initialized to prevent the value changed
        return list(filter(None, map(lambda x: x if exclude(x[0]) else None, results)))

    def get_internal(self):
        return list(filter(None, map(lambda x: get_internal(x), self.results)))

    def get_external(self):
        return list(filter(None, map(lambda x: get_external(x), self.results)))

    # def get_links(self):
    #     results = [(get_link(per), per.get_text()) for per in self.content.find_all(has_str_href)]
    #     # The results must initialized to prevent the value changed
    #     results = list(filter(None, map(lambda x: x if exclude(x[0]) else None, results)))
    #     self.internal_links = filter(None, map(lambda x: get_internal(x), results))
    #     self.external_links = filter(None, map(lambda x: get_external(x), results))
    #     return {self.url: {"internal": list(self.internal_links), "external": list(self.external_links)}}


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def add_vertex(self, url):
        self.numVertices = self.numVertices + 1
        new_vertex = Vertex(url)
        self.vertList[url] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def add_edge(self, f, t, cost=0):
        if f not in self.vertList:
            nv = self.add_vertex(f)
        if t not in self.vertList:
            nv = self.add_vertex(t)
        self.vertList[f].add_neighbor(t, cost)
        # pass

    def get_vertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())


def test_graph():
    g = Graph()
    for i in range(6):
        g.add_vertex(i)
    g.add_edge(0, 1, 5)
    g.add_edge(0, 5, 2)
    g.add_edge(1, 2, 4)
    g.add_edge(2, 3, 9)
    g.add_edge(3, 4, 7)
    g.add_edge(3, 5, 3)
    g.add_edge(4, 0, 1)
    g.add_edge(5, 4, 8)
    g.add_edge(5, 2, 1)
    for v in g:
        for w in v.get_connections():
            print("( %s , %s )" % (v.get_id(), w.get_id()))




def test_vertex():
    v = Vertex(url='http://www.samsan.com.tw')
    print(v.results)
    print(v.external_links)
    print(v)


def test_graph():
    g = Graph()
    url = 'http://www.samsan.com.tw'
    g.add_vertex(url='http://www.samsan.com.tw')
    v = g.vertList[url]
    # v = Vertex(url='http://www.samsan.com.tw')

    for k in v.internal_links:
        try:
            g.add_edge(url, url + k[0])
        except:
            continue
    # g.add_edge('http://www.baidu.com', 'http://www.samsan.com.tw')
    print(g)

# test_vertex()
g = Graph()
url_default = 'http://www.samsan.com.tw'
def fact(n, url):
    if n == 1:
        return
    if hasattr(g.vertList, url):
        v = g.vertList[url]
    else:
        v = g.add_vertex(url)
    for k in v.internal_links:
        try:
            g.add_edge(url, url_default + k[0])
            fact(n-1, url_default + k[0])
        except:
            continue



g = Vertex(url='http://www.samsan.com.tw')
pass
# test_graph()

# fact(3, url_default)

# print(g)
