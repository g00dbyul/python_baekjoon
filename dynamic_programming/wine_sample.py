'''
6
6
10
13
9
8
1

https://www.acmicpc.net/problem/2156
'''
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))


if n < 3:
    if n == 1:
        print(arr[0])
    else:
        print(arr[0]+arr[1])
else:
    dp = [0] * (n)
    dp[0] = arr[0]
    dp[1] = arr[0]+arr[1]
    dp[2] = max(arr[2]+dp[0], dp[1], arr[1]+arr[2])


    for i in range(3, n):
        dp[i] = max(dp[i-1], dp[i-2] + arr[i], dp[i-3] + arr[i-1] + arr[i])

    print(max(dp))