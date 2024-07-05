'''
https://www.acmicpc.net/problem/1193

백준 1193
'''
'''
1 - 1/1
2 - 1/2
'''

input_number = int(input())

line = 1
while input_number > line:
    input_number = input_number - line
    line = line + 1

mother = 0
son = 0

if line % 2 == 0:
    mother = line - input_number + 1
    son = input_number
else:
    son = line - input_number + 1
    mother = input_number

print(son, '/',mother, sep='')
