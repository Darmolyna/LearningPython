
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = 5
y = 10
print(x + y)

x = 5
y = "John"
print(x, y)


#Create a variable outside of a function, and use it inside the function

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()


#Create a variable inside a function, with the same name as the global variable

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#If you use the global keyword, the variable belongs to the global scope:

#Also, use the global keyword if you want to change a global variable inside a function.

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)