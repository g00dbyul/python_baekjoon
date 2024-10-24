'''
5
1
3
8
-2
2

2
2
1
10

https://www.acmicpc.net/problem/2108
'''
import sys
input = sys.stdin.readline

size = int(input())
arr = []
frequency = dict()
for _ in range(size):
    num = int(input())
    arr.append(
        num
    )

    if num in frequency.keys():
        frequency[num] = frequency[num] + 1
    else:
        frequency[num] = 1
def average(arr):
    return round(sum(arr) / size)

def center_value(arr):
    return arr[size // 2]

def max_density_value(frequency):
    maximum = max(frequency.values())
    numbers = []
    for key in frequency.keys():
        if frequency[key] == maximum:
            numbers.append(key)
    numbers.sort()
    if len(numbers) == 1:
        return numbers[0]
    return numbers[1]



def coverage(arr):
    return arr[-1] - arr[0]

arr.sort()
print(average(arr))
print(center_value(arr))
print(max_density_value(frequency))
print(coverage(arr))