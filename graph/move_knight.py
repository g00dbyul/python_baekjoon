'''
https://www.acmicpc.net/problem/7562
'''
'''
3
8
0 0
7 0
100
0 0
30 50
10
1 1
1 1

1
100
0 0
30 50
'''

from collections import deque
def bfs(size, start, end):
    board = [[0 for _ in range(size)] for _ in range(size)]

    queue = deque([])
    directions = [(1,2),(-1,2), (1,-2), (-1,-2), (2,1), (2,-1), (-2,1), (-2, -1)]
    queue.append((start[0], start[1]))

    while queue:
        x,y = queue.popleft()
        for dx, dy in directions:
            if 0 <= x+dx < size and 0 <= y+dy < size and board[x+dx][y+dy] == 0:
                queue.append((x+dx, y+dy))
                board[x+dx][y+dy] = board[x][y] + 1
    return board[end[0]][end[1]]

TC = int(input())

for _ in range(TC):
    size = int(input())
    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))
    print(bfs(size, start, end))

