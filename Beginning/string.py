print("Hello")
print('Hello')

x = "Hello World"
print(len(x))

#Print only if "free" is present:
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")


#print only if "expensive" is NOT present:
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")


#You can use quotes inside a string, as long as they don't match the quotes surrounding the string:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
#You can assign a multiline string to a variable by using three quotes:


#Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5])


#Get the characters from the start to position 5 (not included):
b = "Hello, World!"
print(b[:5])


#Get the characters from position 2, and all the way to the end:
b = "Hello, World!"
print(b[2:])


#Use negative indexes to start the slice from the end of the string:
#Example: Get the characters: From: "o" in "World!" (position -5) To, but not included: "d" in "World!" (position -2):
b = "Hello, World!"
print(b[-5:-2])


#The lower() method returns the string in lower case:
a = "Hello, World!"
print(a.lower())


#The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())


#The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))

#The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']