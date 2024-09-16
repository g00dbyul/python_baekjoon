'''
10 1 10 2 1

F, S, G, U, D
F : 건물 전체 층수
S : 시작 지점
G : 회사 위치
U : 올라갈 수 있는 층
D : 내려갈 수 있는 층
'''
from collections import deque

F, S, G, U, D = map(int, input().split())
queue = deque([])
visited = [-1] * (F+1)
next_step = [U, -D]

queue.append(S)
visited[S] = 0

while queue:
    pop = queue.popleft()
    if pop == G:
        break
    for step in next_step:
        if 1 <= pop + step <= F and visited[pop + step] == -1:
            queue.append(pop + step)
            visited[pop + step] = visited[pop] + 1

if visited[G] == -1:
    print('use the stairs')
else:
    print(visited[G])

