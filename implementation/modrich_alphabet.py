'''
ljes=njak

6

https://www.acmicpc.net/problem/2941
'''

c_alphabets = ['dz=', 'c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()

for alphabet in c_alphabets:
    word = word.replace(alphabet, '*')

print(len(word))









