'''
print('Hello, "world!"') # // - целостное деление  / обычное деление
print(type('helo, world!')) #string - строка
print('hello,' + 'world!') #concatenate
print('hello, ' + 'world!')
print('hello,' + ' world!')
print('1' + '1')
print(1+1)
print(True, False) #boolean
print(5 > 10, 10 > 5)
print(5 == 5)
print(5 != 5)
print(5 != 5 and 5 < 10)
print(5 == 5 and 5 < 10)
print(5 != 5 or 5 < 10)
print(5 == 5 or 5 < 10)
print(type(int('5'))) # string to int
print(type('5'))
print(type(bool('5')))
print(type(str('5')))
print(type(float('5')

#lesson 2
name = "Denis"
name1 = ['jerry', 'gabit', 'akon', 'gani', 'aibek']
name2 = 'jerry', 'gabit', 'akon', 'gani', 'aibek'
print("hello" + name)
print("hello " + name)

print("Hello, ""Denis")
print("hello" * 5)
print(name[0])
print(name[-1])
print(name1[0])
print(name1[-1])
print(name2[0])
print(name[0:3])
print(name[0:5])
print(name[0:3:2])
print(name[0:3:1])
print(name[0:3:3])
print(name[0:6:3])
print(name[0:7:3])
print(name[0:6:4])
print(name[0:7:4])
print(name[:3])
print(name[2:])
print(name[:-1:])

# lesson 3
name = "denis"
print(name)
name = "urban"
print(name)
Date_of_birth = "september 2008"
print(Date_of_birth)
DateOfBirth = "ssss"
print(DateOfBirth)


#lesson 4
name = "Urban"
print(name, type(name))
name = 5
print(name, type(name))
name = 5.6
print(name, type(name))
name = [1, 2]
print(name, type(name))


#lesson 5
name = input("your name: ")
current_year = 2024
date_of_birth = (int(input('which one of year you born? ')))
age = current_year - date_of_birth
print(type(name))
print("hello,", name)
print("in this year your age is ", age)

print("привет, я строка в нижнем регистре".upper())
print("привет, я строка в нижнем регистре".lower())
print("привет, я строка в нижнем регистре".upper().lower())
print("привет, я строка в нижнем регистре".lower().upper())
print("привет, я строка в нижнем регистре".replace("привет", "пока"))
print("привет, я строка в нижнем регистре".replace(" ", "-"))


#lesson 6
food = ['apple', 'coconut', 'banana']
print(food[0])
print(food[-1])
food[0] = "peach"
print(food[0])
food.append(True)
print(food)
#food.extend('String')
food.extend(['String'])
print(food)
food.remove("peach")
print(food)
print("coconut" in food)
print("coconut" not in food)
print(food[0:2])
print(food[0:3])
print(food[0:3:2])



#lesson 7

tuple_ = 1, 2, 3, 4, True, "string"
tuple2 = 1, 2, 3, 4
tuple3 = tuple([1, 2, 3, 4])
print(tuple_)
print(tuple2)
print(tuple3)
print(type(tuple_))
print(tuple_[0])
list = (1, 2, 3, 4, True, "string")
print(tuple_.__sizeof__())
print(list.__sizeof__())
tuple_ = ([1, 2], 0)
print(tuple_)
tuple_[0][0] = 2
print(tuple_)
tuple_ = ([1, 2], 0) + (1, 2)
print(tuple_)
tuple_ = ([1, 2]) * 3
print(tuple_)


#lesson 8
phone_book = {"Gabit": 87779896914, "akerke": 87056302133}
print(phone_book)
print(phone_book["Gabit"])
phone_book["Gabit"] = 2763535536
print(phone_book)
phone_book["Anton"] = 8777719365
print(phone_book)
del phone_book["Anton"]
print(phone_book)
phone_book.update({"sahsa": 9847807484,
                   "alex": 9482908290389})
print(phone_book)
print(phone_book.get("Gabit"))
print(phone_book.get("Anton"))
print(phone_book.get("Anton", "Такого ключа нет"))
a = phone_book.pop("alex")
print(phone_book)
print(a)
print(phone_book.keys())
print(phone_book.values())
print(phone_book.items())
#phone_book = {"Gabit": [87779896914, 'Gabit'], "akerke": 87056302133}
#phone_book["Anton"] = 8777719365
#phone_book.update({"sahsa": 9847807484,
#                   "alex": 9482908290389})
#print(phone_book)
#set_ = {1, 2, 3, 4, 5, 1, 2, 3, 4}
#print(set_)
set_ = {1, 2, 3, 4, 5, 1, 2, 3, 4, "string", True, (1, 2, 3)}
#print(set_)
list_ = [1, 1, 1, 1, 2, 3, 2, 2]
list_ = set(list_)
#print(set(list_))
print(list_)
#print(list_.discard(1)) дискарт не будет выдавать ошибку при не нахождений обькта
#print(list_.remove(1))
print(list_.add(5))
print(list_)

from re import match

#lesoon 9
print("comedy")
print("fantasy")
print("horror")
genre = int(input("llkaaa"))
match genre:
    case 1:
        print("1")
    case 2:
        print("2")
    case 3:
        print("3")
    case 1 | 3:
        print("3")
    case _:
        print("fdhsj")

#lesson 10
x = r = 1
while x < 10:
    while r < 10:
        print(x, "*", r, "=", x*r, end="|")
        r += 1
    print()
    r = 1
    x += 1

number = int(input())
s = 0
while number:
    s += number % 10
    number //= 10
print(s)


#lesson 11
s = 'hello'
for i in s:
    print(i)


for i in range(1, 10, 1):
    print(i)

for i in range(10):
    print(i)

for i in range(10, 1, -1):
    print(i)

for i in range (1, 10):
    for y in range (1, 10):
        print(i, "*", y, "=", i * y,)
    print()

for i in range(1, 10):
    if i == 7:
        break
    print(i)

for i in range(1, 10):
    if i == 7:
        break
    print(i)
else:
    print(1)

for i in range(1, 10):
    if i == 7:
        continue
    print(i)

for i in range(1, 10):
    if i == 7:
        continue
    print(i)
else:
    print(7)

k = int(input())
s = 0
for _ in range(k):
    number = int(input())
    if number % 6 == 1:
        s += number
print(s)

#lesson 11
s = "hElLO woRLD"
print(s.capitalize())
print(s.title())
print(s.swapcase())
s1 = "JJJ"
print(s1.isupper())
s2 = "jjj"
print(s2.islower())
s3 = "dfdkfjsdk"
print(s3.isalnum())

from http.cookiejar import join_header_words

l = ["asdd", "fjkas", "fjkask"]
print("-" .join(l))

s = "Hello World"
print(s.split("l", 1))          list

s = "Hello World"
print(s.partition(" "))            str

s = "******Hello World******"
print(s.strip("*"))
print(s.lstrip("*"))
print(s.rstrip("*"))
print(s.find("*"))
print(s.rfind("*"))
print(s.index("*"))
print(s.rindex("*"))
print(s.replace("*", "!"))
print(s.replace("*", "!", 1))
print(s.count("*"))
print(len(s))
print(sorted(s))                  list
print(sorted(s, reverse=True))      list

print(ord("f"))
print(chr(102))

s = input()
result = ''
for i in range(len(s)):
    if i % 2 != 0:
        result += s[i]
print(result)

#lesson 12
a = [i for i in range(1, 100) if i % 2 == 0 and  i % 3 == 0]
print(a)
a = [i+1 for i in range(1, 100) if i % 2 == 0 and  i % 3 == 0]
print(a)
a = [i**2 if i % 2 == 0 else i ** 3 for i in range(1, 100)]
print(a)

bu = ["Vanya", "Petya", 'Katya', [1, 2, 3]]
print(bu[-1][-1])

# lesson 13
progs = ["python", "java", 'c++']
progs.insert(1, "php")
print(progs)

progs = ["python", "java", 'c++']
numb = [1, 2, 3]
progs.extend(numb)
print(progs)

progs = ["python", "java", 'c++']
progs.clear()
print(progs)

pr = [3, 2, -7, -5, 19]
pr.sort(key=abs)
print(pr)

#lesson 13
x, y, z = 12, 30, 60
print(x)
print(y)
print(z)

x, y, z, *t = 12, 30, 60, 50, 1000
print(x)
print(y)
print(z)
print(t)

x = 5
y = 10
x, y = y, x
print(x)
print(y)

x = (12, 30,(1, 10, 12), 60, 50, 1000)
print(x[2][1])

x = (12, 30,[1, 10, 12], 60, 50, 1000)
x[2][1] = 1000
print(x)

a = {1, 2, 3, 4}
b = {2, 3, 4, 5}
res = a.union(b)
print(res)

a = {1, 2, 3, 4}
b = {2, 3, 4, 5}
res = a | b
print(res)

a = {1, 2, 3, 4}
b = {2, 3, 4, 5}
res = a & b
print(res)

a = {1, 2, 3, 4}
b = {2, 3, 4, 5}
res = a.intersection(b)
print(res)

a = {1, 2, 3, 4}
b = {2, 3, 4, 5}
a.update(b)
print(a)

a = {1, 2, 3, 4}
b = {2, 3, 4, 5}
a |= b
print(a)

a = {1, 2, 3, 4}
b = {2, 3, 4, 5}
res = a.difference(b)
print(res)

a = {1, 2, 3, 4}
b = {2, 3, 4, 5}
res = a ^ b
print(res)

a = {1, 2, 3, 4}
b = {2, 3, 4, 5}
res = a.symmetric_difference(b)
print(res)

a = {1, 2, 3, 4}
b = {1, 2, 3, 4}               #ПРОВЕРКА ПОДМНОЖЕСТВА
print(a.issubset(b))

a = {1, 2, 3, 4}
b = {1, 2, 3, 4}                 #ПРОВЕРКА НАЛМОЖЕСТВА
print(b.issuperset(a))

#lesson 14
sp = [[1, 2], [3, 4]]
s1 = dict(sp)
print(s1)

sp = ('ab', "cd")
s1 = dict(sp)
print(s1)

sl = {i: i**2 for i in range(1, 10)}
print(sl)

s = 'hello world'
sl = {i: s.count(i) for i in set(s)}
print(sl)

s1 = [1, 2, 3, 4]
s2 = ["one", 'two', 'three', 'four']
sl = dict(zip(s1, s2))
print(sl)

sl = dict.fromkeys(["a","b","c", "d"], 1000)
print(sl)

sl = {
    "name": "Vasya",
    "Age": 17,
    "City": "Arys"
}
l = sl.popitem()
print(sl)
print(l)

sl = {
    "name": "Vasya",
    "Age": 17,
    "City": "Arys"
}
print(sl.get("Age"))
print(sl.get(78))
print(sl.get(78, "havent"))

sl = {
    "name": "Vasya",
    "Age": 17,
    "City": "Arys"
}
print(sl.setdefault(78, "heek"))
print(sl)

sl = {
    "name": "Vasya",
    "Age": 17,
    "City": "Arys"
}
print(sl.setdefault("name"))
print(sl)

sl = {
    "name": "Vasya",
    "Age": 17,
    "City": "Arys"
}
sl1 = {
    1: 'one',
    2: 'two'
}
sl.update(sl1)
print(sl)

sl = {
    "name": "Vasya",
    "Age": 17,
    "City": "Arys"
}
print(dict(sorted(sl.items())))

tel = {
    "ivan": {
        "phone": 874748748,
        "city": "arys",
    },
    "vasya": {
        "phone": 94783632,
        "city": "moscow",
    }
}
print(tel["ivan"]["city"])

tel = {
    "ivan": {
        "phone": 874748748,
        "city": "arys",
    },
    "vasya": {
        "phone": 94783632,
        "city": "moscow",
    }
}
for i in tel.keys():
    for x, y in tel[i].items():
        print(x, y)

# lesson 15
def f1(a, b, c):
    return a * b - c

result = f1(10,15, 150)
print(result)

def f1(a, b):
    return a * b

n1 = int(input())
n2 = int(input())
result = f1(n1, n2)
print(result)

def f1(*args):
    return args

print(f1("hello", 78, 74))

def f1(**kwargs):
    return kwargs

print(f1(a="hello", b=78, c=74))

#lesson 16
def fun(x1, x2):
    a = 1000
    c = x1 + x2 + a
    return c

a = 2000
print(a)
print(fun(2,4))
print(a)

def fun(x1, x2):
    global a
    a = 1000
    c = x1 + x2 + a
    return c

a = 2000
print(a)
print(fun(2,4))
print(a)

def fun():
    a[1] = 1000
    return a

a = [1, 2, 3]
print(a)
print(fun())
print(a)


def fun():
    a = [10, 100, 1000]
    return a

a = [1, 2, 3]
print(a)
print(fun())
print(a)

#lessob 16
def mtt(n):

    def mtr2():
        pr = 1
        for i in range(1, n):
            pr *= i
        return pr
    if n > 15:
        return mtr2()
    else:
        print("fjjkk")


print(mtt(10))

#lesson 17
def out(s):

    def closure():
        return s[0] + s[1]
    return closure


sp = [1, 2, 3, 4]
clos = out(sp)
sp[0] = 100
print(clos())

def mt11(func):

    def wrap():
        print("ДО")
        func()
        print("AFTER")
    return wrap

@mt11
def my_func():
    print('fjdfjdk')


my_func()

def mw1(func):

    def wea():
        new = func().upper() + "!"
        return new
    return wea

@mw1
def eew():
    return "айхан"


print(eew())

def mw1(func):

    def wea():
        new = func().upper() + "!"
        return new
    return wea

def mw2(func):

    def wea():
        new = func() + "?"
        return new
    return wea

@mw1
@mw2
def eew():
    return "айхан"


print(eew())

#lesson 18
products = [
    {
        "name": "milk",
        "price": 120,
        "value": 12,
    },
    {
        "name": "bread",
        "price": 30,
        "value": 100,
    },
    {
        "name": "orange",
        "price": 40,
        "value": 150
    }
]
print(sorted(products, key=lambda item: item["value"]))

import math
a = math.factorial(100)
print(a)

n = int(input())

factorial = 1

for i in range(2, n+1):
    factorial *= i

print(factorial)

numbs = [2, 1, 3, 4, 7, 11, 18, 45, 765, 23, 96, 45]

res = list(sorted(filter(lambda x: x > 20, numbs)))
print(res)
print(sorted([i for i in numbs if i > 20]))

print(sum(map(int, str(578375893759837 ))))
numbs = [2, 1, 3, 4, 7, 11, 18, 45, 765, 23, 96, 45]
print(list(map(lambda n: n ** 2, numbs)))
'''
from functools import reduce
numbs = [2, 1, 3, 4, 7, 11, 18, 45, 765, 23, 96, 45]
pr = reduce(lambda a, b: a * b, numbs,)
print(pr)































































































































































































































































































































































































