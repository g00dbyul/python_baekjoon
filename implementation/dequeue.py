'''
15
push_back 1
push_front 2
front
back
size
empty
pop_front
pop_back
pop_front
size
empty
pop_back
push_front 3
empty
front
'''

'''
    push_front X: 정수 X를 덱의 앞에 넣는다.
    push_back X: 정수 X를 덱의 뒤에 넣는다.
    pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    size: 덱에 들어있는 정수의 개수를 출력한다.
    empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
    front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
queue = deque([])

for _ in range(N):
    command = input().replace('\n', '')
    if 'push_front' in command:
        data = command.split(' ')
        queue.appendleft(
            int(data[1])
        )
    elif 'push_back' in command:
        data = command.split(' ')
        queue.append(
            int(data[1])
        )
    elif 'pop_front' in command:
        if len(queue) == 0:
            print(-1)
        else:
            pop = queue.popleft()
            print(pop)
    elif 'pop_back' in command:
        if len(queue) == 0:
            print(-1)
        else:
            pop = queue.pop()
            print(pop)
    elif 'size' in command:
        print(len(queue))
    elif 'empty' in command:
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif 'front' in command:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif 'back' in command:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])



