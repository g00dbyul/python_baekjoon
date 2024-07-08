'''
https://www.acmicpc.net/problem/2468

백준 2468번 문제
'''

'''
5
6 8 2 6 2
3 2 3 4 6
6 7 3 3 2
7 2 5 3 6
8 9 5 2 7

5
'''
from collections import deque

N = int(input())
area = []
maximum = 0

for i in range(N):
    arr = list(
        map(int, input().split())
    )
    max_value = max(arr)
    if maximum == 0:
        maximum = max_value
    else:
        if max_value > maximum:
            maximum = max_value
    area.append(arr)

def bfs(area, visited):
    count = 0
    queue = deque([])
    dxdy = [(-1,0), (1,0), (0,-1), (0,1)]
    for i in range(N):
        for j in  range(N):
            if area[i][j] == True and visited[i][j] == False:
                count = count + 1
                queue.append((i,j))
                visited[i][j] = False
                while queue:
                    x, y = queue.popleft()
                    for dx, dy in dxdy:
                        if 0 <= x+dx < N and 0 <= y+dy < N and area[x+dx][y+dy] == True and visited[x+dx][y+dy] == False:
                            queue.append((x+dx, y+dy))
                            visited[x + dx][y + dy] = True
    return count

results = []
for height in range(maximum+1):
    safe_area = []
    visited = []
    for row in area:
        temp = []
        visited_temp = []
        for r in row:
            visited_temp.append(False)
            if r <= height:
                temp_value = False
            else:
                temp_value = True
            temp.append(temp_value)
        visited.append(visited_temp)
        safe_area.append(temp)
    results.append(
        bfs(safe_area, visited)
    )

print(max(results))
