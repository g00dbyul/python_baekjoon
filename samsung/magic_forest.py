'''
6 5 6
2 3
2 0
4 2
2 0
2 0
2 2

29
'''

from collections import deque

# 이동 우선순위 : 남 > 서 > 동
R, C, K = map(int, input().split())
# R : 높이, C: 넓이
forest = [[0] * (C) for _ in range(R)]
golem_list = []
for _ in range(K):
    start, exit = map(int, input().split())
    golem_list.append((start, exit))

# 해당 좌표가 이동 가능한지 확인

def check(x,y):
    if y < 0:
        return (0 <= x < C) and (y < R)
    else:
        return (0 <= x < C) and (y < R) and (forest[y][x] == 0)

stamp = {
    0: (0, -1),
    1: (1, 0),
    2: (0, 1),
    3: (-1, 0),
    4: (0, 0)
}

result = 0

def bfs(x,y):
    global result
    dxdy = [(0,-1), (0,1), (-1,0), (1,0)]
    queue = deque([])
    visited = [[False] * (C) for _ in range(R)]

    queue.append((x,y))
    visited[y][x] = True
    layers = []

    while queue:
        pop_x, pop_y = queue.popleft()
        layers.append(pop_y)
        for dx, dy in dxdy:
            # 우선 같은 인덱스 안 에서만 탐색 가능
            if 0 <= pop_x+dx < C and 0 <= pop_y+dy < R:
                if (abs(forest[pop_y+dy][pop_x+dx]) == abs(forest[pop_y][pop_x])) and visited[pop_y+dy][pop_x+dx] == False:
                    queue.append((pop_x+dx, pop_y+dy))
                    visited[pop_y+dy][pop_x+dx] = True
                elif forest[pop_y][pop_x] < 0 and forest[pop_y+dy][pop_x+dx] != 0 and visited[pop_y+dy][pop_x+dx] == False:
                    queue.append((pop_x + dx, pop_y + dy))
                    visited[pop_y + dy][pop_x + dx] = True
    # print("Layer",max(layers))
    result = result + (max(layers) + 1)


for index, golem in enumerate(golem_list):
    position_x, position_y, exit = golem[0]-1, -2, golem[1]
    while True:
        if check(position_x-1, position_y+1) and check(position_x, position_y+2) and check(position_x+1, position_y+1):
            position_y = position_y + 1
        elif check(position_x-1, position_y-1) and check(position_x-2, position_y) and check(position_x-1, position_y+1) and check(position_x-2, position_y+1) and check(position_x-1, position_y+2):
            position_y = position_y + 1
            position_x = position_x - 1
            exit = (exit - 1) % 4
        elif check(position_x+1, position_y-1) and check(position_x+2, position_y) and check(position_x+1, position_y+1) and check(position_x+2, position_y+1) and check(position_x+1, position_y+2):
            position_y = position_y + 1
            position_x = position_x + 1
            exit = (exit + 1) % 4
        else:
            if position_y < 1:
                # 지도 초기화
                forest = [[0] * (C) for _ in range(R)]
            else:
                # 지도그리기
                for s in stamp:
                    dx, dy = stamp[s]
                    forest[position_y + dy][position_x + dx] = index + 1
                    if s == exit:
                        forest[position_y + dy][position_x + dx] = -(index + 1)
                    else:
                        forest[position_y + dy][position_x + dx] = index + 1
                bfs(position_x, position_y)
            break

print(result)