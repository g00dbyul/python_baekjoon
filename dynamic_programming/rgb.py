'''
3
26 40 83
49 60 57
13 89 99

8
71 39 44
32 83 55
51 37 63
89 29 100
83 58 11
65 13 15
47 25 29
60 66 19

https://www.acmicpc.net/problem/1149
'''

N = int(input())
rgb = []
for _ in range(N):
    rgb.append(
        list(
            map(int, input().split())
        )
    )

dp = [[0]*3 for _ in range(N)]
dp[0] = rgb[0]

for i in range(1,N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + rgb[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + rgb[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + rgb[i][2]

print(min(dp[-1]))





