from collections import deque
N = 5
arr = [
    [1,0,0,1,0],
    [0,1,1,1,0],
    [0,0,0,1,0],
    [1,0,0,0,1],
    [0,0,1,0,0]
]

direction = [
    (-1,0),(1,0),(0,-1),(0,1)
]

def push_matrix(arr, d):
    new_arr = [x[:] for x in arr]
    di, dj = direction[d]
    queue = []

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                queue.append((i,j))

    if d == 0: # 상
        queue.sort(key=lambda x:x[0])
    elif d == 1: # 하
        queue.sort(key=lambda x: x[0], reverse=True)
    elif d == 2: # 좌
        queue.sort(key=lambda x: x[1])
    else: # 우
        queue.sort(key=lambda x: x[1], reverse=True)
    queue = deque(queue)

    while queue:
        pi, pj = queue.popleft()
        if 0 <= pi+di < N and 0 <= pj+dj < N:
            if new_arr[pi+di][pj+dj] == 0:
                queue.append((pi + di, pj + dj))
                new_arr[pi+di][pj+dj] = new_arr[pi][pj]
                new_arr[pi][pj] = 0
    return new_arr

for a in arr:
    print(a)

print('========')
nar = push_matrix(arr, 3)

for a in nar:
    print(a)

