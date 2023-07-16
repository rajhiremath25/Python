num = int(input("Enter Integer number to check if Even or Odd : "))
if (num % 2) == 0:
    print("This is Even Number")
else:
    print("This is Odd Number")

num = int(input("Enter Integer number to see if positive, negative or zero : "))
if num > 0 :
    print("Number is positive")
elif num < 0 :
    print("Number is negative")
else :
    print("Number is zero")

factorial = 1
num = int(input("Enter Integer number to get the Factorial : "))
if num == 0 :
    print("Factorial of zero is zero")
    factorial = 0
elif num < 0 :
    print("Factorial does not exist for negative numbers")
    factorial = None
else :
    for i in range(1, num+1) :
        factorial = factorial * i
print(factorial)

num = int(input("Enter Integer number to get the REVERSE : "))
temp = num
rev = 0
while temp > 0 :
    first = temp % 10
    rev = rev * 10 + first
    temp = temp // 10
print(rev)
if rev == num :
    print("number is pallondrom")
else :
    print("number is not pallondrom")

a = 0
b = 1
num = int(input("Enter Integer number to get the Fibonaci number at that place : "))
if num == 0 :
    print(a)
if num < 0 :
    print("invalid")
else :
    for i in range(2, num) :
        c = a + b
        a = b
        b = c
print(b)

num1 = int(input("Enter Integer number two numbers to reverse : "))
num2 = int(input("Enter Integer number two numbers to reverse : "))
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2
print(num1)
print(num2)

for num in range(10):
    for i in range(num):
        print(num, end=" ")
    print("\n")





