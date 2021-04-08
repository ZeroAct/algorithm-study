from sys import stdin

while True:
    s = stdin.readline().rstrip()
    if s == '0':
        break
    elif s == s[::-1]:
        print('yes')
    else:
        print('no')