'''
5 7 3
0 2 4 4
1 1 2 5
4 0 6 2

3
1 7 13
'''

from collections import deque

N,M,K = map(int, input().split())

graph = [
    [0 for _ in range(M)] for _ in range(N)
]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1

result = []
queue = deque([])
visited  = [
    [False for _ in range(M)] for _ in range(N)
]

directions = [(1,0), (-1,0), (0,1), (0,-1)]

for i in range(N):
    for j in range(M):
        count = 0
        if graph[i][j] == 0 and visited[i][j] == False:
            queue.append((i, j))
            visited[i][j] = True
            count = count + 1
            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                    if 0 <= x+dx < N and 0 <= y+dy < M and visited[x+dx][y+dy] == False and graph[x+dx][y+dy] == 0:
                        queue.append((x+dx, y+dy))
                        visited[x + dx][y + dy] = True
                        count = count + 1
            result.append(count)

print(len(result))
for i in sorted(result):
    print(i, end=' ')
