'''
6
10 20 10 30 20 50

https://www.acmicpc.net/problem/11053
'''

N = int(input())
arr = list(
    map(int, input().split())
)

dp = [1] * N
for i in range(1,N):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))


