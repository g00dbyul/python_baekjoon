def partial_sum(arr, number):
    end, count, current_sum = 0, 0, 0
    for start in range(len(arr)):
        while current_sum < number and end < len(arr):
            current_sum = current_sum + arr[end]
            end = end + 1
        if current_sum == number:
            count = count + 1
        current_sum = current_sum - arr[start]
    return count

'''
예시가 굉장히 뭐 같은데... 내가 만들 수 없다 ㅠ
start는 0부터 시작 한다는 전재, end를 부분합이 number보다 커질때까지 늘린다.
부분합이 num랑 같은지 비교
start를 늘린다. 
'''


arr = [1, 2, 3, 2, 5]
print(
    partial_sum(arr,5)
)