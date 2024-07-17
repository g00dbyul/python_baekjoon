'''
1 1
0
2 2
0 1
1 0
3 2
1 1 1
1 1 1
5 4
1 0 1 0 0
1 0 0 0 0
1 0 1 0 1
1 0 0 1 0
5 4
1 1 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 1 1
5 5
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0
'''

from collections import deque

def bfs(jido):
    width, height = len(jido[0]), len(jido)
    queue = deque([])
    visited = [
        [False for _ in range(width)] for _ in range(height)
    ]
    dxdy = [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (1,-1), (1,1), (-1,1)]
    count = 0
    # 상,하,좌,우, 좌상, 좌하, 우상, 우하
    for i in range(height):
        for j in range(width):
            if jido[i][j] == 1 and visited[i][j] == False:
                queue.append((i,j))
                visited[i][j] = True
                while queue:
                    x, y = queue.popleft()
                    for dx, dy in dxdy:
                        if 0 <= x+dx < height and 0 <= y+dy < width and jido[x+dx][y+dy] == 1 and visited[x+dx][y+dy] == False:
                            queue.append((x+dx, y+dy))
                            visited[x + dx][y + dy] = True
                count = count + 1
    return count


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    jido = []
    for _ in range(h):
        temp = list(
            map(int, input().split())
        )
        jido.append(temp)
    print(bfs(jido))


