#var has no declared type, no ending ;
message = "Hello world!"
print(message)

#multiple assignment
mul, ti, assign = 1, 2, 3
print(mul)      #1
print(assign)   #3

#division and multi-operand type always returns float
math = 9 / 9
print(math)     #1.0
math = 9 + 3.0
print(math)     #12.0

#can force return int with dropped remainder using //
math = 9 // 9
print(math)     #1

#string literal with multi-lines and space preservation via """
#/ prevents newline
print("""/
"There was no reason for me to stay in the real world any
longer. In the real world, it didn’t matter if I was there or not.
When I realized that, I was no longer afraid of losing my body."
""")

#repeat string
print(3 * "ee" + 2 * 'aa')

#string auto-contanation when strings adjacent
long_string = ('this is a very long string '
                'it is all one string')
print(long_string)

#string char access, negative num to start from right (read only access)
print(long_string[-1])

slice = 'having slice time'
print(slice[:2])      #no start slices from [0]. Exlusive end char num.
print(slice[0: 120])  #out of bounds num slices to end/start automatically

#uppercase each word
person = 'gerald thomas'.title()
print(person)

#template strings have f before, then calls and vars wrapped in {} inside string
print(f'{person} {slice} {"today".upper()}')

print(' test  '.strip() + 'test')

# >= 1 chapter python docs + "crash course" (12 chapters + 11 chapters)
# >= 1 chapter react docs (11 chapters)
# >= 1 chapter clean code (17 chapters)
# practice with both
#
