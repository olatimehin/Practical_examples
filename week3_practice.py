
# string handling 
word = "Hello There!"

idx = word[0:8:2] # start: end: step
print(idx) 

#remebering string
word = "Do you enjoy python yet?"
new_upper = word.upper()
new_lower = word.lower()
new_capitalize = word.capitalize()
new_strip = word.strip("?")
new_split = word.split(" ")
new_join =" ".join(word)
new_replace = word.replace(" ", " @") 
print(word)
print(new_upper)
print(new_lower)
print(new_capitalize)
print(new_strip)
print(new_split)
print(new_join)
print(new_replace)


#fromating string 
name = "John"
surname = "Python"

print("My name is {} {} and i am a throrugh enjoyer of {} \ ". format(name,surname,surname))

#alternatively
print("My name is {0} {1} and i am a thorugh enjoyer of {1}".format(name, surname))

# f string
print(f"My name is {name} {surname} and i am a thorough enjoyer of {surname}")

# format example
Value =  68.85673423

output =("Your total on your order will be : £{:.2f}".format(Value))
print(output)

# alternatively
print(output.format(Value))

# DATA STRUCTURES : LISTS & DICTIONARIES

names = ["jimmy", "Billy","Terry","Kerry", "Joe"]
for i in names:
    print(i)    # this will print the list of all the items

names = ["jimmy","Billy","Terry","Kerry","Joe"]
for i in names:
    print(names) # this will print everything together in 5 times 

# in operator and lists

names = ["jimmy", "Billy","Terry","Kerry", "Joe"]

name_one = "lucy"
name_two = "Terry"

# if statement in list
if name_two in names:
    print("i am a member")
 
#if else in list   
if name_one in names:
    print("I am a member")
else:
    print("i am not a member")

# if elif and else in list
print("Welcome here......")
if name_one in names:
    print(f"{name_one} is a member")
elif name_two in names:
    print(f"{name_two} is a member")
else:
    print("Non is a member")
    
#append in a list 
names = ["jimmy", "Billy","Terry","Kerry", "Joe"]
names.append("sally")
print(names)


#extending list
numbers = [1,2,3,4]
numbers.extend([5,6,7,8,])
print(numbers)

#inserting in a list 
numbers = [1,2,3,4,5]
numbers.insert( 2, "two")
print(numbers)

# popping from a list
numbers = [1,2,3,4,5]
popped_number = numbers.pop(2)
print(popped_number)
print(numbers)

#Dictionaries
# dictionary is similar to list but it has keys and values
# Two ways to declare dictionary 
new_dictionary = dict(name = "kitty", age = 0.5, Kitten = True)
print(new_dictionary)

# print each value of the key
new_dictionary = dict(name = "kitty", age = 0.5, Kitten = True)
print(new_dictionary["name"])
print(new_dictionary["age"])         # note we can use loop instead of writing one by one see example below 
print(new_dictionary["Kitten"])

# print all keys,values and items
new_dictionary = dict(name = "kitty", age = 0.5, Kitten = True)
print(new_dictionary.keys())
print(new_dictionary.values())    # note we can use loop instead of writing one by one see example below 
print(new_dictionary.items())

#change element of the dictionary  
new_dictionary = dict(name = "kitty", age = 0.5, Kitten = True)
new_dictionary["name"] = ("ketty")
print(new_dictionary)

# add to the dictionary
new_dictionary = dict(name = "kitty", age = 0.5, Kitten = True)
new_dictionary["class"] = ("sss 3")
print(new_dictionary)

#remove from the distionary 
new_dictionary = dict(name = "kitty", age = 0.5, Kitten = True)
remove_new_dictionary = new_dictionary.pop("age")
print(remove_new_dictionary)

#Accessing all values using for  loop through dictionary
new_dictionary = dict(name = "kitty", age = 0.5, Kitten = True)

for values in new_dictionary.values():
    print(values)

#Accessing all keys using for  loop through dictionary
new_dictionary = dict(name = "kitty", age = 0.5, Kitten = True)

for keys in new_dictionary.keys():
    print(keys)
    
#Accessing items using for  loop through dictionary
new_dictionary = dict(name = "kitty", age = 0.5, Kitten = True)

for keys,values in new_dictionary.items():
    print(keys,":", values)'''
    
'''# boolean examples
# declare a boolean 
has_drivers_license = True
has_traffic_fine = False

# booleans in if statement 
issunny = True

if issunny:
    print("it is sunny today,don't forget the sunscreen!")
    
# example 2
# this example declare a boolean that red,blue and green car were clean.
# the number of car was is 0
# the activity was not busy;
# therefore when user request input to know if a car is dirty or not, if it YES the clean car change to false 
# the number of car wash started counting to be inresed by 1 for every yes
# if the number of car was is three busy becomes true and once busy bcomes True you print the car wash is parked today
clean_red_car = True
clean_blue_car = True
clean_green_car = True
num_of_car = 0
busy = False

