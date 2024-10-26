'''
5 3
5 4 3 2 1
1 3
2 4
5 5

https://www.acmicpc.net/problem/11659
'''
import sys
input = sys.stdin.readline

N,M = map(int, input().split())
arr = list(
map(int, input().split())
)

sum_arr = [0] * (N+1)

total = 0
for i in range(1,N+1):
    total = total + arr[i-1]
    sum_arr[i] = total

for _ in range(M):
    i, j = map(int, input().split())
    print(sum_arr[j] - sum_arr[i-1])
