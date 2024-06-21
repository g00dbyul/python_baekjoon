'''
백준 : 7576
https://www.acmicpc.net/problem/7576
'''

'''
6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1
'''

from collections import deque

width, height = map(int, input().split())
box = []

for i in range(height):
    box.append(list(map(int, input().split())))

visited = [[False for i in range(width)] for j in range(height)]

queue = deque([])

dxdy = [(-1,0), (1,0), (0,-1), (0,1)]
result = 0

for i in range(height):
    for j in range(width):
        if box[i][j] == 1:
            queue.append((i,j))

while queue:
    x,y = queue.popleft()
    for dx, dy in dxdy:
        if 0 <= x+dx < height and 0 <= y+dy < width and box[x+dx][y+dy] == 0:
            box[x + dx][y + dy] = box[x][y] + 1
            queue.append((x+dx, y+dy))


for row in box:
    for i in row:
        if i == 0:
            print(-1)
            exit()
        else:
            result = max(result, i-1)
print(result)
