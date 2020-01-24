#python hello_world.py
#first python program

#variables in python are labels that referenced by values
print('>>> message = "hello python variable"')
message = 'hello python variable'

#basic print
print('''\n#print using print():
print("printing variable: " + message)''')
print("printing variable: " + message)

#division returns float
print("\n#Division returns float 10 / 1 = ")
print(10 / 1)

#floor
print("\n#Drop decimal in division with \\\\. 5 \ 2 = ")
print(5 // 2)

#powers
print("\n#Powers with **. 2**3 = ")
print(2**3)

#mixed operands result in float
print("\n#Mixed operands result in float: 2.5 * 2 = ")
print(2.5 * 2)

#round()
print("""\n#Rounding 126.18273 to second decimal with round():
>>> print(round(126.18273, 2)""")
print(round(126.18273, 2))

#qoutes
print("\nUnpaired qoute prints as part of string:")
print("Tom's books")

#quote wrapping
print('\n"Quote pairs wrapped in opposite type quote pairs (single vs double) will print"')

#multi-line
print("""\n#Strings wrapped in triple quotes (''', etc.)
can span multiple lines
    and preserve indentation""")

#concat
print("""\n#String concatenation with +
>>> print('The' + ' ' + 'String')""")
print('The' + ' ' + 'String')

#multiple times
print("""\n#Using * on string will print multi times
>>> print(3 * 'string')""")
print(3 * 'string')

#auto-concat
print('\n#String literals next to each other auto concat: '
""">>> print('the' ' string'
>>>                                            ' is auto concated')""")
print('the' ' string'
      ' is auto concated')

#string var concat
print("""\n#Can concat string to vars, expression result strings, etc. with + :
>>> fruit = 'apple'
>>> print('   the ' + fruit)""")

fruit = 'apple'
print('   the ' + fruit)

#string indexing
print("""\n#Can read (only) chars in string by referencing index as if array of chars
>>> print(fruit[0])""")
print(fruit[0])

print("""\n#Access from end index back via negative nums
>>> print(fruit[-1]):""")
print(fruit[-1])

#slicing
print("""\n#Can copy out substring (exclusive end char) as if pulling range from char array:
>>> print(fruit[2:4]):""")
print(fruit[2:4])

#auto-close slice
print("""\n#If leave end off of slice (still using :), will count missing side as start or end automatically
>>> print(fruit[:4]):)""")
print(fruit[:4])

#negative index slice
print("""\n#Can also slice using negative index:
>>> print(fruit[-4:0])):""")
print(fruit[-4:])

#out of bound index slice
print("""\n#Index end out of bound uses default start/end instead of error:
>>> print(fruit[0:100]):""")
print(fruit[0:100])

#string length
print("""\n#String length via len(my_string):
>>> print(len(fruit)):""")
print(len(fruit))

#capitalizating Words
print("""\n#Uppercase words with title():
>>> my_string = '   this is my string   '
>>> print(my_string.title())""")

my_string = '   this is my string   '
print(my_string.title())

#full casing
print("""\n#Upper or lower case whole string with upper() and lower():
>>> print(my_string.upper())
>>> print(my_string.lower()):""")
print(my_string.upper())
print(my_string.lower())


#f-strings
print("""\n#f-strings are python ver of template literals in JS:
>>> print(f\"The fruit is: {fruit}\")""")
print(f"The fruit is: {fruit}")

#f-string w/ function
print("""\n#f-string holding function output:
>>> print(f'The fruit is {fruit.upper()}')""")
print(f'The fruit is {fruit.upper()}')

#format() method
print("""\n#If using Python under v3.6, use format() instead of f-strings
>>> print("My name is {}. This {} tale.".format("Ishmael", "is my"))""")
print("My name is {}. This {} tale.".format("Ishmael", "is my"))

#tabs
print("""\n#Add tabs to string with \\t special char:
>>> Nested
>>> \\tlist
>>> \\t\\twith tabs""")
print("""Nested
\tlist
\t\twith tabs""")


#removing whitespace
print("""\n#Can remove whitespace on right, left, or both sides of string with rstrip(), lstrip(), and strip():
>>> print(f'{'   whitespace   '.rstrip()}
>>> {'   whitespace   '.lstrip()}
>>> {'   whitespace   '.strip()}')""")

print(f"""{'   whitespace   '.rstrip()}
{'   whitespace   '.lstrip()}
{'   whitespace   '.strip()}""")

#multi assign
print("""\n#Multiple assignment with syntax: a, b, c = 1, 2, 3:
>>> x, y, z = 'dog', 123, 1.8
>>> print(f'x: {x}, y: {y}, z: {z}')""")
x, y, z = 'dog', 123, 1.8
print(f'x: {x}, y: {y}, z: {z}')

#lists
print("""\n#Indexing and slicing works the same as strings:
>>> my_list = [1, 2, 'string', 'word'.upper()]
\n>>> print(my_list)""")
my_list = [1, 2, 'string', 'word'.upper(), 'fish', 1234]
print(my_list)

print('\n>>> print(my_list[-1])')
print(my_list[-1])

print('\n>>> print(my_list[1:100]))')
print(my_list[1:100])

print('''\n>>> my_list[2:4] = []
>>> print(my_list)''')
my_list[2:4] = []
print(my_list)

#nested list
print("""\n#Nested list:
>>> my_nested = [[1, 8, 12], [ ‘a’, ‘b’, ‘c’]]
>>> print(my_nested[1][2])""")
my_nested = [[1, 8, 12], [ 'a', 'b', 'c']]
print(my_nested[1][2])

#remove from list
print("""\n#Remove from list using del keyword:
>>> del my_list[2]
>>> print(my_list)""")
del my_list[2]
print(my_list)


print("""\n#Can pop off end with my_list.pop():
>>> my_list = [0, 1, 2, 3, 4, 5]
>>> my_list.pop()
>>> my_list.pop()
>>> print(my_list)
>>> print(popped)""")
my_list = [0, 1, 2, 3, 4, 5]
my_list.pop()
popped = my_list.pop()
print(my_list)
print(popped)


print("""\n#remove() an index, append() to end, insert() in index
>>> my_list = [0, 1, 2, 4, 2, 1, 9, 2, 4, 2, 8]
>>> my_list.remove(2)
>>> my_list.append('B')
>>> my_list.insert(2, 'A')
>>> print(my_list)""")
my_list = [0, 1, 2, 4, 2, 1, 9, 2, 4, 2, 8]
my_list.remove(2)
my_list.append('B')
my_list.insert(2, 'A')
print(my_list)

print("""\n#if uses 'if ... :', 'elif ... :', 'else:' with no ( ).
#Python indentation (equal spaces or tabbed) based blocks instead of {} based""")
x, y = 0, 1
if x > y:
   print('x > y')
   print('check the indentation')
elif x < y:
   print('x < y')
else:
   print('x == y')

print("""\n#loop using 'for index in iterable:'
#index is current index, and loop ends when iterable ends
>>> ints = [1, 2, 5, 9]
>>> for int in ints:
>>>     print(int)""")
ints = [1, 2, 5, 9]
for int in ints:
    print(int)

print("""\n#can loop n times with range(n) and for:
>>> for i in range(4):
>>>   print(i)
0
1
2
3""")
for i in range(4):
   print(i)

print("""\n#range() also takes end and step params to produce x to y range, via z steps
#note that end in range is exlusive by 1 step from specified end (zero oriented):
>>> for i in range(-20, 40, 10):
>>>    print(i)""")
for i in range(-20, 40, 10):
   print(i)

print("""\n#for loops can run with an else clauses that excutes on loop completion
#if loop executes due to break, then else will not run...loop just breaks and exits:\n
>>> for i in range(3):
>>>     print("feels")
>>>     if(i == 2):
>>>         break
>>> else:
>>>     print("badman")
feels
feels
feels       //break hit, loop exits
\n>>> for i in range(3):
>>>     print("feels")
>>>     if(i == 100):
>>>         break
>>> else:
>>>     print("badman")
feels
feels
feels       //loop completes
badman      //else runs
""")
# for i in range(3):
#     print("feels")
#     if(i == 2):
#         break
# else:
#     print("badman")
#
# for i in range(3):
#     print("feels")
#     if(i == 100):
#         break
# else:
#     print("badman")

print("""\n#standard use for continue...if hit, jump to next iteration:
>>> for i in range(4):
>>>     if(i == 2):
>>>         continue
>>>     print(i)""")
for i in range(4):
    if(i == 2):
        continue
    print(i)

print("""\n""")

print("""\n""")

print("""\n""")