print("Welcome to the car wash")

redcheck = input("Is the red car dirty? (Yes/No): ").capitalize()
if redcheck == "Yes":
    clean_red_car = False
    
bluecheck = input("Is the blue car dirty? (Yes/No)").capitalize()
if bluecheck == "Yes":
    clean_blue_car = False

greencheck =  input("Is the green car dirty? (Yes/No)").capitalize()
if greencheck == "Yes":
    clean_green_car = False

if clean_red_car == False:
    print("Red car really needs a cleaning ")
    num_of_car += 1
    
if clean_blue_car == False:
    print("Blue car really needs a cleaning ")
    num_of_car += 1
    
if clean_green_car == False:
    print("Green car really needs a cleaning ")
    num_of_car += 1
    print(num_of_car)
    
if num_of_car == 3:
    busy = True

if busy == True:
    print("The car wash was packed today")'''
    
'''# Data Structures (pop and insert and treated the same way)
names = [
    "Jimmy",
    "Billy",
    "John",
    "Sally",
    "Joe",
    "Johnny"
]

popped_name = names.pop() # this will remove the last element of the list 
print(popped_name)  # 
print(names)

another_name = "Jumbo" # you can add to the list my declaring another variabl;e e.g another_name 

names.insert(0, another_name) # insert the variable declared at index 0

print(names)


add_another_name = "adekunle" # you declare another variable
names.insert(2,add_another_name) # you make the index to be 2, it there for add adekunle to index 2
print(names)

names.insert(0,"sola") # to insert to the first element of the list 
print(names)

names.pop(-1) # to remove the last element 
print(names)

#Extend in a list 
numbers = [1,2,3,4,5]
ex_number = [6,7, "yes", False, "John"]
numbers.extend(ex_number)

print(numbers)


# if statement 
names = [
    "Jimmy",
    "Billy",
    "John",
    "Sally",
    "Joe",
    "Johnny"
]

if "lucy" in names:
    print("she is as a member")
else:
    print("she is not a member")
    
    
for i in names: # loop through the element 
    print(i)
# same result with above  
for i in range(len(names)):
    print(names[i])

my_dictionary = {"name": "Terry","age":23,"is_funny": False }

popped = my_dictionary.pop("is_funny") # remove is_funny from the list 
print(popped)     # print the remove element 
print(my_dictionary) #print the rest of the element


my_dictionary["is_funny"]=popped # add the remove element back to the list 
print(my_dictionary) #print the list

reference = my_dictionary["age"] #this is referencing a particluar key

value = my_dictionary.get("name") # To get a value from a dictionary
print(value)

my_dictionary["is_cool"] = True
print(my_dictionary)

#split dictionary 
names = ["Jphn Python", "Sol Badguy","Kazuya Mishima","Terry Bogard"]
name_dictionary = {}

for i in names:
    names = i.split(" ")
    print(names)

    name = names[0]
    surname = names[1]
    print(surname)
    name_dictionary[name] = surname
print(name_dictionary)

count = 0
count = count + 1
new_sentence = ""
sentence = input("Please enter your sentence : ")

split_sentence = sentence.split() #split the sentence
print(f"list:{split_sentence}") # print the splited

sentence = "The quick brown fox"
print(sentence.find("o"))

# string manipulation 
#  example 
my_list = ['apple', 'banana', 'cherry', 'date']

for index in range(len(my_list)):
    print(f"Index: {index} {my_list[index]}") # we have two index,1 is for the for loop and second is for the list


count = 0

sentence = input("Please enter your string: ").lower()
character = input("Please enter the character you would like to count : ").lower()

for index in range(len(sentence)):
    print(f"index : {index} character : {sentence[index]}") # we have two index,1 is for the for loop and second is for the list 
    #print(f"index : {index} and {sentence[index]}")
    #print(sentence[index]) # print the index of the sentence i.e what you enter 
    if character == sentence[index]: # if the character user input is in the sentence index
        count += 1 #loop or iterate through it the number of times the character appear in the sentence 
print(f"The character : {character} appeared {count} times")


# Another way to understand better 
count = 0

sentence = input("Please enter your string: ").lower()
character = input("Please enter the character you would like to count : ").lower()

for jam in range(len(sentence)):
    print(f"iteration : {jam} character : {sentence[jam]}") #first printing 
 
    if character == sentence[jam]: 
        count += 1 
print(f"The character : {character} appeared {count} times") #second printing

# using while loop and for loop together
count = 0
while True:
    
    sentence = input("Please enter your string: ").lower()
    character = input("Please enter the character you would like to count : ").lower()
    
    if len(character)> 1:
        print("You have entered more than one character,Please try again")
        continue 
    else:
        break
    
for jam in range(len(sentence)):
    #print(f"iteration : {jam} character : {sentence[jam]}") #first printing 
 
    if character == sentence[jam]: 
        count += 1 
print(f"The character : {character} appeared {count} times") #second printing'''
