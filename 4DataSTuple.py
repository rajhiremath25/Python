# Data Structures - Tuple, List, Dictionary and Set

# Tuple is ordered collection of elements enclosed within ()
# Tuples are immutable
# Tuples can have elemets of different data types

tup1 = (1, "a", True, 3.14, "my name is john", 3 + 5j)
print(type(tup1))
print(tup1[0])
print(tup1[2])
print(tup1[-1])
print(tup1[1 : 4])

# you can not modify the tuple becuase it is immutable
# tup1[1] = "hi" TypeError: 'tuple' object does not support item assignment
print(len(tup1))
# tup1[6] = "new element" 'tuple' object does not support item assignment

tup2 = (1, "a", "me")
tup3 = (2, "b", "you")
print(tup2 + tup3) # Concatination
tup4 = tup2 + tup3
print(tup4)
tup4 = tup3 + tup2
print(tup4)

print(tup2 * 3) #repeating
print(tup2 *3 + tup3) #repeating and concanitating

tup5 = (1, 2, 3, 4, 5)
print(min(tup5))
print(max(tup5))