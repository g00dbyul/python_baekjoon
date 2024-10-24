'''
7 3

https://www.acmicpc.net/problem/2960
'''

N, K = map(int, input().split())

eratos_arr = [True] * (N+1)

result = []

for i in range(2, len(eratos_arr)):
    if eratos_arr[i] == True:
        eratos_arr[i] = False
        result.append(i)
        for j in range(2*i, len(eratos_arr), i):
            if eratos_arr[j] == True:
                eratos_arr[j] = False
                result.append(j)


print(result[K-1])
