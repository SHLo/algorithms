from utils import parse
import sys
import copy
import math

def main():
    try:
        in_file_name = sys.argv[1]
    except Exception:
        sys.stderr.write('usage: python karger.py ${in_file_name}')
        return

    graph = parse(in_file_name)

    result = karger(graph)

    print(result)

def karger(graph):

    min_cut = sys.maxint

    for _ in xrange(int(math.pow(len(graph), 2))):
        graph_copied = copy.deepcopy(graph)
        cut = graph_copied.single_karger()
        min_cut = min(min_cut, cut)

    return min_cut














if __name__ == '__main__':
    main()
