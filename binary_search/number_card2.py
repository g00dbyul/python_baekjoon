'''
10
6 3 2 10 10 10 -10 -10 7 3
8
10 9 -5 2 3 4 5 -10

https://www.acmicpc.net/problem/10816
'''
import sys
input = sys.stdin.readline

N = int(input())
cards = sorted(
    list(
        map(int, input().split())
    )
)

M = int(input())
candidate = list(
    map(int, input().split())
)

card_dict = {}
for card in cards:
    if card in card_dict:
        card_dict[card] = card_dict[card] + 1
    else:
        card_dict[card] = 1

for c in candidate:
    if c in card_dict:
        print(card_dict[c], end=' ')
    else:
        print(0, end=' ')

