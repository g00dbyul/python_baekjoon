'''
https://www.acmicpc.net/problem/10773

백준 10773번 문제
'''

'''
4
3
0
4
0

0
'''

import sys
input = sys.stdin.readline

K = int(input())
array = []

for i in range(K):
    line = int(input())
    if line != 0:
        array.append(line)
    else:
        if len(array) == 0:
            continue
        else:
            array.pop()

print(sum(array))