'''
https://www.acmicpc.net/problem/1916
'''

'''
5
8
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
1 5
'''
import heapq
INF = 1e9

def dijikstra(graph, start_node, end_node):
    queue = []
    # 거리배열 초기화, 최대값으로 초기화하고 최소값으로 갱신 해줘야 함
    distance = [INF] * (len(graph) + 1)

    # 우선순위 큐 초기화(맨 처음에는 시작 노드를 넣어야 함)
    heapq.heappush(queue, (0, start_node))
    # 시작 노드의 거리는 0으로
    distance[start_node] = 0

    while queue:
        # 현재 방문한 노드와 거리
        dist, node = heapq.heappop(queue)
        if distance[node] < dist:
            # 이미 노드까지의 거리가 더 짧은 경우 더 확인할 필요 없이 패스
            continue
        # 인접한 노드들 정보 가져오기
        for gd, gn in graph[node]:
            # 현재 인접한 노드까지의 거리 > 지금까지의 거리 + 지금 노드에서 인접한 노드까지 거리 => 최단거리 갱신해야 함(우선순위 큐 추가)
            if distance[gn] > dist + gd:
                distance[gn] = dist + gd
                heapq.heappush(queue, (dist + gd, gn))
    return distance[end_node]

city = int(input())
routes = int(input())

graph = [[] for _ in range(city+1)]

for _ in range(routes):
    start, end, cost = map(int, input().split())
    graph[start].append((cost, end))

start_node, end_node = map(int, input().split())
print(dijikstra(graph, start_node, end_node))
