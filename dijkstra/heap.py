class Heap():
    def __init__(self, graph):
        self.graph = graph
        self.data = [str(v) for v in range(1, len(graph) + 1)]

    def _get_key(self, idx):
        data = self.data
        vertex_name = data[idx]
        return self.graph[vertex_name]['score']

    def heapify(self, vertex_name):
        idx = self.data.index(vertex_name)

        self._up_heapify(idx)
        self._down_heapify(idx)

    def extract_min(self):
        data = self.data
        if len(data) == 1:
            return data.pop()

        _min = data[0]
        data[0] = data.pop()

        self._down_heapify(0)
        return _min

    def _up_heapify(self, idx):
        data = self.data
        if idx == 0:
            return
        parent = (idx - 1) / 2

        if self._get_key(parent) > self._get_key(idx):
            data[parent], data[idx] = data[idx], data[parent]
            self._up_heapify(parent)

    def _down_heapify(self, idx):
        data = self.data
        left = idx * 2 + 1
        right = idx * 2 + 2

        if left > len(data) - 1:
            return

        elif left == len(data) - 1:
            candidate = left

        else:
            if self._get_key(left) < self._get_key(right):
                candidate = left
            else:
                candidate = right

        if self._get_key(candidate) < self._get_key(idx):
            data[idx], data[candidate] = data[candidate], data[idx]
            self._down_heapify(candidate)





