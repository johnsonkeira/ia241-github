'''
lab 5

if statement
'''

#3.1
a_color = 'green'

if a_color == 'green': 
    print("you've won 5 points")
    
#3.2
a_color = 'pink'

if a_color == 'green': 
    print("you've won 5 points")
else:
     print("you've won 10 points")
     
#3.3
favorite_fruits =['mango', 'banana', 'strawberries']

if 'mango'in favorite_fruits:
    print('i really like the flavor of a mango')
if 'banana' in favorite_fruits:
    print('bananas are my favorite to use for smoothies')
if ' strawberries'in favorite_fruits:
    print("i love chocolate covered strawberries")

#3.4
age = 19

if age < 10:
    print('kid')
elif age < 20:
    print('teenager')
else:
    print('adult')
    if age > 65:
        print ('elder')
    