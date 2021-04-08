n = int(input())

arr = [0, 0, 1, 1]

for i in range(4, n+1):
    tmp = []
    if i%3==0:
        tmp.append(arr[i//3])
    if i%2==0:
        tmp.append(arr[i//2])
    tmp.append(arr[i-1])

    arr.append(min(tmp) + 1)

print(arr[n])