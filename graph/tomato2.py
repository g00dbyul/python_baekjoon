'''
백준 7569번 문제
https://www.acmicpc.net/problem/7569
'''

'''
5 3 1
0 -1 0 0 0
-1 -1 0 1 1
0 0 0 1 1
'''
import sys
from collections import deque
input = sys.stdin.readline
N, M, H = map(int, input().split())
graph = []
visited = []

for h in range(0, H):
    tmp = []
    visited_tmp = []
    for m in range(0, M):
        tmp.append(
            list(
                map(int, input().split())
            )
        )
        visited_tmp.append(False)
    graph.append(tmp)
    visited.append(visited_tmp)

queue = deque([])
dxdydz = [(-1,0,0), (1,0,0), (0,-1,0), (0,1,0), (0,0,-1), (0,0,1)]
for h in range(0, H):
    for m in range(0, M):
        for n in range(0, N):
            if graph[h][m][n] == 1:
                queue.append((h,m,n))

while queue:
    x, y, z = queue.popleft()
    for dx, dy, dz in dxdydz:
        if 0 <= x+dx < H and 0 <= y+dy < M and 0 <= z+dz < N and graph[x+dx][y+dy][z+dz] == 0:
            queue.append((x+dx, y+dy, z+dz))
            graph[x + dx][y + dy][z + dz] = graph[x][y][z] + 1

maximum = 0
for h in range(0, H):
    for m in range(0, M):
        for n in range(0, N):
            if graph[h][m][n] == 0:
                print(-1)
                exit()
            else:
                if graph[h][m][n] >= maximum:
                    maximum = graph[h][m][n]

print(maximum - 1)








