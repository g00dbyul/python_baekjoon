N = 5

arr = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

def partial_rotate_90(si,sj,size, arr):
    new_arr = [x[:] for x in arr]
    temp = [[0]* size for _ in range(size)]

    for i in range(si,size+si):
        for j in range(sj, size+sj):
            temp[i-si][j-sj] = arr[i][j]

    rot = [x[:] for x in temp]
    for i in range(size):
        for j in range(size):
            rot[i][j] = temp[size-j-1][i]

    for i in range(si,size+si):
        for j in range(sj, size+sj):
            new_arr[i][j] = rot[i-si][j-sj]
    return new_arr

rot = partial_rotate_90(1,1,3, arr)
for a in rot:
    print(a)

