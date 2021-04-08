from sys import stdin
input = stdin.readline

N = int(input())
ch_len = len(str(N))
M = int(input())
available = [i for i in range(10)]

if M > 0:
    for r in set(map(int, input().split())):
        available.remove(r)

def check(available, target):
    target_nums = list(map(int, str(target)))
    res = True
    for target_num in target_nums:
        if target_num not in available:
            res = False
            break
    return res

cost = abs(N - 100)

for tmp in range(0, 1000001):
    if check(available, tmp):
        cost = min(len(str(tmp)) + abs(N - tmp), cost)

print(cost)