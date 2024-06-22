'''
백준 1697

출처 : https://www.acmicpc.net/problem/1697
'''

'''
5 17

수빈이가 5-10-9-18-17 순으로 가면 4초만에 동생을 찾을 수 있다.
'''

from collections import deque

n, k = map(int, input().split())
queue = deque([])
max = 100000
graph = [0] * (max+1)

queue.append(n)
while queue:
    pop = queue.popleft()
    if pop == k:
        break
    for v in [pop - 1, pop + 1, pop * 2]:
        if 0 <= v <= max and graph[v] == 0:
            queue.append(v)
            graph[v] = graph[pop] + 1

print(graph[k])


