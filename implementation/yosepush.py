'''
7 3

<3, 6, 2, 7, 5, 1, 4>

https://www.acmicpc.net/problem/1158
'''

from collections import deque

N, K = map(int, input().split())
arr = deque(
[i for i in range(1,N+1)]
)
result = []

while arr:
    for _ in range(K-1):
        pop = arr.popleft()
        arr.append(pop)
    result.append(arr.popleft())

print(
    str(result)
    .replace('[', '<')
    .replace(']', '>')
)





