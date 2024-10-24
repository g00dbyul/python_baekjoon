'''
baekjoon online judge
noojkeab enilno egduj

<open>tag<close>
<open>gat<close>

<ab cd>ef gh<ij kl>
<ab cd>fe hg<ij kl>

https://www.acmicpc.net/problem/17413
'''

from collections import deque

word = input()
word_queue = deque([])
is_tag = False
result = ''

for w in word:
    if w == '<':
        if len(word_queue) > 0:
            if is_tag:
                while word_queue:
                    result = result + word_queue.popleft()
            else:
                while word_queue:
                    result = result + word_queue.pop()
        is_tag = True
        word_queue.append(w)
    elif w == '>':
        word_queue.append(w)
        while word_queue:
            result = result + word_queue.popleft()
        is_tag = False
    elif w == ' ':
        if is_tag:
            word_queue.append(w)
        else:
            while word_queue:
                result = result + word_queue.pop()
            result = result + ' '
    else:
        word_queue.append(w)

if len(word_queue) > 0:
    if is_tag:
        while word_queue:
            result = result + word_queue.popleft()
    else:
        while word_queue:
            result = result + word_queue.pop()


print(result)







