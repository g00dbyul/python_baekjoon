'''
순열, 순서가 있음 1,2 != 2,1
visited를 안써도 되긴 함.
visited를 쓰는게 성능향상이 됨
'''

def permutation(candidate, n, arr):
    if len(candidate) == n:
        print(candidate)
        return
    for i in range(len(arr)):
        if arr[i] not in candidate:
            permutation(candidate+[arr[i]], n, arr)

def permutation_advance(candidate, n, arr, visited):
    if len(candidate) == n:
        print(candidate)
        return
    for i in range(len(arr)):
        if visited[i] == False:
            visited[i] = True
            permutation_advance(candidate + [arr[i]], n, arr, visited)
            visited[i] = False


permutation([], 2,  [1,2,3,4])
print('Advanced permutation')
permutation_advance([], 2,  [1,2,3,4], [False]*4)