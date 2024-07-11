'''
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

27

4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2


test
7 7
2 1 0 0 1 1 0
1 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 1 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
'''
from collections import deque

import copy

N, M = map(int, input().split())
virus_map = []
for _ in range(N):
    virus_map.append(
        list(
            map(int, input().split())
        )
    )

def count_safe_area(vmap):
    count = 0
    for i in range(N):
        for j in range(M):
            if vmap[i][j] == 0:
                count = count + 1
    return count

def spread(vmap):
    visited = [[False] * M for _ in range(N)]
    queue = deque([])
    dxdy = [(-1,0), (1,0), (0,-1), (0,1)]
    for i in range(N):
        for j in range(M):
            if vmap[i][j] == 2 and visited[i][j] == False:
                queue.append((i,j))
                visited[i][j] = True
                while queue:
                    x, y = queue.popleft()
                    for dx, dy in dxdy:
                        if 0 <= x+dx < N and 0 <= y+dy < M and vmap[x+dx][y+dy] == 0 and visited[x+dx][y+dy] == False:
                            queue.append((x + dx, y + dy))
                            vmap[x + dx][y + dy] = 2
                            visited[x + dx][y + dy] == True
    return vmap

maximum = 0

def create_wall(count):
    '''
    Back-Tracking
    재귀함수를 통해 구현하며, 특정 조건에서 실행하고 결과를 분석.
    중요한 것은 재귀함수 호출 이후 변경된 데이터를 다시 원복 해줘야 함.

    이 문제에서는 2차원 배열 좌표 중에서 0인 곳 3곳을 골라 1로 변경해야 함.
    즉, 0인 곳을 3개 고르는 모든 경우의 수를 찾아야 함.
    그래서 현재 개수를 가리키는 count 변수를 매개변수로 하여 재귀함수 실행.
    '''
    global maximum
    if count == 3:
        temp_map = copy.deepcopy(virus_map)
        spread_map = spread(temp_map)
        safe_area = count_safe_area(spread_map)
        if safe_area > maximum:
            maximum = safe_area
        return
    for i in range(N):
        for j in range(M):
            if virus_map[i][j] == 0:
                virus_map[i][j] = 1
                create_wall(count + 1)
                virus_map[i][j] = 0

create_wall(0)
print(maximum)
