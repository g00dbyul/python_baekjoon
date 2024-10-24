'''
6
10
20
15
25
10
20
'''

n = int(input())
arr = [0]
dp_arr = [0] * (n+1)
for _ in range(n):
    arr.append(
        int(input())
    )

if n < 2:
    print(sum(arr))
else:
    dp_arr[1] = arr[1]
    dp_arr[2] = arr[1] + arr[2]
    for i in range(3, n+1):
        dp_arr[i] = max(arr[i] + arr[i - 1] + dp_arr[i - 3], arr[i] + dp_arr[i - 2])
    print(dp_arr[n])


