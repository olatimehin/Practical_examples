# Try and except 

'''usernames = ["Jimmy", "Billy", "John"]

while True:
    
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    
    if username in usernames :
        
        print("This username already exists! Try again. ")
        continue
    else:
        
        print(f"Welcome {username}. ")
        break

# Try and except code 

while True:
    
    try:
        
        num = int(input("Please enter a number: "))
        
        print("That is a nice number right there.")
        
        break
    
    except ValueError:
        
        print("That is not a valid number.Pleased try again...")
        
# Raise Exemption code
num = input("Please enter a value greater than 10 : ")
num_int = int(num)
if num_int < 10:
    raise Exception(f"Your value was less than 10.The value of num was : {num_int}")

# Raise Exemption another pattern
num = int(input("Please enter a value greater than 10 : "))

if num < 10:
    raise Exception(f"Your value was less than 10.The value of num was : {num}")

# while loop and for loop
kittens = 0

question = input("Has a kitten attempted word domination (y/n) : ")

while question == "y":
    
    kittens += 1
    
    print(f"{kittens} kittens has attempted world domination")
    
    question = input("Add another kitten? y/n ")
    
while True:
    print("My name is kellykuzzy")
    
    question = input("Do you wish to stop me? (y/n): ")
    
    if question == "y":
        print("As you wish")
        break
    
while True:
    print("I am a loop!")
    
    question = input("Would you like me to continue? (y/n): ")
    if question == "y":
        print("Back to the beginning")
        continue
    else:
        print("I shall cease")
        break
    
# for loop
for output in range(11):
    print("Why hello there.")
    
lenght = 34.90 - 23.23
round_lenght = round(lenght)
print(round_lenght)

exp = (5 + 6) * 2 
print(f"Expression is : {exp}")

name = "John Doe"
fact = "A traffic jam lasted lasted for more than 10 days, with cars only moving 0.6 miles a day."
address = "77 Winchester lane"
empty_str = " "

print(name)
print(fact)
print(address)
print(empty_str)

greeting = "Hello"
print(greeting[0] + greeting[1] + greeting[2] + greeting[3] + greeting[4])

# string indexing
very_long_word = "superwomanlization"
print(very_long_word[0:3])
print(very_long_word[0:])
print(very_long_word[:])
print(very_long_word[:10])

#concatenation

name = "Tin"
sentence = "My name is" + name
print(sentence)
print(f"my name is {name}")

age = 32
age_str = str(age)
sentence2 = "My age is " + age_str
print(sentence2)

age = 35
sentence3 = "My age is " + str(age)
print(sentence3)

sentence4 = "My name is {},i am {} years old.".format(name,age)
print(sentence4)
sentence5 = f"My name is {name}, i am {age} years old"
print(sentence5)

#manipulation of string

manip_string = "    ***Welcome$to$the$world$of$programming***    "

manip_string_strip = manip_string.strip()
print(manip_string_strip)'''

'''# while loop
i = 0

while True:
    
    if i < 10:
        print(i)
        i += 1
    
# while loop
a = 0
while a < 10:
    print(a)
    a += 1
    
sum1 = 0
i = 0
while sum1 <= 25:
    sum1 += 2
    print(sum1)
    
# while loop
start = 5
while start % 2 != 0:
    print(start)
    start += 1
    
number = int(input("Enter number less than 100: ")) # request user to enter number

while number > 100:     # while loop condition if number is greater than 100
    
    print("Please try again")  # The response from the above condition 
    
    number = int(input("Enter number less than 100: ")) # repeat the same request again 
    
if number % 2 == 0:  #if the repeated condition is even number 
    
    print(number * 2) # print the number you enter multiplied by 2
    
else:
    
    print(number * 3) # else if odd number print multiplied by 3
    

# infinte loop
i = 10
while i < 14:
    print("I can see infinity")
    
#while not loop

import random as rd

num = rd.randint(1,50) # randint means random integer from 1 to 50.
num_guess = int(input("Guess a number from 1 to 50: ")) # request user to input a number 

while num_guess != num:  # while loop condition i.e if number guess is not equal to num( random no 1 to 50)
    if num_guess < num:  # if statement asking if the guess number is less than the random number 
        num_guess = int(input("Too small! Guess another number from 1 to 50: "))
    else:
        num_guess = int(input("Too big! Guess another number from 1 to 50: "))
    print("You guessed correctly")
    
#for loop and range

for num in range(1,50):
    print(num)
    
# How to read a file in python  
# create a python text as input.txt
file = open('input.txt', 'r')

lines = file.read()

print(lines)

#how to over write file

file = open('input.txt', 'w')

file.write("Hello there")
file.close()

#how to add 
file = open('input.txt', 'a')

file.write("Hello there")
file.close()

# using while loop, input and f string 
count = 0
total = 0

num = int(input("Please enter a number : "))

while num != 0:
    count += 1
    total += num
    
    num = int(input("Please enter a number(enter 0 to stop) : "))

print(f"There were {count} numbers recorded.")
print(f"The total of all numbers is {total}")


# Create time table 

num = int(input("Please enter the desire time table value: "))

for table in range(1,13):
    print(f"loop iteration # {table}")
    times_value = num * table
    print(f"{num} times {table} is equal to : {times_value}")
    
#alternatively way of creating times table 
for x in range(1,2):
     for y in range(1,13):
         print(f"{x} * {y} = {x*y}")
print(" ")

#alternative way of creating times table
for i in range(1,13):
    for j in range(1,13):
        
        z = i * j
        print(f"{i} * {j} = {z}")

while True:
    name = input("please enter your name: ")
    
    if name != "John":
        print("You are not John,I require John.Try again")
    else:
        print("Welcome back John,everyone has missed you")

# Task 8 to print three angle 
symbol = "*"
for x in range(1,10):
    if x < 6:
        print(symbol * x)
    else:
        reduce = 10 - x
        print(reduce * symbol)'''