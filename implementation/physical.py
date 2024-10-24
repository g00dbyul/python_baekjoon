'''
5
55 185
58 183
88 186
60 175
46 155


https://www.acmicpc.net/problem/7568
'''

N = int(input())
arr = []
result = []

for i in range(N):
    arr.append(
        tuple(
            map(int, input().split())
        )
    )

for i in range(N): # 비교
    rank = 1
    for j in range(N): # 상대 -> 상대가 모든 것이 크면 rank + 1, 가장 크다면 1로 끝나겠지, 가장 작다면 매번 추가 되겠지.
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            rank = rank + 1
    print(rank, end=' ')


