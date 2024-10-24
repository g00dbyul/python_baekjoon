'''
1 1
2 1
3 1
4 3 1
5 4 3 1
6 2 1
7 6 2 1
8 4 2 1
9 3 1
10 9 3 1
11 10 9 3 1
12 4 2 1
15
1000000

https://www.acmicpc.net/problem/1463
'''

X = int(input())
arr = [0] * (X+1)

for i in range(2, X+1):
    arr[i] = arr[i - 1] + 1
    if i % 2 == 0:
        arr[i] = min(arr[i], arr[i // 2] + 1)
    if i % 3 == 0:
        arr[i] = min(arr[i], arr[i // 3] + 1)

print(arr[X])

