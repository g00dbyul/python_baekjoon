'''
5
4 1 5 2 3
5
1 3 7 9 5

https://www.acmicpc.net/problem/1920
'''

def find_target(arr, target):
    start, end = 0, len(arr)-1
    while end >= start:
        mid = (start+end) // 2
        if arr[mid] == target:
            return 1
        if target > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return 0


N = int(input())
arr = list(
    map(int, input().split())
)

M = int(input())
candidate = list(
    map(int, input().split())
)
arr.sort()

for c in candidate:
    print(find_target(arr, c))
