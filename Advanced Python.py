'''<List Comprehension>'''

r1 = [1, 2, 3, 4, 5]
r2 = [x*2 for x in r1]

r3 = [x*3 for x in r1 if x % 2]

r1 = ['black', 'white']
r2 = ['red', 'blue', 'green']
r3 = []
for t in r1:
    for p in r2:
        r3.append(t + p) # r3 = [t + p for t in r1 for p in r2] 

r4 = [n * m for n in range(2, 10) for m in range(1, 10) if (n * m) % 2] 

'''<Iterable & Iterator>'''

# iterable 객체를 대상으로 iter 함수를 호출해서 iterator 객체를 만든다

ds = [1, 2, 3, 4]
ir = iter(ds)

next(ir) # 1

next(ir) # 2

next(ir) # 3

next(ir) # 4

'''-----------------------------'''

ds = [1, 2, 3]
ir = iter(ds) # ir = ds.__iter__()
next(ir) # ir.__next__()
next(ir) # ir.__next__()

ir = iter([1, 2, 3])
while True:
    try:
        i = next(ir)
        print(i, end = ' ')
    except StopIteration:
        break

'''------------------------------'''

# 파이썬은 모든게 객체(함수도 객체)

def fct_fac(n):
    def exp(x):
        return x ** n
    return exp

'''
def fct_fac(n):
  return lambda x: x ** n
'''

f2 = fct_fac(3) # x ** 3
f2(2) # 8

# lambda args: expression (return이 내재되어 있음)

def show(s):
    print(s)

ref = show # ref = lambda s: print(s)
ref('hi')

'''<map & filter(list comprehension으로 대체 가능)>'''

def pow(n):
      return n ** 2

st1 = [1, 2, 3]
st2 = list(map(pow, st1))

ir = map(pow, st1)
for i in ir: # ir은 iterator 객체이므로 for루프 가능
    print(i, end = ' ')

st1 = [1, 2, 3]
st2 = [3, 2, 1]
st3 = list(map(sum, st1, st2))

st = ['one', 'two', 'three']
rst = list(map(lambda s: s[::-1], st))
print(rst)

st = list(range(1, 11))
fst = list(filter(lambda n: not(n % 3), map(lambda n : n **2, st))) # [9, 36, 81]

'''------------------------------'''

st1 = [1, 2, 3]
st2 = list(map(lambda n: n**2, st1)) # st2 = [n**2 for n in st1]

st = [1, 2, 3, 4, 5]
ost = list(filter(lambda n: n % 2, st)) # ost = [n for n in st if n % 2]

st = list(range(1, 11))
fst = list(map(lambda n: n**2, filter(lambda n: n % 2, st))) # fst = [n**2 for n in st if n % 2] 


'''<Tuple Packing & Unpacking>'''

# *는 위치에 따라 packing or unpacking

tri_two = 23, 12
print(tri_two) # (23, 12)

tri_three = (12, 25)
bt, ht = tri_three
print(bt, ht) # 12 25

nums = (1, 2, 3, 4, 5)
n1, n2, *others = nums
print(others) # [3, 4, 5]

nums = [1, 2, 3, 4, 5]
n1, n2, *others = nums
print(others) # [3, 4, 5]

def ret_nums():
    return 1, 2, 3, 4, 5

nums = ret_nums()
print(nums) # (1, 2, 3, 4, 5)

def show_nums(n1, n2, *other):
    print(n1, n2, other, sep = ',')

show_nums(1, 2, 3, 4) # 1, 2, (3, 4) : 매개변수 앞에 *는 나머지 값들은 튜플로 묶어서 이 변수에 저장하겠다는 뜻

def sum(*nums):
    s = 0
    for i in nums:
        s += i
    return s

print(sum(1, 2, 3)) # 6

# 튜플 안에 튜플 unpacking

t = (1, 2, (3, 4))
a, b, (c, d) = t
print(a, b, c, d, sep= ', ')
print(a, b)

