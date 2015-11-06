import sys
from collections import defaultdict

def dfs_ori(v):
    global cnt
    cnt += 1
    if sys.argv[2] == 'dbg':
        print('dfs_ori on: ' + str(v))
        print('cnt: ' + str(cnt))
    for to in ori_graph[v]:
        if visited[to] == False:
            visited[to] = True
            dfs_ori(to)


def dfs_rev(v):
    if sys.argv[2] == 'dbg':
        print('dfs on ' + str(v))
    global f
    for to in rev_graph[v]:
        if visited[to] == False:
            visited[to] = True
            dfs_rev(to)
    f += 1
    f_map[f] = v

def dfs_rev_itr(v):
    global f
    stack = [v]
    visited[v] = True
    while len(stack) > 0:
        v = stack[-1]
        for to in rev_graph[v]:
            if visited[to] == False:
                visited[to] = True
                stack.append(to)
                if sys.argv[2] == 'dbg':
                    print('dfs_rev_itr: ' + str(to))
                    print(stack)
                break
        else:
            stack.pop()
            f += 1
            f_map[f] = v
            if sys.argv[2] == 'dbg':
                print('finished: ' + str(v))

def dfs_ori_itr(v):
    global cnt
    stack = [v]
    visited[v] = True
    cnt += 1
    while len(stack) > 0:
        v = stack[-1]
        for to in ori_graph[v]:
            if visited[to] == False:
                stack.append(to)
                visited[to] = True
                cnt += 1
                break
        else:
            stack.pop()








file_name = sys.argv[1]

ori_graph = defaultdict(list)
visited = {}
f_map = {}
f = 0
with open(file_name) as f_handle:

    for line in f_handle:

        line_list = line.split()
        from_v = int(line_list[0])
        to_v = int(line_list[1])
        
        visited[from_v] = False
        visited[to_v] = False
        ori_graph[from_v].append(to_v)

rev_graph = defaultdict(list)

for to_v in ori_graph:
    for from_v in ori_graph[to_v]:
        rev_graph[from_v].append(to_v)

"""
with open('out.txt', 'w') as out_f:
    for from_v in rev_graph:
        
        out_f.write(str(from_v) + ' ' + str(rev_graph[from_v]) + '\n')
"""

for i in range(len(visited), 0, -1):
    if visited[i] == False:
        visited[i] = True
        dfs_rev_itr(i)

#print(f_map)
for v in visited:
    visited[v] = False

cnt = 0
answer = [0 for _ in range(5)]

for i in range(len(visited), 0, -1):
    v = f_map[i]
    if sys.argv[2] == 'dbg':
        print('i: ' + str(i) + ' v: ' + str(v))
    if visited[v] == False:
        visited[v] = True
        dfs_ori_itr(v)
        if cnt > answer[0]:
            answer.pop(0)
            answer.append(cnt)
            answer.sort()
        cnt = 0

answer.sort(reverse = True)
print(answer)
