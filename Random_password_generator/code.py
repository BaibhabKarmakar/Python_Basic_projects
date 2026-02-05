import random
import string

# value = random.choice([1 , 2 , 3])
# print(value)

# print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation)
password_len = int(input("What will be the length of the password : "))
charValues = string.ascii_letters + string.digits + string.punctuation
password = ""

# List Comprehension : 

password = "".join([random.choice(charValues) for i in range(password_len)])

# Normal Loop Method : 

# for i in range(password_len):
#     password += random.choice(charValues)
print(f"Your random password is : {password}")