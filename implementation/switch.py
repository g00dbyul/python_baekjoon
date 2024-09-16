'''
8
0 1 0 1 0 0 0 1
2
1 3
2 3
'''

n = int(input())
arr = [0]

arr.extend(
list(
    map(int, input().split())
)
)

m = int(input())

for _ in range(m):
    gender, num = map(int, input().split())
    if gender == 1:
        for i in range(num, len(arr), num):
            arr[i] = int(not arr[i])
    elif gender == 2:
        start = num - 1
        end = num + 1
        while (start >= 1 and end < len(arr) and arr[start] == arr[end]):
            start = start - 1
            end = end + 1

        for i in range(start + 1, end):
            arr[i] = int(not arr[i])

for i in range(1, len(arr)):
    end = ' '
    if i % 20 == 0:
        end = '\n'
    print(arr[i], end=end)