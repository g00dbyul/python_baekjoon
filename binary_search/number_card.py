'''
5
6 3 2 10 -10
8
10 9 -5 2 3 4 5 -10


https://www.acmicpc.net/problem/10815
'''
import sys
input = sys.stdin.readline

def find_target(arr, target):
    start, end = 0, len(arr)-1
    while end >= start:
        mid = (start+end) // 2
        if arr[mid] == target:
            return 1
        if arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0

N = int(input())
cards = sorted(
    list(
        map(int, input().split())
    )
)

M = int(input())
candidate = list(
        map(int, input().split())
    )

for c in candidate:
    print(find_target(cards, c), end=' ')
