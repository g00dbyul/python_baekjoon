'''
3
4
7
10

https://www.acmicpc.net/problem/9095
'''

def solution(n):
    if n < 4:
        if n == 3:
            return 4
        else:
            return n
    arr = [0] * (n+1)
    arr[1] = 1
    arr[2] = 2
    arr[3] = 4
    for i in range(4,n+1):
        arr[i] = arr[i-1] + arr[i-2] + arr[i-3]
    return arr[n]

T = int(input())

for _ in range(T):
    print(solution(int(input())))

