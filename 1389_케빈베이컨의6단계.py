from sys import stdin
from collections import defaultdict
input = stdin.readline

N, M = map(int, input().split())

edges = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

min_kevin_bacon_list = []
for A in edges.keys():
    queue = [[A, 0]]
    visited = defaultdict(list)
    visited[A] = 0

    while len(queue):
        vertex, level = queue.pop(0)

        for b in edges[vertex]:
            if b not in visited.keys():
                queue.append([b, level+1])
                visited[b] = level+1
    
    min_kevin_bacon_list.append([A, sum(visited.values())])

min_kevin_bacon_list.sort(key=lambda x: x[0])
min_kevin_bacon_list.sort(key=lambda x: x[1])
print(min_kevin_bacon_list[0][0])
