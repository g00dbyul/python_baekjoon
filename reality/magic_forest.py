'''
6 5 6
2 3
2 0
4 2
2 0
2 0
2 2

29
'''
#
# R, C, K = map(int, input().split())
#
# forest = [[0] * C for _ in range(R)]
#
# for _ in range(K):
#     start, exit = map(int, input().split())

# 기본 설정 및 입력 파싱
R, C, K = map(int, input().split())

goelems = []
for _ in range(K):
    c, d = map(int, input().split())
    goelems.append((c, d))

# 숲의 상태를 나타내는 배열 초기화
forest = [[False] * C for _ in range(R)]

# 방향 설정 (0: 북, 1: 동, 2: 남, 3: 서)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def is_valid(x, y):
    return 0 <= x < R and 0 <= y < C

# 골렘이 이동할 수 있는 최대 위치까지 이동 후, 정령이 최종적으로 도달한 행 번호를 반환하는 함수
def move_golem(c, d):
    # 초기 골렘 위치 (c가 중앙 열)
    x, y = 0, c - 1
    while True:
        # 남쪽으로 한 칸 내려갈 수 있는지 확인
        if x + 1 < R and not forest[x + 1][y]:
            x += 1
            forest[x][y] = True
        else:
            # 서쪽으로 회전할 수 있는지 확인
            if y - 1 >= 0 and not forest[x + 1][y - 1]:
                y -= 1
                x += 1
                forest[x][y] = True
                d = (d + 3) % 4  # 서쪽으로 회전하면 반시계 방향으로 출구 이동
            # 동쪽으로 회전할 수 있는지 확인
            elif y + 1 < C and not forest[x + 1][y + 1]:
                y += 1
                x += 1
                forest[x][y] = True
                d = (d + 1) % 4  # 동쪽으로 회전하면 시계 방향으로 출구 이동
            else:
                break  # 더 이상 이동할 수 없으면 종료
    return x + 1  # 정령이 도달한 최종 행 번호 (1-based)

# 최종 위치 합계
final_sum = 0

# 각 골렘에 대해 이동 시뮬레이션
for c, d in goelems:
    result = move_golem(c, d)
    final_sum += result

# 결과 출력
print(final_sum)