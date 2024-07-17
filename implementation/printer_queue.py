'''
3
1 0
5
4 2
1 2 3 4
6 0
1 1 9 1 1 1
'''

from collections import deque

t = int(input())

for _ in range(t):
    size, index = map(int, input().split())
    priority = list(map(int, input().split()))
    queue = deque([])
    for i in range(size):
        queue.append(
            (i, priority[i])
        )

    count = 0
    while True:
        is_back = False
        temp = queue[0][1]
        for i in range(1, len(queue)):
            if temp < queue[i][1]:
                is_back = True
                break
        if is_back:
            pop = queue.popleft()
            queue.append(pop)
        else:
            pop = queue.popleft()
            count = count + 1
            if pop[0] == index:
                print(count)
                break



