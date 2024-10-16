# 순열 : 순서 존재, 중복 안됨

arr = [i for i in range(1,5)]
visited = [0] * len(arr)

# 뽑을 개수, 뽑은 원소를 담을 배열
# 백트래킹
def permutation(n, new_arr):
    global arr
    if len(new_arr) == n:
        print(new_arr)
        return
    for i in range(len(arr)):
        if not visited[i]:
            visited[i] = 1
            permutation(n, new_arr + [arr[i]])
            visited[i] = 0


# permutation(2, [])
permutation(2, [])