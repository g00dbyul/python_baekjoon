'''
백준 11724번 문제
참조 : https://www.acmicpc.net/problem/11724
'''

'''
6 5
1 2
2 5
5 1
3 4
4 6
'''
from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def bfs(node, graph, visited):
    queue = deque([])
    queue.append(node)
    visited[node] = True
    while queue:
        pop = queue.popleft()
        for adj in graph[pop]:
            if visited[adj] == False:
                queue.append(adj)
                visited[adj] = True

N,M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False for i in range(0, N+1)]

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

result = 0

for i in range(1, N +1):
    if visited[i] == False:
        result = result + 1
        bfs(i, graph, visited)

print(result)
