from sys import stdin
input = stdin.readline

from collections import defaultdict
N, M, V = map(int, input().split())

edges = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)
for k in edges.keys():
    edges[k].sort()

# dfs
visited = []
stack   = [V]
while len(stack):
    vertex = stack.pop(-1)
    if vertex in visited:
        continue
    visited.append(vertex)
    stack += edges[vertex][::-1]

print(' '.join(map(str, visited)))

# bfs
visited = []
queue   = [V]
while len(queue):
    vertex = queue.pop(0)
    if vertex in visited:
        continue
    visited.append(vertex)
    queue += edges[vertex]

print(' '.join(map(str, visited)))