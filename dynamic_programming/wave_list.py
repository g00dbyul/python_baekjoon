'''
2
6
12

https://www.acmicpc.net/problem/9461
'''

arr = [1] * (101)
for i in range(4,101):
    arr[i] = arr[i-3] + arr[i-2]

T = int(input())
for _ in range(T):
    n = int(input())
    print(arr[n])