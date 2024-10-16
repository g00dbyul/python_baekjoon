from collections import deque


# 큐를 사용해 숫자 1, 2, 3으로 이루어진 그룹을 찾고 밀어내는 함수
def move_group_with_queue(grid, direction):
    # grid의 크기
    n, m = len(grid), len(grid[0])

    # 이동 방향 설정 (상, 하, 좌, 우)
    di, dj = 0, 0
    if direction == 'right':
        di, dj = 0, 1
    elif direction == 'left':
        di, dj = 0, -1
    elif direction == 'up':
        di, dj = -1, 0
    elif direction == 'down':
        di, dj = 1, 0

    # 숫자 1의 좌표를 모두 찾기
    group = []
    visited = [[False] * m for _ in range(n)]
    queue = deque()

    # 숫자 1을 찾고 큐에 추가
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                queue.append((i, j))
                visited[i][j] = True
                group.append((i, j))

    # BFS 방식으로 그룹 찾기 (큐 사용)
    while queue:
        i, j = queue.popleft()

        # 상하좌우로 탐색하여 연결된 숫자 2와 3을 찾음
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj] and grid[ni][nj] in [1, 2, 3]:
                visited[ni][nj] = True
                queue.append((ni, nj))
                group.append((ni, nj))

    # 그룹의 숫자를 일시적으로 0으로 설정
    group_values = {}
    for i, j in group:
        group_values[(i, j)] = grid[i][j]  # 현재 위치의 값을 저장
        grid[i][j] = 0  # 그룹 영역을 0으로 설정

    # 이동 가능 여부 확인 (벽이나 경계를 넘지 않는지 체크)
    can_move = True
    for i, j in group:
        ni, nj = i + di, j + dj
        if not (0 <= ni < n and 0 <= nj < m and grid[ni][nj] == 0):
            can_move = False
            break

    # 이동이 가능하다면 그룹을 이동
    if can_move:
        for i, j in group:
            ni, nj = i + di, j + dj
            grid[ni][nj] = group_values[(i, j)]  # 저장된 값을 새로운 위치에 할당

    return grid


# 테스트 배열 (벽(-1) 포함, 숫자 1, 2, 3은 밀어내야 함)
grid_with_walls_queue = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 2, 3, 0, 0],
    [0, 1, 2, 3, 0, -1],
    [0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

# 숫자 1, 2, 3을 오른쪽으로 밀기 (큐 사용)
new_grid_with_walls_queue = move_group_with_queue(grid_with_walls_queue, 'right')

for a in new_grid_with_walls_queue:
    print(a)