'''
3
2 2
1 5
13 29

https://www.acmicpc.net/problem/1010
'''

T = int(input())

for _ in range(T):
    n,m = map(int, input().split())
    if n == m:
        print(1)
    elif n == 1:
        print(n * m)
    else:
        acc = 1
        son = 1
        for i in range(n):
            acc = acc * m
            m = m - 1
            son = son * (i+1)
        print(acc // son)


