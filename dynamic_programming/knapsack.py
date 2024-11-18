'''
4 7
6 13
4 8
3 6
5 12

https://www.acmicpc.net/problem/12865
'''

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [[0, 0]]
for i in range(n):
    arr.append(list(map(int, input().split())))
dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1): # 후보군
    for j in range(1, k + 1): # 무게 1 ~ k 까지
        if j < arr[i][0]: # 후보군의 무게가 더 크면 안 넣으면 됨, 직전 값으로 대치
            dp[i][j] = dp[i - 1][j]
        else: # 무게가 작은 경우 : 넣는 경우 vs 안 넣는 경우(안넣는 경우는 앞의 조건과 동일, 후보군 무게 + 앞서 넣은 블록을 제외한 무게)
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - arr[i][0]] + arr[i][1])

print(dp[n][k])
