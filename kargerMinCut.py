import sys
import random

def edges_update(vertex_objs, edges):

    #edges = filter(lambda item: not item[0]['value'] == item[1]['value'], edges)
    #edges = [item for item in edges if not item[0]['value'] == item[1]['value']]
    """
    to_delete = []
    for i, edge in enumerate(edges):
        if edge[0]['value'] == edge[1]['value']:
            to_delete.append(i)
    """
    finished = False
    to_delete = None
    while True:
        for i, edge in enumerate(edges):
            if edge[0]['value'] == edge[1]['value']:
                to_delete = i
                break
        else:
            break
        edges.pop(to_delete)
    """
    for i in to_delete:
        edges.pop(i)
    """


def contract(vertex_objs, edges):
    edge_contract = random.choice(edges)
    #print('contract: ', edge_contract)
    super_vertex = min(edge_contract[0]['value'], edge_contract[1]['value'])
    replaced_vertex = max(edge_contract[0]['value'], edge_contract[1]['value'])
    vertex_objs[replaced_vertex]['value'] = super_vertex
    for key in vertex_objs:
        if vertex_objs[key]['value'] == replaced_vertex:
            vertex_objs[key]['value'] = super_vertex
    edges_update(vertex_objs, edges)

def min_cut_routine():
    file_name = sys.argv[1]

    vertex_objs = {}
    edges = []
    vertex_cnt = 0
    with open(file_name) as f:
        for line in f:
            vertex_cnt += 1
            vertex_row = line.strip().split()
            vertex_curr = int(vertex_row[0])
            vertex_objs[vertex_curr] = {'value': vertex_curr}

    with open(file_name) as f:
        for line in f:
            vertex_row = line.strip().split()
            vertex_curr = int(vertex_row[0])
            for v in vertex_row:
                v = int(v)
                if v > vertex_curr:
                    edges.append((vertex_objs[vertex_curr], vertex_objs[v]))
            
    while vertex_cnt > 2:
        contract(vertex_objs, edges)
        vertex_cnt -= 1
        """
        print(edges)
        print(vertex_objs)
        """
    cuts = len(edges)
    print(cuts)
    return cuts

times = int(sys.argv[2])
min_cuts = sys.maxsize
while times > 0:
    cuts = min_cut_routine()
    if cuts < min_cuts:
        min_cuts = cuts
    times -= 1

print('result: ', min_cuts)
"""
print(edges)
print(vertex_objs)
"""

#edge_contract = edges.pop(random.randint(0, len(edges) - 1))

