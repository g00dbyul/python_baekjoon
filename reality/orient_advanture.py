'''
탐사 진행(K)
1. 최대 카운트 찾기
- 회전 횟수(90,180,270)
- 중심축 (열, 행)
- 회전-> 카운트 -> 비교 및 갱신

연쇄 획득(무한 루프)
- 카운트 없으면 끝

2 20
7 6 7 6 7
6 7 6 7 6
6 7 1 5 4
7 6 3 2 1
5 4 3 2 7
3 2 3 5 2 4 6 1 3 2 5 6 2 1 5 6 7 1 2 3
'''

'''
3 30
2 5 3 6 5
4 2 7 6 5
7 3 6 1 1
1 4 3 6 4
1 5 4 6 4
1 1 5 3 6 1 2 2 7 4 1 1 5 2 6 5 7 2 3 7 7 3 6 3 2 3 5 4 7 3

7 13 19
'''

'''
GG ㅠㅠ
'''

from collections import deque

K, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(5)]
lst = list(map(int, input().split()))

def rotate(arr, pi, pj): # 회전축은 좌측 상단
    rotated = [x[:] for x in arr]
    for i in range(3):
        for j in range(3):
            rotated[pi+i][pj+j] = arr[pi+3-j-1][pj+i]
    return rotated

def bfs(arr):
    queue = deque([])
    visited = [[0] * 5 for _ in range(5)]
    didj = [(-1,0), (1,0), (0,-1), (0,1)]
    temp = []
    total_set = []

    for i in range(5):
        for j in range(5):
            if visited[i][j] == False:
                queue.append((i,j))
                visited[i][j] = True
                temp.append((i,j))
                while queue:
                    pop_i, pop_j = queue.popleft()
                    for di, dj in didj:
                        next_i = pop_i+di
                        next_j = pop_j+dj
                        if 0 <= next_i < 5 and 0 <= next_j < 5 and visited[next_i][next_j] == False and (arr[pop_i][pop_j] == arr[next_i][next_j]):
                            queue.append((next_i, next_j))
                            visited[next_i][next_j] = True
                            temp.append((next_i, next_j))
                if len(temp) >= 3:
                    total_set = total_set + temp
                temp = []
    return total_set

arr = [
    [2,3,2,6,2],
    [4,6,7,3,1],
    [7,1,1,3,1],
    [1,4,3,5,4],
    [1,5,4,1,4]
]


result = []
for k in range(K): # 발굴 횟수
    # 유물 개수 카운트
    max_count = []
    max_arr = []
    answer = 0
    # 우선순위가 주어지면 우선순위 대로 반복문을 만들면 됨
    for rot in range(1, 4):  # 회전
        for pj in range(3):  # 열
            for pi in range(3):  # 행
                rotated = [x[:] for x in arr]
                for _ in range(rot): # rot 만큼 회전(90, 180, 270)
                    rotated = rotate(arr, pi, pj)
                    piece_points = bfs(rotated)
                    if len(piece_points) > len(max_count):
                        max_count = piece_points
                        max_arr = rotated
    # 발굴하기
    if len(max_count) > 0:
        arr = max_arr
        for pi, pj in max_count: # 탐색으로 나온 지점을 0으로 변경
            arr[pi][pj] = 0
        for j in range(5):
            for i in range(4, -1, -1):
                if arr[i][j] == 0:
                    arr[i][j] = lst.pop(0) # 조각 갈아끼우기
                    answer = answer + 1  # 횟수만큼 추가
        # 후속 발굴
        while True:
            piece_points = bfs(arr)
            if len(piece_points) == 0: # 후속 탐색 종료
                break
            else:
                for pi, pj in piece_points:  # 탐색으로 나온 지점을 0으로 변경
                    arr[pi][pj] = 0
                for j in range(5):
                    for i in range(4, -1, -1):
                        if arr[i][j] == 0:
                            arr[i][j] = lst.pop(0)  # 조각 갈아끼우기
                            answer = answer + 1  # 횟수만큼 추가
    # 발굴할 수 없으므로 종료
    else:
        break
    result.append(answer)

print(*result)


