import sys
from collections import defaultdict

file_name = sys.argv[1]

ori_graph = defaultdict(list)

with open(file_name) as f_handle:
    for line in f_handle:

        line_list = line.split()
        from_v = int(line_list[0])
        to_v = int(line_list[1])

        ori_graph[from_v].append(to_v)

rev_graph = defaultdict(list)

for to_v in ori_graph:
    for from_v in ori_graph[to_v]:
        rev_graph[from_v].append(to_v)

