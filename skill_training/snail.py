T = int(input())

for _ in range(T):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    # 방향 우선 순위 : 우 -> 하 -> 좌 -> 상 우선 순위대로 좌표 배열
    direct = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0)
    ]

    # 방향 플래그 0 ~ 3까지만 -> 좌표 배열의 인덱스 그대로 접근
    d = 0
    # 좌표값 -> 좌표 배열에 따라 변경
    i, j = 0, 0
    # 좌표에 찍을 숫자 순차적으로 증가
    count = 1

    # 시작
    arr[i][j] = count
    count = count + 1

    while True:
        di, dj = direct[d]
        if 0 <= i + di < N and 0 <= j + dj < N:  # 범위 안에 포함되어야 함
            if arr[i + di][j + dj] == 0:
                arr[i + di][j + dj] = count
                i = i + di
                j = j + dj
                count = count + 1
            else:  # 진행 방향으로 못 움직임, 이미 숫자가 채워져 있는 상황이므로 방향 전환
                d = (d + 1) % 4
        else:  # 범위 밖 방향 전환
            d = (d + 1) % 4

        if count == N * N + 1:  # 좌표를 수정한 후 count 값을 변경 하기 때문에 마지막 값을 찍은 다음 빠져나와야 함
            break

    print('# '+str(N))
    for a in arr:
        print(*a)


