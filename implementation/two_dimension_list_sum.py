'''
2 3
1 2 4
8 16 32
3
1 1 2 3
1 2 1 2
1 3 2 3
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
arr = []
for _ in range(N):
    tmp = list(
        map(int, input().rstrip().split())
    )
    arr.append(tmp)
sum_arr = [[0 for _ in range(M+1)] for _ in range(N+1)]

for n in range(1,N+1):
    for m in range(1,M+1):
        sum_arr[n][m] = sum_arr[n-1][m] + sum_arr[n][m-1] - sum_arr[n-1][m-1] + arr[n-1][m-1]

K = int(input())
for _ in range(K):
    i,j,x,y = map(int, input().rstrip().split())

    print(
        sum_arr[x][y] - sum_arr[x][j-1] - sum_arr[i-1][y] + sum_arr[i-1][j-1]
    )


