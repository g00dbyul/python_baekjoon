'''
    add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
    remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
    check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
    toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
    all: S를 {1, 2, ..., 20} 으로 바꾼다.
    empty: S를 공집합으로 바꾼다.

https://www.acmicpc.net/problem/11723
'''

'''
26
add 1
add 2
check 1
check 2
check 3
remove 2
check 1
check 2
toggle 3
check 1
check 2
check 3
check 4
all
check 10
check 20
toggle 10
remove 20
check 10
check 20
empty
check 1
toggle 1
check 1
toggle 1
check 1
'''

import sys
input = sys.stdin.readline

arr = [0 for i in range(0,21)]

N = int(input())

for _ in range(N):
    calc = input().replace('\n', '')
    if 'add' in calc:
        num = int(calc.split()[1])
        if arr[num] == 0:
            arr[num] = 1
    elif 'remove' in calc:
        num = int(calc.split()[1])
        if arr[num] == 1:
            arr[num] = 0
    elif 'check' in calc:
        num = int(calc.split()[1])
        if arr[num] == 1:
            print(1)
        else:
            print(0)
    elif 'toggle' in calc:
        num = int(calc.split()[1])
        if arr[num] == 0:
            arr[num] = 1
        elif arr[num] == 1:
            arr[num] = 0
    elif 'all' in calc:
        arr = [1 for i in range(0,21)]
    elif 'empty' in calc:
        arr = [0 for i in range(0,21)]



