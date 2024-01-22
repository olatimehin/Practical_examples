
# part 1

# import modules 

import math as m

x = m.sqrt(64.547895)
print(x)

from math import sqrt
x = sqrt(64.5478965)
print(x)

# creating functions     12/12/2023
def addition(x,y):
    value = x + y
    return value
print(addition(2 ,5))
# function 
my_list = [1,2,3,4,5,6,7,8,9,10] #initialising a list variable 

def addition(list): # the list here was replace by my list when recalling down
    
    total = 0

    for value in list: # this is just a loop to iterate over the function and add it together 
        total += value

    return total
result = addition(my_list)  # calling the function with my_list parameter
print(result)

# alternatively
my_list = [1,2,3,4,5] #initialising a list variable 

def addition(kele): # the kele here was replace by my list when recalling down
    
    total = 0

    for value in kele: # this is just a loop to iterate over the function and add it together 
        total += value

    return total      # this will keep the total 

result = addition(my_list)  # calling the function with my_list parameter and store it
print("My result is",result)

# return is when you want to use same value somewhere,you can recall
# it any time but if you dont want to use the value again you can simply 
# recall the function down
def add():
    a = 20
    b = 25
    result = a + b
    return result

# Call the function and store the result
sum_result = add()

# Print the result
print("The sum is:", sum_result)

# another pattern
def add():
    a = 2
    b = 5
    print(a + b) # nothing will happen until you recall the function
add()  #recalling

my_list = [9,8,7,6,5] # declare a list

def substraction(list): # define function 
    
    total = list.pop(0) #remove the first element of list
    
    for value in list:
        
        total -= value
        
    return total 

sub_list = substraction(my_list)
print(sub_list)'''


# import file
'''import matplotlib.pyplot as plt # this is use to draw a graph

x = [2,5,12,13.7,18]
y = [5,13,15.8,12,22]   # x, y must have the same number of list

plt.plot(x, y)
plt.show()'''

  
import random as rd 

'''cpu_choice = rd.randint(1,3)  # it will bring out random number start from 1 to 3
print(cpu_choice)

user_choice = int(input("Input 1 for rock, 2 for paper,3 for scissors: "))

#rock = 1
#paper = 2
#scissors = 3

if cpu_choice == 1 and user_choice == 1:
    print("Draw")
    
elif cpu_choice == 1 and user_choice == 2:
    print("You win!")
    print("Paper beats rock")
    
elif cpu_choice == 2 and user_choice == 1:
    print("You loose")
    print("Try again")

elif cpu_choice == 3 and user_choice == 2:
    print("You loose slightly")
      
elif cpu_choice == user_choice:
    print("Its a tie!")'''
    

# introduce while loop
import random as rd 

'''while True:
    cpu_choice = rd.randint(1,3)  # it will bring out random number start from 1 to 3
    print(cpu_choice)

    user_choice = int(input("Input 1 for rock, 2 for paper,3 for scissors: "))

#rock = 1
#paper = 2
#scissors = 3

    if cpu_choice == 1 and user_choice == 1:
        print("Draw")
        continue    
    elif cpu_choice == 1 and user_choice == 2:
        print("You win!")
        print("Paper beats rock")
        continue
    elif cpu_choice == 2 and user_choice == 1:
        print("You loose")
        print("Try again")
        continue
    elif cpu_choice == 3 and user_choice == 2:
        print("You loose slightly")
        continue
    elif cpu_choice == user_choice:
        print("Its a tie!")
        break


def addition(x ,y):
    
    value = x + y
    return value

#sum_addition = addition(3, 5) # to recall and store
#print(sum_addition)

x = int(input("Please enter a number : "))
y = int(input("Please enter a number : "))

total = addition(x, y) # call function
print(total * 4)'''


