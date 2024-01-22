# STRING PRACTICE

'''print("Hello World")

# name = input("Please enter your name : ")

# print(f"My name is : {name}")
# Python_is_cool = 100

#another_variable = "python_is_cool"

#print(another_variable)

# concatenation

name = "peter"
surname = "Parker"
full_name = name + " " + surname 
print(full_name)

len_full_name = len(full_name)
print(len_full_name)

lower_full_name = full_name.lower()
upper_full_name = full_name.upper()
capitalize_full_name = full_name.capitalize()
print(lower_full_name)
print(upper_full_name)
print(capitalize_full_name)

# strip string

message = "***The!is!my!boy***"
strip_message = message.strip("*")
print(strip_message)

#split string
split_message = message.split("!")
print(split_message)

#replace
replace_message = message.replace("!", " ")
print(replace_message)

# join string
list_example = ["The","is","my","boy"]
join_message = " ".join(list_example)
print(join_message)

#indexing string
string = "Hello"
idx_string = string[0:3]
print(idx_string)

#escape character
escape = ("ade is a boy.\n He stay in london.\t his father is my frd")
print(escape)

# Numbers in Python 
num1 = 6 
num2 = 6.5
num3 = "6"
print(type(num1))
print(type(num2))
print(type(num3))

#casting data type
float_num1 = float(num1)
str_num2 = str(num2)
int_num3 = int(num3)

print(float_num1)
print(str_num2)
print(int_num3)

# Booleans
while True:
    user_num = int(input("Please enter the user number : "))
    if user_num == 0:
        print("Enter another number more than zero : ")
        continue
    elif user_num <= 10:
        print("The number you enter is lessthan 10: ")
    elif user_num >=11 and user_num <= 20:
        print("You are within 11 to 20 : ")
    else:
        print("The number is above 20")
        
# Nested if statement
grade = int(input("Enter your grade : ")) 
if grade > 50:
    if grade > 75:
        print("You have passed : ")
    else:
        print("You have passed, but you can do better : ")
else:
    print("You failed!")
    
    
if 10 < 50 and 500 > 100:
    print("This is conjunction")
else:
    print("This is not a conjunction")
    
if 10 < 50 or 500 > 100:
    print("This is disjunction")
else:
    print("This is not a disjunction")
if not 100 < 500:
    print("This is negation")
else:
    print("Not negation")'''
    
#PROJECTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
'''Certainly! Here's a description of the provided code in plain words:

Username Input:

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

# using the Not operator
username = input("Enter your username : ")

if not username:
    print("Username name invalid.Please enter a valid username.")
else:
    print(f"Welcome {username}")
    
# create a program that gets a user's age and determines if they are eligible for a discount

age = int(input("Please enter your age (as a whole number): "))

is_member = input("Are you a member of our reward programs? yes/no: ").lower()

# check if user is a member and storing the appropriate boolean 
if is_member == "yes":
    is_member = True
else:
    is_member = False
    
# initialising the discount variable
    
discount = 0.0

if age >= 60:
    discount = 0.2
    
    if is_member:
        discount += 0.1
        
#converting discount to a percentage
discount_per = discount * 100
rounded_discount = round(discount_per, 2)

print(f"Your discount percentage will be {rounded_discount}%")

#Eligibility for discounts
senior = discount > 0

#Recommending reward program to eligible senior citizens
if senior and not is_member:
    print("Join our rewards program for additional discounts!")