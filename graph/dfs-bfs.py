'''
백준 1260번 문제
참조 : https://www.acmicpc.net/problem/1260
'''

'''
첫번째 : node 갯수
두번째 : 간선 갯수
세번째 : 시작점

Example 1 - Input
4 5 1
1 2
1 3
1 4
2 4
3 4

Example 1 - Output
1 2 4 3
1 2 3 4
'''

from collections import deque

def dfs(graph, visited, start):
    print(start, end=' ')
    visited[start] = True
    for point in sorted(graph[start]):
        if visited[point] == False:
            dfs(graph, visited, point)

def bfs(graph, visited, start):
    queue = deque([])
    queue.append(start)
    visited[start] = True
    while queue:
        pop = queue.popleft()
        print(pop, end=' ')
        for point in sorted(graph[pop]):
            if visited[point] == False:
                queue.append(point)
                visited[point] = True


node, vertex, start = map(int, input().split(' '))

adjacent_map = {}
dfs_visited = [False] * (node+1)
bfs_visited = [False] * (node+1)

for i in range(1, node + 1):
    adjacent_map[i] = set([])

for i in range(0, vertex):
    x, y = map(int, input().split(' '))
    adjacent_map[x].add(y)
    adjacent_map[y].add(x)

dfs(adjacent_map, dfs_visited, start)
print()
bfs(adjacent_map, bfs_visited, start)


