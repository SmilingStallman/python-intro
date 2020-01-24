#countries to visit
countries = ['France', 'Germany', 'Poland', 'Peru', 'Sweden']

#printing countries
print(countries)

#counties alphabetized
print(sorted(countries))

#countries state not changed by sorted()
print(countries)

#countries in reverse order
countries.reverse()
print(countries)

#countries state changed by reverse() method call on it
print(countries)

#restoring original order by reversing again
countries.reverse()
print(countries)

#sort countries permenantly by calling .sort() on it
countries.sort()
print(countries)

#sort countries permenantly in reverse alpha order
countries.sort(reverse=True)
print(countries)

#list comprehension
num_list = [num + num for num in range(1,11)]
print(num_list)

#list functions
print(min(num_list))
print(max(num_list))
print(sum(num_list))

#list of nums divisable by 3
num_list = [num for num in range(3, 31, 3)]
print(num_list)

#looping through sliced num_list
for num in num_list[4:8]:
    print(num)

#An immutable list via a tuple
tuple = (1, 2, 3, 4, 5)

#trying to change tuple index val throws error
#tuple[2] = 'new'

#since no constant vars in python, can change val of var referencing tuple
tuple = (5, 4, 3, 2, 1)
print(tuple)

#logical operators
if(3 >= 2 and 'test' != 'Test'):
    print('and conditions satisfied')

if(3 >= 4 or 'test' == 'test'):
    print('one or both or conditions satified')

#checking if val in list
print(3 in num_list)

#if not empty list
my_list = []
if my_list:
    print('List is not empty')
else:
    print('List is empty')

if tuple:
    print('Tuple is not empty')
else:
    print('Tuple is empty')
