import random

def parse(file_name):
    graph = Graph()
    with open(file_name) as lines:
        for line in lines:
            v_list = line.split()
            focus = v_list[0]
            graph[focus] = v_list[1:]
    return graph

class Graph(dict):
    def _contract(self, v1, v2):
        self[v1] = [v for v in self[v1] if v != v2]
        self[v2] = [v for v in self[v2] if v != v1]

        self[v1].extend(self[v2])

        del self[v2]

        for scatter in set(self[v1]):
            self[scatter] = [v1 if (v == v2) else v for v in self[scatter]]

    def single_karger(self):
        while len(self.keys()) > 2:
            v1 = random.choice(self.keys())
            v2 = random.choice(list(set(self[v1])))

            self._contract(v1, v2)

        return len(self.values()[0])
