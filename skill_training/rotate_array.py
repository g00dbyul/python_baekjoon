#시계방향 회전
def rotate_90(arr):
    height = len(arr)
    width = len(arr[0])
    rotated = [[0] * height for _ in range(width)]

    for i in range(height):
        for j in range(width):
            # 회전 되는 배열의 행은 기존 배열의 열이다.
            # 회전 되는 배열의 열은 (기존 배열 높이 -1 -기존배열 행 인덱스) 이다.
            rotated[j][height-1-i] = arr[i][j]
    return rotated

def rotate_180(arr):
    height = len(arr)
    width = len(arr[0])
    rotated = [[0] * width for _ in range(height)]

    for i in range(height):
        for j in range(width):
            rotated[height-1-i][width-1-j] = arr[i][j]
    return rotated

# 시계방향 270도, 반시계방향 90도
def rotate_270(arr):
    height = len(arr)
    width = len(arr[0])
    rotated = [[0] * height for _ in range(width)]

    for i in range(height):
        for j in range(width):
            rotated[width-1-j][i] = arr[i][j]
    return rotated


arr_1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

arr_2 = [
    [1,2,3],
    [4,5,6]
]

print(arr_1)
print(arr_2)

print(rotate_90(arr_1))
print(rotate_90(arr_2))

print(rotate_180(arr_1))
print(rotate_180(arr_2))

print(rotate_270(arr_1))
print(rotate_270(arr_2))

arr_3 = [[7 * j + i for i in range(1, 8)] for j in range(7)]
