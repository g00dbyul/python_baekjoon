'''
백 1012번 문제
참조 : https://www.acmicpc.net/problem/1012
'''

'''
1 : tc
2 : 가로, 세로, 배추개수
배추개수 반복

2
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 1
5 5
'''

from collections import deque

tc = int(input())

dxdy = [(-1,0), (1,0), (0,-1), (0,1)]

for i in range(tc):
    n,m,w = map(int, input().split())
    baechoo_map = []
    visited = []
    for j in range(n):
        tmp = []
        visited_tmp = []
        for k in range(m):
            tmp.append(0)
            visited_tmp.append(False)
        baechoo_map.append(tmp)
        visited.append(visited_tmp)

    for j in range(w):
        x, y = map(int, input().split())
        baechoo_map[x][y] = 1


    result = 0
    queue = deque([])
    for j in range(n):
        for k in range(m):
            if baechoo_map[j][k] == 1 and visited[j][k] == False:
                queue.append((j,k))
                visited[j][k] = True
                while queue:
                    x, y = queue.popleft()
                    for dx, dy in dxdy:
                        if  0 <= x+dx < n and 0 <= y+dy < m and baechoo_map[x+dx][y+dy] == 1 and visited[x+dx][y+dy] == False:
                            queue.append((x+dx, y+dy))
                            visited[x+dx][y+dy] = True
                result = result + 1
    print(result)


