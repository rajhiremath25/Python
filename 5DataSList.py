# List is ordered collection of elements enclosed in []
# Lists are mutable

list1 = [1, "a", True, 3.14, "my name is john", 3 + 5j]
print(type(list1))
print(list1[0])
print(list1[2])
print(list1[-1])
print(list1[1 : 4])

#change value of oth element
list1[0] = 100
print(list1)

#append an element
list1.append(500)
print(list1)

#remove last element
list1.pop()
print(list1)

#reverse list
print(list1.reverse()) #list is reversed but no o/p
print(list1)

list1 = ["I", "Lion", "King"]
list1.insert(1, "am")
print(list1)

list1 = [1, "a", "me"]
list2 = [2, "b", "you"]

print((list1 + list2))
print(list1)
print(list2)

print((list2 + list1))

print(list1 * 3)
print(list1)