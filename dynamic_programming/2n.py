'''
https://www.acmicpc.net/problem/11726
'''

n = int(input())

if n <= 2:
    print(n % 10007)
else:
    arr = [0] * (n + 1)
    arr[1] = 1
    arr[2] = 2

    for i in range(3, n + 1):
        arr[i] = arr[i - 1] + arr[i - 2]
    print(arr[n] % 10007)