def isValid(s: str) -> bool:
    stack = []
    for i in s:
        if i == "(" or i == "[" or i == "{":
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            else:
                pop = stack.pop()
                if pop == '(' and i != ')':
                    return False
                elif pop == '[' and i != ']':
                    return False
                elif pop == '{' and i != '}':
                    return False
    return not stack

def isValidByNossi(s: str) -> bool:
    stack = []
    for p in s:
        if p == "{":
            stack.append("}")
        elif p == "[":
            stack.append("]")
        elif p == "(":
            stack.append(")")
        elif stack and stack[-1] == p:
            stack.pop()
        else:
            return False
    return not stack


for case in ["()", "()[]{}", "(]", "([])"]:
    # print(isValid(case))
    print(isValidByNossi(case))

'''
JS에서 조건문으로 평가하는 거랑 비슷함
빈 배열이면 False로 평가, 무언가 있으면 True로 평가
'''
arr = []

if arr:
    print('A')
else:
    print('B')

arr.append(1)

if arr:
    print('A')
else:
    print('B')

print(not [])
print(not arr)