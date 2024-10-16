'''
i1, j1, h1, w1 = 1, 1, 2, 2
i2, j2, h2, w2 = 2, 2, 2, 2
'''

def is_overlap(a,b):
    i1, j1, h1, w1 = a
    i2, j2, h2, w2 = b
    # 사각형이 겹치지 않는 조건을 확인
    if i1 + h1 <= i2 or i2 + h2 <= i1:  # 위아래로 겹치지 않는 경우
        return False
    if j1 + w1 <= j2 or j2 + w2 <= j1:  # 좌우로 겹치지 않는 경우
        return False
    # 위의 조건이 모두 성립하지 않으면 겹친다
    return True

print(
is_overlap((1, 1, 2, 2), (2, 2, 2, 2))
)

[
    [0,0,0,0],
    [0,1,2,0],
    [0,1,2,0],
    [0,1,2,0]
]

