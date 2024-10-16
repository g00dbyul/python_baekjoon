'''
조합 : 중북 안됨, 순서 없음 => (1,2) == (2,1)
'''

arr = [1,2,3,4]
def combination(candidate, n, start, arr):
    if len(candidate) == n:
        print(candidate)
        return
    for i in range(start, len(arr)):
        combination(candidate + [arr[i]], n, i+1, arr)


combination([], 2, 0, [1,2,3,4])


