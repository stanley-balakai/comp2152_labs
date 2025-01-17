print("Hello World")
print(3)

a = 5
print(a)

b = "Michael"
print(b)

print(a, b)

print(type(a))
print(type(b))
print(type(9.0))
print(type(True)) # :)

# Hello World

print(5 + 5)
print(5 - 5)
print(a - 5)

c = 3
d = 4
e = 5
f = 6

g = c + d ** e / f % e

h = c - d / e ** f + d

# 0. Parentheses: ()
# 1. Powers/Exponents: **
# 2. Products: * / // %
# 3. Addition: + -
print(h)


#  Lists
l = [1, 2, 3, 5]
print(l)

m = [1, 2, 3, "five", 6.0]
print(m)

# String formatting
age = 5
print("My age is %d years old." % age)

print()

st_f = "I am {}{} years old"
# st_f1 = "I am not {} years old"
st_not_f = "not "

print(st_f.format(age, ""))
# print(st_f1.format(age))
print(st_f.format(st_not_f, age))

# User input
age1 = input("Please enter your age: ")
print(age1)