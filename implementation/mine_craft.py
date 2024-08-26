'''
3 4 99
0 0 0 0
0 0 0 0
0 0 0 1

2 0

3 4 1
64 64 64 64
64 64 64 64
64 64 64 63

1 64


1.좌표 (i, j)의 가장 위에 있는 블록을 제거하여 인벤토리에 넣는다.
2.인벤토리에서 블록 하나를 꺼내어 좌표 (i, j)의 가장 위에 있는 블록 위에 놓는다.
1번 작업은 2초가 걸리며, 2번 작업은 1초가 걸린다.
'''

import sys
input = sys.stdin.readline

# 모든 땅의 높이를 h로 만드는데 걸리는 시간을 구하는 함수
def get_time(h):
    add_num = 0  # 삽입할 블록의 개수
    erase_num = 0  # 제거할 블록의 개수

    # 0부터 256까지 각 높이
    for i in range(257):
        # 현재 높이의 개수, 현재높이 - 목표(h) => 차이
        n, tmp = nums[i], i - h
        # 개수가 0이라면 넘어감
        if n == 0: continue

        # 높이의 차가 음수일 경우 삽입할 블록의 개수 구해줌(h가 크기 때문에 블록 삽입)
        if tmp < 0:
            add_num += (-tmp) * n
            # 높이의 차가 양수일 경우 제거할 블록의 개수 구해줌(h보다 작기 때문에 블록을 지워야 함)
        else:
            erase_num += tmp * n

    # 만약 인벤토리에서 사용할 수 있는 블록이 있을 경우(블록을 추가하는데에는 제약이 있음 인벤토리 갯수, 이전에 블록을 지운 갯수)
    if (erase_num + b) - add_num >= 0:
        # 시간을 구해줌
        time = erase_num * 2 + add_num
        return time
        # 사용할 수 있는 블록이 없을 경우
    else:
        return 1e9 + 1


# 입력 받기
n, m, b = map(int, input().split())

# 땅 높이에 해당하는 칸의 개수
nums = [0] * 257
for i in range(n):
    for j in list(map(int, input().split())):
        nums[j] += 1

    # 최소 시간과 그 때의 높이를 저장할 변수
answer = 1e9
height = 0

# 0부터 256까지 모든 땅을 같은 높이로 만들기
for h in range(257):
    # 시간을 계산
    time = get_time(h)
    # 최소값과 그 때의 땅 높이를 구해줌
    if time <= answer:
        answer = time
        height = h

print(answer, height)