arr = [1,3,5,7,9,11,13,15]

# 배열이 정렬 되어 있음이 보장
# 찾고자하는 배열의 인덱스 리턴, 업으면 -1
def binary_search(arr, target):
    start, end = 0, len(arr)-1

    while end >= start:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target: # 찾고자 하는 값이 mid보다 클 경우, start를 mid로 대체
            start = mid+1
        else: # 찾고자 하는 값이 mid보다 작으므로 end를 mid로 대체
            end = mid-1
    return -1

print(binary_search(arr, 1))
print(binary_search(arr, 2))
print(binary_search(arr, 5))

