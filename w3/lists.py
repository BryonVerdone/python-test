# print('hello world')

# print('this is python')
# x= 5
# y=3

# print(name)
# if(x>y):
#   print('x is bigger than y')
#   print('i like tacos')

#   # this is a comment

#   # Casting 

#   someString= str(3)

#   print(type(someString))

# a,b,c= 'taco','green','truck'

# print(a,b,c)

# # Unpacking a collection 

# fruits= ['apple','banana','orange']
# d,e,f= fruits
# print(d,e,f)

# bryonsAge= 28
# print(name,bryonsAge) 

# def addnums(num1,num2):
#   print(num1+num2)

# addnums(13,52)

# # print random number
# import random

# from more_itertools import last

# print(random.randrange(1,654))

# # get a character from a string

# lastName= 'verdone'

# print(lastName[3])

# for letter in lastName:
#   print(letter)

# LISTS ##########################################

# List items can be of any data type



friends= ['david','jer','nick','brett']

print(friends[2])
print(len(friends))


# Range of Indexes

fruit = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango",'blueberry']
print(fruit[2:6])

# print items from the start up to index
print(fruit[:4])
# print items from starting index to the end

print(fruit[3:])

# check to see if item is in list
if 'blueberry' in fruit:
  print('yes we have blueberries')
else:
  print('sorry no blueberries')

  # Change Item Value
fruit[0]= 'carrot'
print(fruit)
# Add list items
newList= ['taco','pizza','cookie']
# newList.insert(2,'apple')
print(newList)
anotherList=['rock','stick','tree']

# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

newList.append('soup')
print(newList)
newList.extend(anotherList)
print(newList)

# Remove list items

newList.remove('taco')
print(newList)

# The pop() method removes the specified index.

newList.pop(3)
print(newList)

# The clear() method empties the list. The list still remains, but it has no content.

clearThisList= ['shoe','shirt','pants']
clearThisList.clear()
print(clearThisList)

# Loop Through a List

shoes= ['nike','adidas','new balance']

for i in shoes:
  print(i)