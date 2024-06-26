'''
ljes=njak

6
'''

c_alphabets = ['dz=', 'c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()

for alphabet in c_alphabets:
    word = word.replace(alphabet, '*')

print(len(word))