p = (1, 2, (3, 4))
_, b, (_, d) = p # tip
print(b, d)

ps = [('lee', 172), ('jung', 182), ('yoon', 179)]
for n, h in ps:
    print(n, h, sep =', ')

'''<Named Tuple>'''

from collections import namedtuple
Tri = namedtuple('Triangle', ['bottom', 'height']) # 'Triangle' 이라는 이름의 클래스 생성
# Tri = namedtuple('Tri', ['bottom', 'height']) 클래스와 변수 이름 일치시키는게 tip
t = Tri(3, 7)
print(t[0], t[1])
print(t.bottom, t.height)

'''<Dict & Zip>'''

# zip은 튜플로 저장하지만 list(zip()) tuple(zip()) dict(zip()) 으로 변환
# zip은 3이상 조합도 가능

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = dict([('a', 1), ('b', 2), ('c', 3)])
d3 = dict(a = 1, b = 2, c = 3)
d4 = dict(zip(['a', 'b', 'c'], [1, 2, 3]))
# d1 == d2 == d3 == d4 


'''<dict looping & comprehension>'''

# dict.keys() dict.values() dict.items()

d = dict(a = 1, b = 2, c = 3)
for k in d.keys():
    print(k, end = ', ')

d1 = dict(a = 1, b = 2, c = 3)
d2 = {k : v*2 for k, v in d1.items() if v % 2}

ks = ['a', 'b', 'c', 'd']
vs = [1, 2, 3, 4]
d = {k : v for k, v in zip(ks, vs) if v % 2}

'''<using * and **>'''

def who(a, b, c):
    print(a, b, c, sep = ', ')

d = dict(a = 1, b = 2, c = 3)
who(*d) # key
who(**d) # value
who(*(d.items()))

def func(*args): # tuple
    print(args)

func() # ()
func(1, 2) # (1, 2)

def func(**args): # dict
    print(args)

func(a = 1) # {'a': 1}

def func(*args1, **args2):
    print(args1)
    print(args2)

func(1, a = 1) 
# (1,)
# {'a': 1}

'''<dict & defaultdict>'''

# 방법1
s = 'robbot'
d = {}
for k in s:
    if k in d:
        d[k] += 1
    else:
        d[k] = 1
# {'r': 1, 'o': 2, 'b': 2, 't': 1}

# 방법2
s = 'robbot'
d = {}
for k in s:
    d[k] = d.setdefault(k, 0) + 1 # d.setdefault(k, v) : k에는 키, v에는 디폴트 값
# k에 해당하는 키가 있을 때 키의 값 반환 k에 해당하는 키가 없을 때, 딕셔너리 k:v 저장하고 v 반환

# 방법3
from collections import defaultdict
s = 'robbot'
d = defaultdict(int) # int 함수(입력 x 시 0 반환) 등록하면서 defaultdict 호출 (디폴트 값을 갖는 딕셔너리) # defaultdict(lambda: 7) 넣으면 디폴트가 7
for k in s:
    d[k] += 1

'''<set & frozenset>'''
# set : mutable / frozenset : immutable

A = {'a', 'c', 'd', 'f'}
B = {'a', 'b', 'd', 'e'}

# 합집합: A - B 교집합: A & B 합집합: A | B 대칭 차집합: A ^ B

os = {1, 2, 3, 4, 5}
os.add(6)
os.discard(1)
os.update({7, 8, 9})
os &= {2, 4, 6, 8} # {2, 4, 6, 8}와 겹치는 원소만 남김
os -= {2, 4}
os ^= {1, 3, 6} # {1, 3, 6}에 있는 원소는 빼고 없는 원소는 추가

'''<sorting skill>'''

ns = [3, 1, 4, 2]
ns.sort()
ns.sort(reverse=True)


ns = [('Yoon', 33), ('Lee', 12), ('Park', 29)]
def age(t):
    return t[1]

