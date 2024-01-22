name = "Pieter"
surname = "Parker"

full_name = name + " " + surname
print(full_name)

message = "batman"
message_len = len(message)
print(message_len)

message = "Python is Fun"
new_message = message.upper()
print(new_message)

message = "Python is Fun"
new_message = message.lower()
print(new_message)

message = "***bat*man****"

new_message = message.strip("*")
print(new_message)

reference = "The-king-of-iron-fist"
new_ref = reference.split("-")
print(new_ref)

final_ref= " ".join(new_ref)
print(final_ref)

message = "Hey!you!over!there"
message_replace = message.replace("!"," ")
print(message_replace)

string = "Hello world"
print(len(string))
idx = string[0:8]
print(idx)
