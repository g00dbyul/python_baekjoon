'''
https://www.acmicpc.net/problem/2839

5가 가장 큼, 5에서 떨어지는 경우를 먼저 체크 -> 3을 하나씩 빼면서 체크 -> 3을 뺐더니 음수가 된다면 3,5조합으로 만들 수 없음
'''

N = int(input())

result = 0

while N >= 0:
    if N % 5 == 0:
        result = result + (N // 5)
        print(result)
        break
    N = N - 3
    result = result + 1
    if N < 0:
        print(-1)
        break

