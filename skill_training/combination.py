arr = [1, 2, 3, 4]

# 순서, 중복 모두 허용 안됨
# 현재 인덱스 기준 다음 인덱스 던지기(이전 인덱스는 볼 필요 음슴)
def combination(n, new_arr, c):
    if len(new_arr) == n:
        print(new_arr)
        return
    for i in range(c, len(arr)):
        combination(n, new_arr + [arr[i]], i + 1)

combination(2, [], 0)