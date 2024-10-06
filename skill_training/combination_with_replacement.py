arr = [1, 2, 3, 4]

# 순서X, 중복 허용
def combination_with_replacement(n, new_arr, c):
    if len(new_arr) == n:
        print(new_arr)
        return
    for i in range(c,len(arr)):
        combination_with_replacement(n, new_arr + [arr[i]], i)

combination_with_replacement(2, [], 0)