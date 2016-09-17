from collections import defaultdict

class Vertex():
    def __init__(self):
        self.from_v = []
        self.to_v = []
        self.finish_time = -1
        self.visited = False

    def reverse(self):
        self.from_v, self.to_v = \
        self.to_v, self.from_v

    def __repr__(self):
        return 'from: %(from)s \
to: %(to)s' % {'from': self.from_v,
                 'to': self.to_v}


class Graph(defaultdict):
    def __init__(self):
        defaultdict.__init__(self, Vertex)
        self.timer = 0
        self.is_reversed = False
        self.stack = []
        self.scc_buffer = []
        self.scc_groups = []

    def reverse(self):
        self.is_reversed = not self.is_reversed
        for vertex in self.values():
            vertex.reverse()
            vertex.visited = False

    def dfs(self, start_name):
        start = self.get(start_name)
        start.visited = True
        for to in start.to_v:
            if self.get(to).visited == False:
                self.dfs(to)
        if self.is_reversed:
            self.stack.append(start_name)
        else:
            self.scc_buffer.append(start_name)

def parse_file(in_file_name):
    graph = Graph()
    with open (in_file_name) as lines:
        for line in lines:
            items = line.split()
            _from = items[0]
            to = items[1]
            graph[to].from_v.append(_from)
            graph[_from].to_v.append(to)
    return graph
