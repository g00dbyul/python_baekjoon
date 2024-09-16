'''
9
7 3
7
1 2
1 3
2 7
2 8
2 9
4 5
4 6

3
'''
import sys
sys.setrecursionlimit(100000)

n = int(input())
start, end = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

depth = 0
result = []

def dfs(graph, visited, node, depth):
    depth = depth + 1
    visited[node] = True
    if node == end:
        result.append(depth)
    for adj in graph[node]:
        if visited[adj] == False:
            dfs(graph, visited, adj, depth)

dfs(graph, visited, start, 0)
if len(result) == 0:
    print(-1)
else:
    print(result[0] - 1)



