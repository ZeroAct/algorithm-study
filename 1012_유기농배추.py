from sys import stdin
input = stdin.readline

def find_neighbors(vertexes, vertex, M, N, visited):
    y, x = vertex
    neighbors = []
    for y_, x_ in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
        ny = y + y_
        nx = x + x_
        if 0 <= ny < M and 0 <= nx < N and \
            [ny, nx] in vertexes and [ny, nx] not in visited:
            neighbors.append([ny, nx])
    
    return neighbors

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    vertexes = []
    for _ in range(K):
        vertexes.append(list(map(int, input().split())))

    queue = []
    visited = []
    count = 0

    while len(visited) != len(vertexes):
        for vertex in vertexes:
            if vertex not in visited:
                visited.append(vertex)
                queue.append(vertex)
                break
        
        while len(queue):
            vertex = queue.pop(0)
            neighbors = find_neighbors(vertexes, vertex, M, N, visited)
            for neighbor in neighbors:
                visited.append(neighbor)
                queue.append(neighbor)

        count += 1

    print(count)