from sys import stdin

stdin.readline()
ns = set(stdin.readline().rstrip().split())
stdin.readline()

answer = ""
for m in stdin.readline().rstrip().split():
    answer += "1\n" if m in ns else "0\n"

print(answer)