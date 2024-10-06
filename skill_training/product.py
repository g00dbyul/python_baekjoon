arr = [i for i in range(1,5)]

#  순서, 중복 존재
# 중복이 허용 되므로 visited가 필요없음 -> 백트래킹 필요 음슴
def product(n, new_arr):
    global arr
    if len(new_arr) == n:
        print(new_arr)
        return
    for i in range(len(arr)):
        product(n, new_arr + [arr[i]])

product(3, [])

