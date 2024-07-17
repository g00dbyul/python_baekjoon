'''
3
3 7
15 7
5 2
'''

N = int(input())
positions = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(N):
    x, y = map(int, input().split())

    for i in range(y, y+10):
        for j in range(x, x+10):
            positions[i][j] = 1


result = 0

for p in positions:
    result = result + sum(p)

print(result)
