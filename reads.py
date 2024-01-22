'''is_raining = False
if is_raining == True:
    print("print a coat with you")
else:
    print("dont border to bring anything")
 
while True:
        
    user_num = int(input("Please enter a number: "))

    if user_num == 0:
        
        print("put another number than zero")
        continue
    elif user_num < 10:
        print("It is a small number")
        continue
    elif user_num > 10 and user_num < 20:
        print("It is a range")
        continue
    else:
        print("It is a bigger number")
        continue'''
#nested     

'''grade = int(input("Please enter your grade: "))

    
if grade > 50:
    
    if grade > 75:
        
        print("you passed")
        
    else:
            
        print("You passed but you could improved")
else:
    print("you would need to rewrite")
        
# Numerical string
# to write a statemnet to include name,school and age
print("This is the first sentence. \n This is another sentence.")

name = input("Enter your name: ")
name = name.lower()
school = input("Please enter the name of your school: ")
school = school.capitalize()
print(f"My name is: {name},I school in {school} united kingdom")

age = int(input("Please enter your age: "))
current_year =  2023
year_turn_100 = current_year + (100 - age)

# year_turn_100 =str(year_turn_100)
#print("Hey,my name is" + name + " I schooled in " + school + "i will be 100 years old in" + year_turn_100  )
print(f"Hey,my name is {name},I schooled in {school},i will be 100 years old in {year_turn_100}")

# write a code to count the number of sunny in a sentence
sentence = "Sunny days are the best,I am always in the best mood when it is sunny.If you ask me what the best weather is,I will say SUNNY "
new_sentence = sentence.lower()
count_sunny = new_sentence.count("sunny")
print(count_sunny)

#implicit casting 
x = 5
y = 2.0
sum = x + y
sum = int(sum)
print(sum)

#explicit casting 
num = "45"
num_int = int(num) 
print(num_int)

import math as m

my_float = 2.548966251

floor = m.floor(my_float) # rounding down
ceiling = m.ceil(my_float) #rounding up

print(floor)
print(ceiling)

#Absolute value
age = -45
abs_age = abs(age)  #absolute

print(abs_age)

# round up to 2 decimal places 
rounding = round(my_float, 2)
print(rounding)

# To increase value 

x = 5
x = x + 1
print(x)

x = 6
x += 2
print(x)'''

'''Username Input:

The program begins by prompting the user to enter their username using the input function.
It checks if the entered username is not empty. If the username is empty, it prints an error message indicating that the username is invalid. Otherwise, it prints a welcome message including the entered username.

Age and Discount Eligibility:

The program then prompts the user to enter their age as a whole number using the input function, and it converts the input to an integer.
The user is asked whether they are a member of the reward programs by inputting 'yes' or 'no'. The input is converted to lowercase for case-insensitive comparison.
The program checks if the user is a member and stores the result in the is_member variable.

Discount Calculation:

The program initializes the discount variable to 0.0.
If the user's age is 60 or more, a discount of 20% is applied.
If the user is a reward program member, an additional 10% discount is applied.
The calculated discount percentage is then printed, rounded to two decimal places.

Eligibility and Recommendation for Reward Program:

The program determines if the user is a senior citizen eligible for a discount by checking if the discount is greater than 0.
If the user is a senior citizen but not a reward program member, it recommends joining the rewards program for additional discounts.
In summary, the code takes user inputs for username, age, and reward program membership, calculates a discount based on age and membership, and provides information and recommendations regarding discounts and joining the reward program.
'''

# Request a user input to enter username,if the user didn't enter anything reply invalid username
username =  input("Please enter your username: ")
 
if not username:
     print("Invalid username,please enter your username.")
else:
    print(f"Welcome {username}")
    
# Request the user to enter age as a whole number using input function and convert to integer
# create a variable is member and input whether they are a member of a reward program by inputting yes or no and covert to lower
age = int(input("Please enter your age: "))

is_member = input("Are you a member of our reward system? yes/no: ").lower()
if is_member == "yes":
    is_member = True
else:
    is_member = False

#The program initializes the discount variable to 0.0.
#If the user's age is 60 or more, a discount of 20% is applied.
#If the user is a reward program member, an additional 10% discount is applied.
#The calculated discount percentage is then printed, rounded to two decimal places.

# create a variable discount    
discount = 0.0

if age >= 60:
    discount = 0.2
    
    if is_member:
        discount += 0.1
#convert discount to a percentage rounding to 2 decimal places

per_discount = discount * 100
rounded_discount = round(per_discount, 2)
print(rounded_discount)
print(f"Your discount percentage will be {rounded_discount}%")

#eligibility for discount
senior = discount > 0

#Recommending rewards programs to eligible senior citizen 

if senior and not is_member:
    print(f"join our rewards program for additional discounts")