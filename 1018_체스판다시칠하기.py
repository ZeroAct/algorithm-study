from itertools import accumulate
from sys import stdin

N, M = map(int, stdin.readline().split())

board = [[0] * (M+1)]
for n in range(1, N+1):
    board.append([0] + list(map(int,stdin.readline().strip('\n').replace('W', '0').replace('B', '1'))))
    for m in range(1, M+1):
        board[n][m] = (n + m) % 2 == board[n][m]

for n in range(1, N+1):
    board[n] = list(accumulate(board[n]))
    for m in range(1, M+1):
        board[n][m] += board[n-1][m]

min_val = 32
for n in range(8, N+1):
    for m in range(8, M+1):
        val = board[n][m]-board[n-8][m]-board[n][m-8]+board[n-8][m-8]
        min_val = min(min_val, val, 64-val)

print(min_val)