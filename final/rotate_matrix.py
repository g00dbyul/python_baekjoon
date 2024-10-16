N = 5

arr = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]


def rotate_90(arr):
    new_arr = [x[:] for x in arr]
    for i in range(N):
        for j in range(N):
            new_arr[i][j] = arr[N-1-j][i]
    return new_arr

def rotate_180(arr):
    new_arr = [x[:] for x in arr]
    for i in range(N):
        for j in range(N):
            new_arr[i][j] = arr[N-1-i][N-1-j]
    return new_arr

rarr = rotate_90(arr)
for a in rarr:
    print(a)

print('===========')

narr = rotate_180(arr)
for a in narr:
    print(a)