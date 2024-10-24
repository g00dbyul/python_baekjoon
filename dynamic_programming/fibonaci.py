'''
3
0
1
3

https://www.acmicpc.net/problem/1003
'''


def fibo(n):
    if n == 0:
        return (1,0)
    elif n == 1:
        return (0,1)
    arr = [(0,0)] * (n+1)
    arr[0] = (1,0)
    arr[1] = (0,1)
    for i in range(2,n+1):
        arr[i] = (arr[i-1][0] + arr[i-2][0], arr[i-1][1] + arr[i-2][1])
    return arr[n]

T = int(input())
for _ in range(T):
    a, b = fibo(int(input()))
    print(a, b)



