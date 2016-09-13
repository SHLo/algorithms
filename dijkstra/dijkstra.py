import sys
from heap import Heap

def main():

    try:
        in_file_name = sys.argv[1]
    except Exception:
        sys.stderr.write('Usage: python dijkstra ${in_file_name}')

    graph = parse_in_file(in_file_name)
    result = dijkstra(graph)

def dijkstra(graph):
    result = {}
    heap = Heap(graph)
    curr = _extract_min_score_vertex(graph, heap)
    graph[curr]['score'] = 0
    graph[curr]['path'] = []


    while(True):
        _update_scores(graph, curr, heap)
        result.update({curr: graph[curr]})
        del graph[curr]

        if len(graph) == 0:
            break

        curr = _extract_min_score_vertex(graph, heap)

    result = {
        key: {
            'length': value['score'],
            'path': value['path']
        } for key, value in result.items()
    }
    return result

def parse_in_file(in_file_name):

    graph = {}
    with open(in_file_name) as lines:
        for line in lines:
            line_cols = line.split()
            _from = line_cols[0]
            edges = [{'to': tup.split(',')[0],
                        'length': int(tup.split(',')[1])} \
                     for tup in line_cols[1:]]
            graph[_from] = {'score': sys.maxint,
                            'edges': edges,
                            'path': []}


    return graph

def _update_scores(graph, vertex_name, heap):
    for edge in graph[vertex_name]['edges']:
        to = edge['to']
        if to not in graph:
            continue
        length = edge['length']
        old_score = graph[to]['score']
        new_score = graph[vertex_name]['score'] + length
        if new_score < old_score:
            graph[to]['score'] = new_score
            heap.heapify(to)
            graph[to]['path'] = graph[vertex_name]['path'] + [to]


def _extract_min_score_vertex(graph, heap):
    return heap.extract_min()

#    min_score = sys.maxint
#    for v in graph.keys():
#        if graph[v]['score'] < min_score:
#            min_score = graph[v]['score']
#            min_vertex = v
#    return min_vertex








if __name__ == '__main__':
    main()
