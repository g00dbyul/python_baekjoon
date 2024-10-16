# 배열 내에서 숫자 1이 있는 영역을 상하좌우로 움직이는 함수
def move_area(grid, direction):
    # grid의 크기
    n, m = len(grid), len(grid[0])

    # 숫자 1의 좌표를 모두 찾기
    ones = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                ones.append((i, j))

    # 이동 방향 설정 (상, 하, 좌, 우)
    # direction == 'up'이면 (i-1, j)
    # direction == 'down'이면 (i+1, j)
    # direction == 'left'이면 (i, j-1)
    # direction == 'right'이면 (i, j+1)
    di, dj = 0, 0
    if direction == 'up':
        di, dj = -1, 0
    elif direction == 'down':
        di, dj = 1, 0
    elif direction == 'left':
        di, dj = 0, -1
    elif direction == 'right':
        di, dj = 0, 1

    # 먼저, 숫자 1의 영역을 0으로 만듦
    for i, j in ones:
        grid[i][j] = 0

    # 이동하면서 다른 숫자가 있으면 밀어냄
    new_ones = []
    for i, j in ones:
        ni, nj = i + di, j + dj

        # 배열의 범위 내에 있어야 함
        if 0 <= ni < n and 0 <= nj < m:
            # 이동할 위치가 0인 경우는 그냥 이동
            if grid[ni][nj] == 0:
                new_ones.append((ni, nj))
            else:
                # 다른 숫자가 있는 경우 그 숫자를 같은 방향으로 밀기
                new_val = grid[ni][nj]
                move_number(grid, ni, nj, di, dj)
                new_ones.append((ni, nj))

    # 숫자 1을 새 위치에 업데이트
    for i, j in new_ones:
        grid[i][j] = 1

    return grid


# 숫자를 밀어내는 함수 (재귀적으로 이동)
def move_number(grid, i, j, di, dj):
    n, m = len(grid), len(grid[0])
    ni, nj = i + di, j + dj

    # 배열의 범위 내에 있어야 함
    if 0 <= ni < n and 0 <= nj < m:
        # 만약 이동할 위치가 비어있으면 밀어낸다
        if grid[ni][nj] == 0:
            grid[ni][nj] = grid[i][j]
            grid[i][j] = 0
        else:
            # 만약 다른 숫자가 있으면 재귀적으로 밀어낸다
            move_number(grid, ni, nj, di, dj)
            grid[ni][nj] = grid[i][j]
            grid[i][j] = 0


grid = [
    [0, 0, 0, 0],
    [0, 1, 2, 0],
    [0, 1, 2, 0],
    [0, 0, 0, 0]
]

# 숫자 1을 오른쪽으로 이동
new_grid = move_area(grid, 'down')

for row in new_grid:
    print(row)