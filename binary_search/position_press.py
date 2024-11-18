'''
5
2 4 -10 4 -9
'''

import sys
input = sys.stdin.readline

N = int(input())
arr = list(
    map(int, input().split())
)

def binary_search_index(number, arr):
    start, end = 0, len(arr)-1
    while start <= end:
        mid = (start+end) // 2
        if arr[mid] == number:
            return mid
        if arr[mid] < number:
            start = mid + 1
        else:
            end = mid - 1
    return -1

sorted_arr = list(sorted(set(arr)))

for i in arr:
    print(binary_search_index(i, sorted_arr), end=' ')



