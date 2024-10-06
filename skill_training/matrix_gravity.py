arr = [[0, 1, 0], [1, 0, 1], [0, 1, 0], [0, 0, 1], [0, 1, 0]]

for a in arr:
    print(a)

def gravity():
    n = len(arr)
    m = len(arr[0])
    for i in range(n - 1): # 배열 높이
        for j in range(m):
            p = i
            # 현재칸이 아래로 내려갈 수 있다면 그 윗줄도 한 칸 씩 연쇄적으로 내려와야함, > 위 1, 아래 0 일때 교환
            # 아래로 갈 수록 비교 횟수가 많아짐.
            while 0 <= p and arr[p][j] == 1 and arr[p + 1][j] == 0:
                arr[p][j], arr[p + 1][j] = arr[p + 1][j], arr[p][j]
                p -= 1


'''
0 -
1 - -
2 - - -
3 - - - -

대략 이런 느낌...
위 아래를 조건에 맞으면 스왑하고, 그 과정을 행의 최상단(인덱스 0)을 찍을때까지 해야 함
'''

gravity()

# print('After')
# for a in arr:
#     print(a)

