'''
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6
'''
import heapq
import sys
input = sys.stdin.readline

INF = 1000000000
v, e = map(int, input().split())
start_node = int(input())

graph = [[] for _ in range(v+1)]


for _ in range(e):
    start, end, dist = map(int, input().split())
    graph[start].append((dist, end))

def dijikstra(start_node, graph):
    distance = [INF] * (v + 1)
    queue = []

    heapq.heappush(queue, (0, start_node))
    distance[start_node] = 0

    while queue:
        dist, node = heapq.heappop(queue)
        if distance[node] < dist:
            continue
        for i in graph[node]:
            if distance[i[1]] > dist + i[0]:
                distance[i[1]] = dist + i[0]
                heapq.heappush(queue, (dist + i[0], i[1]))

    return distance[1:]

result = dijikstra(start_node, graph)

for r in result:
    if r == INF:
        print('INF')
    else:
        print(r)