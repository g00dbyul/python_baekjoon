'''
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5

https://www.acmicpc.net/problem/1932
'''
import sys
input = sys.stdin.readline

n = int(input())
triangle = []
for _ in range(n):
    triangle.append(
        list(
            map(int, input().split())
        )
    )

for i in range(1,n):
    for j in range(i+1):
        if j == 0:
            triangle[i][0] = triangle[i][0] + triangle[i-1][0]
        elif j == i:
            triangle[i][-1] = triangle[i][-1] + triangle[i-1][-1]
        else:
            triangle[i][j] = triangle[i][j] + max(triangle[i-1][j], triangle[i-1][j-1])

print(max(triangle[-1]))


