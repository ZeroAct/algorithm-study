from sys import stdin

N = int(stdin.readline())

words = list(set([stdin.readline().rstrip() for _ in range(N)]))
words.sort()
words.sort(key=lambda x: len(x))

print('\n'.join(words))