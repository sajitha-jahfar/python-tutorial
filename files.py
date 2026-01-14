file = open("files.txt", "r") 
print(file.read())
# file.close()

# file = open("files.txt", "r")
# line1 = file.readline()
# print(line1)
# file.close()

# file = open("files.txt", "r")
# lines = file.readlines()
# print(lines)
# file.close()

# file = open("files.txt", "w")
# file.write("Hello, World!")
# file.close()

# file = open("files.txt", "w")
# lines = ["Hello\n", "good morning\n"]
# file.writelines(lines)
# file.close()

# file = open("files.txt", "a")
# file.write("Appended text.\n")
# file.close()

#using with statement 
# with open("files.txt", "r") as file:
# content = file.read()
# print(content)

# position = file.tell()
# print(position)

# try:
#  file = open("file.txt", "r")
#  content = file.read()
# except FileNotFoundError:
#  print("File not found!")
# finally:
#  file.close()

#raise exception
 
# x=-5
# if x<0:
#     raise Exception("negative numbers not allowed")

class NegativeNumberError(Exception):
 pass
def check_number(num):
 if num < 0:
 raise NegativeNumberError("Negative numbers are not allowed!")

try:
 check_number(-10)
except NegativeNumberError as e:
 print(e)
