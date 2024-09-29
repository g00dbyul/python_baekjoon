'''
3 3
1 1 0
1 1 1
1 0 1
1 1 1

11 10
7 4 0
1 1 1 1 1 1 1 1 1 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 1 1 1 1 0 1
1 0 0 1 1 0 0 0 0 1
1 0 1 1 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1
'''
from collections import deque

front = {
    0: (-1, 0),
    1: (0, 1),
    2: (1, 0),
    3: (0, -1)
}
back = {
    0: (1, 0),
    1: (0, -1),
    2: (-1, 0),
    3: (0, 1)
}
graph = []
queue = deque([])


def change_direction(n):
    return (n + 3) % 4


N, M = map(int, input().split())
r, c, d = map(int, input().split())
for _ in range(N):
    graph.append(
        list(
            map(int, input().split())
        )
    )

queue.append((r, c))
count = 0

while queue:
    x, y = queue.popleft()
    if graph[x][y] == 0:
        graph[x][y] = 2
        count = count + 1
    is_possible_clean = False
    for i in range(4):
        d = change_direction(d)
        dir_x, dir_y = front[d]
        if graph[x + dir_x][y + dir_y] == 0 and 0 <= x + dir_x < N and 0 <= y + dir_y < M:
            queue.append((x + dir_x, y + dir_y))
            is_possible_clean = True
            break
    if not is_possible_clean:
        dir_x, dir_y = back[d]
        if graph[x + dir_x][y + dir_y] != 1 and 0 <= x + dir_x < N and 0 <= y + dir_y < M:
            queue.append((x + dir_x, y + dir_y))
        elif graph[x + dir_x][y + dir_y] == 1:
            break

print(count)
