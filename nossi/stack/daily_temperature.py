from collections import deque

def dailyTemperatures(temperatures: [int]) -> [int]:
    stack = []
    answer = [0] * len(temperatures)
    for index, value in enumerate(temperatures):
        if len(stack) == 0:
            stack.append((index, value))
        else:
            if stack[-1][1] < value:
                while stack and stack[-1][1] < value:
                    i,v = stack.pop()
                    answer[i] = index - i
            stack.append((index, value))
    return answer

cases = [
[73,74,75,71,69,72,76,73],
[30,40,50,60],
[30,60,90]
]

for case in cases:
    print(dailyTemperatures(case))