'''
3
0 1 0
0 0 1
1 0 0

1 1 1
1 1 1
1 1 1


7
0 0 0 1 0 0 0
0 0 0 0 0 0 1
0 0 0 0 0 0 0
0 0 0 0 1 1 0
1 0 0 0 0 0 0
0 0 0 0 0 0 1
0 0 1 0 0 0 0

1 0 1 1 1 1 1
0 0 1 0 0 0 1
0 0 0 0 0 0 0
1 0 1 1 1 1 1
1 0 1 1 1 1 1
0 0 1 0 0 0 1
0 0 1 0 0 0 0
'''
from collections import deque

n = int(input())
adjacent = [
    list(map(int, input().split())) for _ in range(n)
]

result = [
    [0]*n for _ in range(n)
]

def bfs(x):
    queue = deque()
    queue.append(x)
    check = [False for _ in range(n)]

    while queue:
        q = queue.popleft()

        for i in range(n):
            if check[i] == False and adjacent[q][i] == 1:
                queue.append(i)
                check[i] = True
                result[x][i] = 1

for i in range(0, n):
    bfs(i)

for row in result:
    for r in row:
        print(r, end=' ')
    print()








