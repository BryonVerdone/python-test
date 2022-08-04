# num1= 100
# num2=50
# userInput= int(input('please enter a number \n'))
# if(userInput >= num1):
#   print(f'This number is equal to or greater than {num1}')
# elif(userInput <= num2):
#   print(f'This number is less than or equal to {num2}')




# name= 'bryon'
# age=28

# actualAge= 28.70
# math= 5+3/5*34


# results= age+math+actualAge

# print(type(results))


print('hello and welcome to our coffee shop!!!!!')
name= input('Hello what is your name? \n')

print(f'hello {name} what would you like to drink? Here is our menu')
order= input('black coffee,tea, latte \n')
price= 8 
amount= input('how many would you like?\n')
total= (int(amount) * price)
print(f'greet choice I\'ll get your {amount} {order}s for you right now that will be ${total}')