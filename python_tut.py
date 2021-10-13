from mmap import ACCESS_DEFAULT


if 5 < 2:
    print("yes")
else:
    print("no")


# icdsjaiofcwdscasdifasd of adsifp oasdpo a pa
# dsvskdfnvldf
# dcfdvcdfs
# cv
# setdfvs

'''
this is 
a 
multi line 
comment
'''


print('''
Hello 
this is 
a 
multi line 
print
''')


a = 1


b = 'himanshu'

print(a)

x = str(a)
y = int(3)
z = float(3)
print(x)
print(y)
print(z)

print(type(z))


q, w, e = "1", "2", "3"

print(q)
print(w)
print(e)

# functions


def myFun():
    global j
    j = 10
    print("my fun is called with the value of = " + str(j))
    print(a)
    print(b)


myFun()

print("this is global j"+str(j))

# print(globals)


'''
Built in data types 
Text      str
Numeric   int, float, complex 
Sequence  list, tuples, range
Map       dict
Set       set, frozenset
Boolean   bool
Bynary    bytes, bytearray, memoryview
'''

# print(type(x))

x = "Hello world"
x = 20
x = 1.1
x = ['apple', "banana", ]
x = ("apple", "banana")
x = range(6)
print(range(10))

x = {
    "name": "jhon",
    "age": 100
}

x = {"dafpdsf", "fadsfa"}
x = frozenset({})

x = True
y = False

x = b'himansnhu'

x = bytearray(5)

x = memoryview(bytes(5))


# Operators
'''
>Assignment 
>Comparision
>Logical
>Indentity
>Membership
>bitwise
'''


x = 10


# 10 + 2
# 10 - 1
# *
# /
# %
# **
# //

# **=
# +=

# ==
# !=
# >
# <
# >=
# <=


# Logical Operators
# and or not


# is not is


# in not in


# & and

# |
# ^

# ~
# <<

# >>

mylist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# for x in mylist:
#     print(x)


for i in range(len(mylist)):
    print(mylist[i])


newList = [x for x in mylist if x%2 == 0]



mylist.sort()

myset = {"apple", "banana", "cherry"}


thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 1960
}
print(thisdict)






i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1


def fun(a):
    print(a)
    return a



def my_fun(*a):
    print(a[0])




class MyClass:
    x = 4


obj = MyClass()

print(obj.x)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def print_obj(self):
        print("name" + self.name)
        print("age" + str(self.age))

obj = Person("himanshu",21)

obj.print_obj()

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
