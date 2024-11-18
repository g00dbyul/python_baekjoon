'''
4 7
20 15 10 17

https://www.acmicpc.net/problem/2805
'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

N,M = map(int, input().split())
trees = list(
map(int, input().split())
)

start, end = 0, max(trees)
mid = 0
result = []
while start <= end:
    mid = (start+end) // 2
    total = 0
    for t in trees:
        if t > mid:
            total = total + (t-mid)
    if total >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)