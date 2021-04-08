from sys import stdin
input = stdin.readline

N = int(input())

costs = list(map(int, input().split()))
for _ in range(N-1):
    cost = list(map(int, input().split()))
    costs = [
        cost[0] + min(costs[1:]),
        cost[1] + min(costs[0::2]),
        cost[2] + min(costs[0:2])
    ]

print(min(costs))