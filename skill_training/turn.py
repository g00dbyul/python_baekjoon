# 북,동,서,남 순서대로 회전하기(0,1,2,3)

# 초기화는 랜덤
d = 0

forward = {
    0: (-1, 0),
    1: (0,1),
    2: (1, 0),
    3: (0,-1),
}

def turn(d):
    return (d + 1) % 4

graph = [[0] * 5 for _ in range(5)]

x, y = 2,2

while True:
    print(x, y)
    move = forward[d]
    if 0 <= x + move[0] < 5 and 0 <= y + move[1] < 5:
        x = x + move[0]
        y = y + move[1]
    else:
        break