ns.sort(key = age, reverse = True)


ns = [('Yoon', 33), ('Lee', 12), ('Park', 29)]
def name(t):
    return t[0]

ns.sort(key = name)


ns = [('Yoon', 33), ('Lee', 12), ('Park', 29)]
ns.sort(key = lambda t : t[1], reverse = True)


ns = ['Julia', 'Yoon', 'Steven']
ns.sort(key = len)


ns = [(3, 1), (2, 9), (0, 5)]
ns.sort(key = lambda t : t[0] + t[1], reveerse = True)

# sorted(): 원본을 그대로 두고 정렬된 사본을 얻고 싶을 때

org = [('Yoon', 33), ('Lee', 12), ('Park', 29)]
cpy = sorted(org, key = lambda t : t[1], reverse = True)

# 튜플은 내용 수정이 불가해 sort는 불가하지만 sorted()로 리스트 사본을 받을 수 있다.

org = (3, 1, 2)
cpy = sorted(org)
cpy1 = tuple(sorted(org))


'''<enumerate>'''

names = ['윤나은', '김현주', '장현지', '이지선', '박선주']
eo = enumerate(names) # eo = enumerate(names, 10) : 10부터 번호 매김
for n in eo:
    print(n)


names = ['윤나은', '김현주', '장현지', '이지선', '박선주']
dnames = {k : v for k, v in enumerate(sorted(names), 1)}

'''<about class>'''

class Father:
    def run(self):
        print("so fast, dad style")

class Son(Father):
    def run(self):# 메소드 오버라이딩
        print("so fast, son style")
    def run2(self):
        super().run() # 부모 클래스의 run 호출 방법

def main():
    s = Son()
    s.run()
    s.run2()

main()


class Car:
    def __init__(self, id, f):
        self.id = id
        self.fuel = f
    def drive(self):
        self.fuel -= 10
    def add_fuel(self, f):
        self.fuel += f
    def show_info(self):
        print("id:", self.id)
        print("fuel:", self.fuel)

class Truck(Car):
    def __init__(self, id, f, c):
        super().__init__(id, f)
        self.cargo = c
    def add_cargo(self, c):
        self.cargo += c
    def show_info(self):
        super().show_info()
        print("cargo:", self.cargo)

def main():
    t = Truck("42럭5959", 0, 0)
    t.add_fuel(100)
    t.add_cargo(50)
    t.drive()
    t.show_info

main()

# __init__ 을 super() 통해서 오버라이딩 하자.

'''<using __>'''

class Person:
    def __init__(self, n, a):
        self.__name = n
        self.__age = a
    def add_age(self, a):
        if(a < 0):
            print('나이 정보 오류')
        else:
            self.__age += a
    def __str__(self):
        return '{0}: {1}'.format(self.__name, self.__age)

def main():
    p = Person('James', 22)
    #p.__age += 1 작성 시 오류 남
    p.add_age(1)
    print(p)

main()

# __ 이용시 객체 외부에서 객체 내에 있는 변수(속성)에 직접 접근 불가 (오류남)

# 하지만 외부 접근을 강제로 막을 필요는 없기 때문에 보통 _ 하나만 붙여서 명시적으로 알림

class Person:
    def __init__(self, n, a):
        self._name = n
        self._age = a
    def add_age(self, a):
        if(a < 0):
            print('나이 정보 오류')
        else:
            self._age += a
    def __str__(self):
        return '{0}: {1}'.format(self._name, self._age)

def main():
    p = Person('James', 22)
    p._age += 1
    p.add_age(1)
    print(p)

main()


'''<string>'''

import string # for문으로 불러오기

string.ascii_lowercase # 소문자 abcdefghijklmnopqrstuvwxyz
string.ascii_uppercase # 대문자 ABCDEFGHIJKLMNOPQRSTUVWXYZ
string.ascii_letters # 대소문자 모두 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
string.digits # 숫자 0123456789