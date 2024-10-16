N = 5

arr = [[0] * N for _ in range(N)]
#우,하,좌,상
right = (0,1)
bottom = (1,0)
left = (0,-1)
top =  (-1,0)

out_to_in = [
    right, bottom, left, top
]

i,j = 0, 0
cnt = 1
d = 0

arr[i][j] = cnt
cnt = cnt + 1

while True:
    di, dj = out_to_in[d]
    if 0 <= i+di < N and 0 <= j+dj < N: # 범위 안
        if arr[i+di][j+dj] == 0:
            arr[i + di][j + dj] = cnt
            cnt = cnt + 1
            i, j = i + di, j + dj
        else: # 이미 번호가 채워진 경우
            d = (d + 1) % 4
    else: # 범위 밖 방향 회전
        d = (d+1) % 4
    if cnt == (N*N) + 1:
        break

for a in arr:
    print(a)

new_arr = [[0] * N for _ in range(N)]
cnt = 1
in_to_out = [
    right, bottom, left, top
]
current_dir = 0
step = 1
change = 2
ci,cj = N // 2, N // 2
new_arr[ci][cj] = cnt
cnt = cnt+1
# change = change - 1

while True:
    for _ in range(change):
        for _ in range(step):
            di, dj = in_to_out[current_dir]
            if 0 <= ci+di < N and 0 <= cj+dj < N and new_arr[ci+di][cj+dj] == 0:
                new_arr[ci+di][cj+dj] = cnt
                cnt = cnt + 1
                ci, cj = ci+di, cj+dj
        current_dir = (current_dir + 1) % 4
    step = step + 1
    change = 2
    if cnt == (N*N)+1:
        break


print('==============')

for a in new_arr:
    print(a)


