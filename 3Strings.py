# Strings are sequence of characters enclosed with single quotes (' '), double quotes (" ") or triple quotes (''' ''')
s1 = 'Hello World'
print(type(s1))
print(s1)

s1 = "Hello World 1"
print(type(s1))
print(s1)

s1 = '''Hello World 3'''
print(type(s1))
print(s1)

s1 = '''This is a multi
line
string
'''
print(type(s1))
print(s1)

my_string = "My Name is John"
print(my_string[0]) # First Character
print(my_string[-1]) # Last Character

print(my_string[4]) # Fifth Character

print(my_string[3:7]) # First element is inclusive, last is not
print(my_string[11:15])
print(my_string[11:])
print(my_string[:2])

print(my_string.upper())
print(my_string.lower())
print(len(my_string))

print(my_string.replace("My", "ma"))
print(my_string)
my_string = my_string.replace("My", "ma")
print(my_string)

my_string = "Hello world Hello my Hell0"
print(my_string.count("Hell"))
print(my_string.find("my")) # index from where sub string starts

fruits = "I like Mangoes,Banans,Grapes"
print(fruits.split(","))
print(fruits.split(",")[1])

my_string = "I am bnan ban nab bb"
print(my_string.find("b"))
print(my_string.count("b"))
print(my_string.replace("b", "a"))
print(my_string.split("b"))