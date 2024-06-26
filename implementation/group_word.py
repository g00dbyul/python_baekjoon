'''
백준 1316번 문제
출처 : https://www.acmicpc.net/problem/1316
'''

'''
3
happy
new
year

4
aba
abab
abcabc
a

5
ab
aa
aca
ba
bb

2
yzyzy
zyzyz
'''

def check_word(word):
    candidate = []
    previous = word[0]
    candidate.append(previous)
    for i in range(1, len(word)):
        if previous == word[i]:
            continue
        else:
            if word[i] in candidate:
                return False
            else:
                previous = word[i]
                candidate.append(previous)
    return True

N = int(input())

result = 0
for _ in range(N):
    word = input()
    if check_word(word):
        result = result + 1

print(result)



