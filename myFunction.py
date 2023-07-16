from functools import reduce


def myFun():
    print("Hello")
myFun()

def add10(x):
    return x+10
print(add10(5))

def odd_even(x):
    if x % 2 == 0 :
        print("x is even")
    else :
        print("x is off")
odd_even(17)

g = lambda x : x * x * x + 100
print(g(7))

list1 = [1, 2, 3, 4, 5]
list1 = list(filter(lambda x : x % 2 == 0, list1))
print(list1)

list1 = [1, 2, 3, 4, 5]
list1 = list(map(lambda x : x * 2, list1))
print(list1)

list1 = [1, 2, 3, 4, 5]
list1 = reduce(lambda x, y : x + y, list1)
print(list1)