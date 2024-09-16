'''
6 4
0100
1110
1000
0000
0111
0000

4 4
0111
1111
1111
1110
'''
from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int, input().replace('\n','').split())
matrix = []

for _ in range(n):
    temp = input().replace('\n','')
    matrix.append(
        list(
            map(int, list(temp))
        )
    )


def bfs(matrix):
    queue = deque([])
    dxdy = [(-1,0), (1,0), (0,-1), (0,1)]
    visited = [
        [[0] * 2 for _ in range(m)] for _ in range(n)
    ]
    visited[0][0][0] = 1
    queue.append((0,0,0))

    while queue:
        x,y,z = queue.popleft()
        if x == n-1 and y == m-1:
            for i in visited:
                print(i)
            return visited[x][y][z]
        for dx,dy in dxdy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if matrix[nx][ny] == 0 and visited[nx][ny][z] == 0:
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    queue.append((nx, ny, z))
                if matrix[nx][ny] == 1 and z == 0:
                    visited[nx][ny][1] = visited[x][y][z] + 1
                    queue.append((nx, ny, 1))
    return -1

print(bfs(matrix))


