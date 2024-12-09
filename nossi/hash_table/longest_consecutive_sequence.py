cases = [
[100,4,200,1,3,2],
[0,3,7,2,5,8,4,6,0,1]
]

def longestConsecutive(nums: [int]) -> int:
    dictionary = {}
    for num in nums:
        dictionary[num] = False
    result = 0
    for num in nums:
        cnt = 0
        if num-1 not in dictionary:
            target = num
            while target in dictionary:
                cnt = cnt + 1
                target = target + 1
        result = max(result, cnt)
    return result

for case in cases:
    print(longestConsecutive(case))
