'''
9999

2

122

2

12635

1

888888

https://www.acmicpc.net/problem/1475
'''


number = input()
candidate = [0 for _ in range(10)]

for n in number:
    to_int = int(n)
    if to_int == 6 or to_int == 9:
        if candidate[6] < candidate[9]:
            candidate[6] = candidate[6] + 1
        else:
            candidate[9] = candidate[9] + 1
    else:
        candidate[to_int] = candidate[to_int] + 1

print(max(candidate))