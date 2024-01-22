'''#input functions
val = input("Please enter your name: ")
print(val)
print(f"my name is {val}")
print("my name is {}".format(val))

#printing type of input value
num = input("Please enter your age: ") # input always come out as a string 
print(num,type(num)) 

#change input data type by casting
num1 = int(input("How old are you: \n"))
print(num1,type(num1))

#taking mutilple input at a time using split() method
#example is input().split(seperator,maxslpit)
Taking two inputs at a time 
x, y = input("Enter two values: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)
print(x, "Number of boy")
print(y, "number of girls")

#a , b = input("Please enter two values: ").split()
#print(f"first value is {a} and second values is {b}")

#taking mutiple input at a time and type casting them
x = list(map(int,input("Enter multiple values: ").split()))
print("list of students:", x)
print(x)

#Taking multiple input using LIST COMPREHENSION
# taking two multiple input at a time 
x, y = [int(x) for x in input("Enter two values: ").split() ]
print("First number is :", x)
print("Second number is : ", y)

#taking three multiple input at a time
x,y,z = [int(x) for x in input("Enter three values: ").split()]
print(x, "numbers")
print(y, "numbers")
print(z, "Numbers")
print("first number is {},second number is {} and finally the last number is {}".format(x,y,z))

#output of print () function
name = "johnson"
age = 23
print("Name is:", name)
print("Age is:",age)

#concatenate output
name = "Alice"
age = 25
print("Hello,my name is", name)
print("Hello my age is", age)
print("Hello,my name is", name, "and i am", age, "years old")

#print concetenated string 
print("Greeksforgreeks is a wonderful " + "websites")
#output formating 
a ,b = 10,1000
print("The value of a is {} and the value of b is {}".format(a,b))

#python input
n = input("Enter the numbers:")
print("Number entered by users", n)
print(type(n))

#seperate parameter in print
a = 12
b = 12
c = 2023
print(a,b,c, sep="-")

#print without newline in python 3.x ''''''1
print("geeks", end=" ")
print("geeksforgeeks")  # the two print join together AND IT WILL BE ON A STRIAGHT LINE 

# array
A = [1,2,3,4,5]
# printing A element in same line
for i in range(5):
    print(A[i], end = " ") #THE PRINT WILL BE ON A STRIGHT LINE INSTEAD OF VERTICALLY LISTED
 
 #OR 
for x in A:
    print(x, end=" ")
    
#Print without newline and without using for loop like the above...............2

B =  [1,2,3,4,5]
#using * asterisk to print the list in a single line
print(*B) 

#print without newline using python sys module...................3
import sys

sys.stdout.write("Geeksfor Geeks")
sys.stdout.write("Is best websites for coding!")

# python end parameter in print()
#end the output with a space
print("Welcome to", end = " ")
print("Geeks for Geeks", end =" ")

#end the output with "@"
print("Python", end = "@")
print("Geeks for Geeks")

#using end to concetenate strings
name = "Alice"
age = 30

print("Hello,my name is", name, "and i am", age, "years old", end = "")
print("Nice to meet you")

#using question mark to concatenate them
print("Hello,my name is", name, "and i am", age, "years old", end = "?")
print("Nice to meet you")
#sep parameter in print()
print("G","F","G", sep = "")
print("09","12","2023", sep="-")
print("olatimehin", "igbekele", sep="@")
print("olatimehin", "igbekele", sep=" ")

#TOPIC 2 PYTHON OPERATORS
# types of operator
# 1. there are 6 Arithmetic operators in python
# + 
# -
# *
# /
# ** exponential i.e raise  to power
# % modulus i.e reminder after division 

# 2.  Comparison operators 
# >
# <
# ==
# !=
# >=
# <=

# 3  logical operators
# and conjunction i.e it is True only fi the two condition are correct
# or disjunction i.e it is True if beither of the two conditions are correct
# not it is True if the operant are false.Note operand is the value to which the operator is assigned 

# 4 assignment operator
# =
# +=
# -=
# *=
# /=
# **=
# %=

# PYTHON DATA TYPES
# 1 NUMERICAL DATA TYPES INCLUDES
# 1. Integers= it is a digit 
# 2. float = it seperated by decimal
# 3. complex number = it is classified as real part and imaginary part e.g -2 + 3j

a = 5
print("Type of a: ", type(a)) 
b = 4.0
print("Type of b:", type(b))
c = 2 + 3j
print("Type of c:",type(c))

# 2. SEQUENCE DATA TYPES INCLUDES 
# 1. string = it is denoted by quotes

# 2. List = this is declare using square bracket.it can be combination of data types.it can be modified.it is mutable
  
# 3.Tuple =it is like list but it is immutable.it declare using bracket 

# the same way we manipulate in string,list and turple index using square bracket

# 3. BOOLEAN DATA TYPES 
A = True
B = False
print(type(A))
print(type(B))

#4 . SET DATA TYPES 
# Set is created using curly braces and put a sequence of element seperated by comma. the same element of set will come out as 1
set1 = set([1,2,3,4,5,6])
print(set1)

# 5 DICTIONARY DATA TYPES
dict = {1:"greeks","name":"for",3:"Greeks"}
print(dict)

# exercise
# declaring a list
L = [1, "a", "string", 1+2]
print(L)
# Adding an element in the list
L.append(6)
print(L)
#Deleting last element from a list
L.pop()
print(L)
#Displaying second element  of the list
print(L[1])

# declaring 
tup = (1, "a", "string", 1+2)
print(tup)
print(tup[1])

#iterations in python 
i = 1
while (1 < 10):
    print(i)
    i += 1'''
    
import math as m
x = m.sqrt(64.55)
print(x)
 # create a function 
my_list = [5,6,7,8,9]

def substraction(list):
    total = list.pop(0)
    print(total)
    
    for value in list:
        print(value)
        
        total -= value 
    return total 
sub_list = substraction(my_list)
print(sub_list)