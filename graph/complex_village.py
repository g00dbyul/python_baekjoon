'''
백준 2667번 문제
참조 : https://www.acmicpc.net/problem/2667
'''

'''
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
'''

from collections import deque

n = int(input())

village = []
visited = []

for i in range(n):
    row = input()
    tmp = []
    visited_tmp = []
    for j in row:
        tmp.append(int(j))
        visited_tmp.append(False)
    village.append(tmp)
    visited.append(visited_tmp)

result = []

def bfs(x,y):
    dxdy = [(-1,0), (1,0), (0,-1), (0,1)]
    queue = deque([])
    queue.append((x,y))
    visited[x][y] = True
    count = 0

    while queue:
        pop_x, pop_y = queue.popleft()
        count = count + 1
        for dx, dy in dxdy:
            if 0 <= pop_x + dx < n and 0 <= pop_y + dy < n and village[pop_x + dx][pop_y + dy] == 1 and visited[pop_x + dx][pop_y + dy] == False:
                queue.append((pop_x + dx, pop_y + dy))
                visited[pop_x + dx][pop_y + dy] = True
    result.append(count)

for i in range(n):
    for j in  range(n):
        if village[i][j] == 1 and visited[i][j] == False:
           bfs(i,j)

print(len(result))
for i in sorted(result):
    print(i)
