'''
백준 4673번 문제
출처 : https://www.acmicpc.net/problem/4673

문제 설명이 참 거시기 함...;;

결론은 1 ~ 10000 까지의 수를 모두 self-number로 구하고
없는 숫자들이 생성자가 된다;;
'''

def d(n):
    string_number = str(n)
    result = 0
    for i in string_number:
        result = result + int(i)
    return result + n

candidate = set([])

for i in range(1, 10001):
    candidate.add(d(i))

for j in range(1, 10001):
    if j not in candidate:
        print(j)