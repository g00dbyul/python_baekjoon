'''
백준 2606번 문제
참조 : https://www.acmicpc.net/problem/2606
'''

'''
7
6
1 2
2 3
1 5
5 2
5 6
4 7
'''

from collections import deque

node = int(input())
vertex = int(input())

visited = [False]
network = {}

for i in range(node):
    network[i+1] = set([])
    visited.append(False)

# print(network)

for i in range(vertex):
    x, y = map(int, input().split(' '))
    network[x].add(y)
    network[y].add(x)

queue = deque([])

queue.append(1)
visited[1] = True

result = 0

while queue:
    pop = queue.popleft()
    result = result + 1
    for i in network[pop]:
        if visited[i] == False:
            queue.append(i)
            visited[i] = True

print(result - 1)
