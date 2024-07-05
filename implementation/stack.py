'''
https://www.acmicpc.net/problem/10828

백준 10828 문제
'''

'''
push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

14
push 1
push 2
top
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
top
'''

import sys
input = sys.stdin.readline

N = int(input())
stack = []
result = []
for _ in range(N):
    command = input().replace('\n', '')
    # print(command)
    if 'push' in command:
        stack.append(
            command.split(' ')[1]
        )
    elif 'pop' in command:
        if len(stack) == 0:
            print(-1)
        else:
            pop = stack.pop()
            print(pop)
    elif 'size' in command:
        print(len(stack))
    elif 'empty' in command:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif 'top' in command:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
