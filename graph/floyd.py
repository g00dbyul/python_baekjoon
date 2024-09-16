'''
5
14
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
3 5 10
3 1 8
1 4 2
5 1 7
3 4 2
5 2 4
'''

import sys
input = sys.stdin.readline

INF = int(1e9)
n = int(input())
case = int(input())
graph = [[INF] * n for _ in range(n)]
for i in range(len(graph)):
    graph[i][i] = 0

for _ in range(case):
    i, j, dist = map(int, input().split())
    if graph[i-1][j-1] > dist:
        graph[i-1][j-1] = dist

for i in range(n):
    for j in range(n):
        for k in range(n):
            if graph[j][k] > graph[j][i] + graph[i][k]:
                graph[j][k] = graph[j][i] + graph[i][k]


for row in graph:
    for r in row:
        if r >= INF:
            print(0, end=' ')
        else:
            print(r, end=' ')
    print()
