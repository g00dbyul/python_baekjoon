'''
https://www.acmicpc.net/problem/10026
'''

'''
5
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR

4 3
'''

from collections import deque

N = int(input())

picture = []
for _ in range(N):
    line = input()
    temp = []
    for i in range(len(line)):
        temp.append(line[i])
    picture.append(temp)

def bfs_normal(picture):
    visited = [[False for _ in range(N)] for _ in range(N)]
    dxdy = [(-1,0), (1,0), (0,-1), (0,1)]
    colors = ['R','G', 'B']
    queue = deque([])
    count = 0

    for color in colors:
        for i in range(N):
            for j in range(N):
                if picture[i][j] == color and visited[i][j] == False:
                    queue.append((i,j))
                    visited[i][j] = True
                    while queue:
                        x, y = queue.popleft()
                        for dx, dy in dxdy:
                            if 0 <= x+dx < N and 0 <= y+dy < N and picture[x+dx][y+dy] == color and visited[x+dx][y+dy] == False:
                                queue.append((x+dx, y+dy))
                                visited[x + dx][y + dy] = True
                    count = count + 1
    return count

def bfs_imnormal(picture):
    visited = [[False for _ in range(N)] for _ in range(N)]
    dxdy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # colors = ['R', 'G', 'B']
    queue = deque([])
    count = 0

    for i in range(N):
        for j in range(N):
            if picture[i][j] == 'B' and visited[i][j] == False:
                queue.append((i,j))
                visited[i][j] = True
                while queue:
                    x, y = queue.popleft()
                    for dx, dy in dxdy:
                        if 0 <= x + dx < N and 0 <= y + dy < N and picture[x + dx][y + dy] == 'B' and visited[x + dx][
                            y + dy] == False:
                            queue.append((x + dx, y + dy))
                            visited[x + dx][y + dy] = True
                count = count + 1

    for i in range(N):
        for j in range(N):
            if picture[i][j] != 'B' and visited[i][j] == False:
                queue.append((i,j))
                visited[i][j] = True
                while queue:
                    x, y = queue.popleft()
                    for dx, dy in dxdy:
                        if 0 <= x + dx < N and 0 <= y + dy < N and picture[x + dx][y + dy] != 'B' and visited[x + dx][
                            y + dy] == False:
                            queue.append((x + dx, y + dy))
                            visited[x + dx][y + dy] = True
                count = count + 1
    return count



print(bfs_normal(picture), bfs_imnormal(picture))

