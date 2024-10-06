# 2차원 배열 내에서 n개의 원소 고르기

width = 7
height = 6

arr = [[0] * width for _ in range(height)]
count = 0
def combination_with_matrix(n, selected, matrix):
    global count
    if len(selected) == n:
        print(selected)
        count = count + 1
        return
    for i in range(height):
        for j in range(width):
            if (i,j) not in selected: # 선택한 좌표가 이미 포함되었는지 확인
                combination_with_matrix(n, selected + [(i,j)], matrix)


combination_with_matrix(3, [], arr)
print(count)