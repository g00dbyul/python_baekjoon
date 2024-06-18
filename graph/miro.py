'''
백준 2178번
참조 : https://www.acmicpc.net/problem/2178
'''

'''
4 6
101111
101010
101011
111011
'''

from collections import deque

height, width = map(int, input().split(' '))
miro_map = []
visited = []

for i in range(0, height):
    row = input()
    tmp = []
    visited_tmp = []
    for j in row:
        tmp.append(int(j))
        visited_tmp.append(False)
    miro_map.append(tmp)
    visited.append(visited_tmp)

dxdy = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우

queue = deque([])
queue.append((0,0))
visited[0][0] = True

while queue:
    pop = queue.popleft()
    # visited[pop[0]][pop[1]] = True
    distance = miro_map[pop[0]][pop[1]]
    for dx, dy in dxdy:
        if 0 <= pop[0] + dx < height and 0 <= pop[1] + dy < width and miro_map[pop[0] + dx][pop[1] + dy] != 0 and visited[pop[0] + dx][pop[1] + dy] == False:
            queue.append((pop[0] + dx, pop[1] + dy))
            visited[pop[0] + dx][pop[1] + dy] = True
            miro_map[pop[0] + dx][pop[1] + dy] = distance + 1
            if pop[0] + dx == height - 1 and pop[1] + dy == width - 1:
                break

print(miro_map[height - 1][width - 1])





