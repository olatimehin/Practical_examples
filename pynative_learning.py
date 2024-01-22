# function in python 
# two types of function
# 1 built function such as range(),id(),type(),input(), eval()
# 2 user definde function
# example of a python range(start,end integer)

'''for i in range(1,10):
    print(i) 

for x in range(1,15):
    print(x, end = " ") # it will print straight 
# user defind function
# create a function using def
# pass the number of parameter
# defined the function body with a block of code
#def function_name(parameter1, parameter2):
    #function body
    # write some action
    #return value

def add(num1, num2):
    
    print("Number 1 :", num1)
    print("Number 2 :", num2)
    addition = num1 + num2
    return addition 

res = add(2, 5)
print("The sum is :", res)'''

# creating a function without parameter
def message():
    print("My message is cooking")
message()

# creating a function with parameter
def course_func(name, course_name):
    print("Hello", name, "Welcome to pynative")
    print("Your course name is", course_name)
course_func("John", "Python")

# creating a function with parameters and return value
def calculation(a, b):
    add = a + b
    return add
res = calculation(4,5)
print("The calculation is :", res)

# calling a function
def even_odd(n):
    if n % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
even_odd(21)