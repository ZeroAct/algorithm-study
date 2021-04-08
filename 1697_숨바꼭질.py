from sys import stdin
input = stdin.readline

N, K = map(int, input().split())

if N >= K:
    step = N - K
else:
    queue = [[N, 0]]
    visited = [False] * 100001
    while queue:
        n, step = queue.pop(0)
        if n == K:
            break

        for k in [n-1, n+1, n*2]:
            if 0 <= k < 100001:
                if not visited[k]:
                    visited[k] = True
                    queue.append([k, step+1])

print(step)
