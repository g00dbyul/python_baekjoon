arr = [1, 2, 3, 4]

# 조합 : 중복 없이 순서를 고려하지 않음
# 현재 인덱스 기준 다음 인덱스 던지기(이전 인덱스는 볼 필요 음슴)
# 순서를 고려하지 않음 (1,2) == (2,1) -> 한번 본 원소는 다시 볼일 음슴
def combination(n, new_arr, c):
    if len(new_arr) == n:
        print(new_arr)
        return
    for i in range(c, len(arr)):
        combination(n, new_arr + [arr[i]], i + 1)

combination(2, [], 0)