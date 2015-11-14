import sys
from collections import defaultdict

def down_heapify(idx):
    if is_leaf(idx):
        return
    if left(idx) == len(tbd_heap) - 1:
        candidate = left(idx)
    else:
        if get_score(left(idx)) > get_score(right(idx)):
            candidate = right(idx)
        else:
            candidate = left(idx)
    if get_score(idx) < get_score(candidate):
        return
    else:
        tbd_heap[idx], tbd_heap[candidate] = tbd_heap[candidate], tbd_heap[idx]
        down_heapify(candidate)

def is_leaf(idx):
    return idx > len(tbd_heap) / 2 - 1

def left(idx):
    return idx * 2 + 1

def right(idx):
    return idx * 2 + 2

def get_score(idx):
    return v_info[tbd_heap[idx]]['score']

def parent(idx):
    return int((idx - 1) / 2)

def up_heapify(idx):
    if idx == 0:
        return
    if get_score(idx) < get_score(parent(idx)):
        tbd_heap[idx], tbd_heap[parent(idx)] = tbd_heap[parent(idx)], tbd_heap[idx]
        up_heapify(parent(idx))

def extract_min():
    if len(tbd_heap) == 1:
        return tbd_heap.pop()

    v_min = tbd_heap[0]
    tbd_heap[0] = tbd_heap.pop()
    down_heapify(0)
    #heap_build(0)  
    return v_min

def heap_insert(v):
    tbd_heap.append(v)
    up_heapify(len(tbd_heap) - 1)

def heap_delete(v):
    idx = tbd_heap.index(v)
    if idx == len(tbd_heap) - 1:
        tbd_heap.pop()
        return

    tbd_heap[idx] = tbd_heap.pop()
    if idx > 0 and get_score(idx) < get_score(parent(idx)):
        up_heapify(idx)
    else:
        down_heapify(idx)
        

def heapify(v):
    idx = tbd_heap.index(v)

    #if idx > 0 and get_score(idx) < get_score(parent(idx)):
    up_heapify(idx)
    #else:
    down_heapify(idx)

def heap_build(idx):
    if is_leaf(idx):
        return
    heap_build(left(idx))
    if not left(idx) == len(tbd_heap) - 1:
        heap_build(right(idx))
    down_heapify(idx)

def heap_pop():
    """
    min_score = sys.maxsize
    v_idx = None
    for i, v in enumerate(tbd_heap):
        if v_info[v]['score'] < min_score:
            min_score = v_info[v]['score']
            v_idx = i
    v_min = tbd_heap[v_idx]
    tbd_heap.pop(v_idx)
    return v_min
    """
    return extract_min()

def heap_update(v):
    if sys.argv[2] == 'dbg':
        print(v)
        print(v_info[v])
    for edge in v_info[v]['edges']:
        v_dst = edge['v_dst']
        length = edge['length']
        if sys.argv[2] == 'dbg':
            print(v_info[v_dst])
        if v_info[v_dst]['done'] == False:
            v_info[v_dst]['score'] = min(v_info[v_dst]['score'], v_info[v]['score'] + length)
            """
            heap_delete(v_dst)
            heap_insert(v_dst)
            """
            heapify(v_dst)
            #heap_build(0)
            

"""
def heap_update(v):
    for v_dst in v_info[v]:
        if v_dst in v_tbd:


"""

v_info = [None] * 250
v_info[0] = None
tbd_heap = []
file_name = sys.argv[1]

with open(file_name) as f_handle:
    for line in f_handle:
        row_list = line.split()
        v_src = int(row_list[0])
        v_info[v_src] = {'score': sys.maxsize, 'done': False, 'edges': []}
        tbd_heap.append(v_src)
        for edge in row_list[1:]:
            edge = edge.split(',')
            v_dst = int(edge[0])
            length = int(edge[1])
            edge = {'v_dst': v_dst, 'length': length}
            v_info[v_src]['edges'].append(edge)

if sys.argv[2] == 'dbg':
    print(v_info)

v_info[1]['score'] = 0

for i in range(250):
    if i > 0 and v_info[i] is None:
        cut = i
        break
v_info = v_info[:cut]
while len(tbd_heap) > 0:
    v_min = heap_pop()
    heap_update(v_min)
    v_info[v_min]['done'] = True

answer_list = [7,37,59,82,99,115,133,165,188,197]
answer = []
for v in answer_list:
    if v is None:
        continue
    answer.append(v_info[v]['score'])

print(answer)
