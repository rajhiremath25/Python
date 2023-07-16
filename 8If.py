a = 8
b = 9
if (a < b) :
    print("a is less than b", "a = " , a, "b = "  , b)

if (b < a):
    print("a is not less than b", "a = ", a, "b = ", b)
else :
    print("a is less than b", "a = ", a, "b = ", b)

a = 10
c = 30
b = 20

if (a > b & a > c):
    print ("a is greatest")
elif (b > c & b > a):
    print("b is greatest")
else:
    print("c is greatest")

tup1 = (1, 2, 3, 4, 5)
if 2  in tup1:
    print(" 2 is present in tup1")

if 6 in tup1:
    print(" 6 is present in tup1")
else :
    print(" 6 is not present in tup1")

list1 = [1, 2, 3, 4, 5]
if list1[1] == 2:
    list1[1] = list1[1] + 100
print(list1)

if list1[4] == 2:
    list1[4] = list1[4] + 100
else :
    list1[4] = list1[4] + 500

print(list1)

dist1 = {"mango": 100, "tomato": 200, "potato": 300}
if dist1["mango"] == 100:
   dist1["mango"] = dist1["mango"] + 500
print(dist1)

