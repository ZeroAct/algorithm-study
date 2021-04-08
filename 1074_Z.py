from sys import stdin
input = stdin.readline

N, r, c = map(int, input().split())

def recur(m, r, c):
    if m == 2:
        return 2*r + c
    m //= 2
    row = 0 if r < m else 1
    col = 0 if c < m else 1
    return recur(m, r-row*m, c-col*m) + (2*row+col)*m*m

print(recur(2**N, r, c))