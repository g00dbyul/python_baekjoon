'''
7
1 6
6 3
3 5
4 1
2 4
4 7
'''
from collections import deque

N = int(input())

vertex = [[] for _ in range(N+1)]
for i in range(N-1):
    a,b = map(int, input().split())
    vertex[a].append(b)
    vertex[b].append(a)

queue = deque([])
queue.append(1)
parent = [0 for _ in range(N+1)]

while queue:
    pop = queue.popleft()
    for node in vertex[pop]:
        if parent[node] == 0:
            parent[node] = pop
            queue.append(node)

for i in range(2,len(parent)):
    print(parent[i])



