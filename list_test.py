'''
파이썬의 List, Set, Dict는 Mutable 객체이다.
단순히 변수에 대입하는 것은 데이터를 가르키는 포인터만 넘기는 것(Shallow Copy)이다.
만약 원본 데이터의 보존이 필요한 경우(ex: Back-Tracking) Deep Copy를 통해,
원본 데이터를 보존하며 다른 변수에 원본 데이터와 동일한 데이터를 복사할 수 있다.

List의 경우 class 함수로 copy()를 지원함.
라이브러리 역시 사용 가능
import copy
copy.deepcopy()

List Slice는 변수를 deepcopy 함 ([:] => 리스트 전체)

성능은 slice가 가장 빠르다고 함.

다만 Set, Dict 에서 처리는 추가적으로 알아봐야 함.
'''

# Shallow Copy
a = [1,2,3,4]
b = a
print(a)
print(b)

b[1] = 10
print(a)
print(b)

'''
a -> [1,10,3,4]
b -> [1,10,3,4]
'''

# Deep Copy
c = a[:]
print(a)
print(c)

c[1] = 5
print(a)
print(c)

'''
a -> [1,10,3,4]
c -> [1,5,3,4]
'''

d = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]

# 2차원 배열도 다행히 슬라이싱으로 Deep Copy 가능
e = d[:]
print(e)