import sys
from utils import Vertex
from utils import Graph
from utils import parse_file
from collections import defaultdict

def main():
    try:
        in_file_name = sys.argv[1]
    except Exception:
        sys.stderr.write('Usage: python scc.py ${in_file_name}')

    graph = parse_file(in_file_name)

    result = scc(graph)

def scc(graph):
    graph.reverse()

    for vertex in graph.keys():
        if graph[vertex].visited == False:
            graph.dfs(vertex)

    graph.reverse()
    print('stack:', graph.stack)
    for vertex in reversed(graph.stack):
        if graph[vertex].visited == False:
            graph.dfs(vertex)
            print('buffer: ', graph.scc_buffer)
            graph.scc_groups.append(graph.scc_buffer[:])
            del graph.scc_buffer[:]

    print(graph.scc_groups)
    answer = sorted([len(group) for group in graph.scc_groups],
                    reverse=True)[:5]

    return answer




if __name__ == '__main__':
    main()
