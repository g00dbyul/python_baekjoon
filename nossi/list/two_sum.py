'''
https://leetcode.com/problems/two-sum/description/
'''

def two_sum_brute_force(nums: list[int], target: int) -> list[int]:
    result = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                result = [i, j]
                break
    return result


def two_sum_hash_map(nums: list[int], target: int) -> list[int]:
    hash_map = {}
    for i, v in enumerate(nums):
        if target - v in hash_map:
            return [hash_map[target - v], i]
        hash_map[v] = i
    return []


'''
hash_map key : 배열의 값
hash_map value : 배열의 키

hash table 에서는 탐색 속도가 O(1)
target - value = 값이 hash table에 있다면 정답!
일단 없다면 hash table에 추가
'''

input_data = [
    ([2, 7, 11, 15], 9),
    ([3, 2, 4], 6),
    ([3, 3], 6)
]

for nums, target in input_data:
    print(
        two_sum_hash_map(nums, target)
    )

