# File, Module, Exception
# Questions
# FILE HANDLING QUESTIONS
# 1. Write a program to create a file named data.txt and write the text
# "Hello File Handling" into it.

file = open("data.txt","w")
file.write("Hello File Handling ")
file.close()

# 2. Write a program to read the contents of a file data.txt and display it on the
# screen.

file = open("data.txt","r")
print(file.read())
file.close()

# 3. Write a program to append the text "Python is awesome" to an existing file.


file = open("data.txt", "a")
file.write("\n Python is awesome")
file.close()

# 4. Write a program to count the number of lines present in a file.

f = open("data.txt", "r")
lines = f.readlines()
print("Number of lines:", len(lines))
f.close()

# 5. Write a program to count the number of words in a file.

f = open("data.txt", "r")
content = f.read()
words = content.split()
print("Number of words:", len(words))
f.close()

# 6. Write a program to copy the contents of one file into another file.

f1 = open("data.txt", "r")
f2 = open("files.txt", "w")
f2.write(f1.read())
f1.close()
f2.close()

# 7. Write a program to read a file and print only the lines that contain the word
# "Python" .

f = open("data.txt", "r")
for line in f:
    if "Python" in line:
        print(line)
f.close()

# 8. Write a program that reads numbers from a file and calculates their sum.

f = open("numbers.txt", "r")
total = 0
for num in f:
    total += int(num)
print("Sum:", total)
f.close()

# ERROR HANDLING (EXCEPTION
# HANDLING) QUESTIONS
# 9. Write a program to handle a ValueError when the user enters invalid input (for
# example, entering letters instead of a number).

try:
    n = int(input("Enter a number: "))
    print(n)
except ValueError:
    print("Invalid input! Please enter a number.")

# 10. Write a program to handle invalid input (user enters a string instead of a
# number).

try:
    n = int(input("Enter number: "))
    print(n)
except:
    print("Error: Enter numbers only")



# 11. Write a program that handles file not found error while opening a file.

try:
    f = open("abc.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("File not found")

# 12. Write a program using try , except , and else blocks.
# 
try:
    a = int(input("Enter a number: "))
    print(a)
except ValueError:
    print("Invalid input")
else:
    print("No error occurred")

# 13. Write a program using try , except , and finally to ensure a message
# "Program ended" is always printed.

try:
    x = int(input("Enter number: "))
    print(x)
except:
    print("Error occurred")
finally:
    print("Program ended")


# 14. Write a program that catches multiple exceptions using multiple except
# blocks.

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(a / b)
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero")

# 15. Write a program that raises a custom error when the user enters a negative
# number.

num = int(input("Enter a number: "))
if num < 0:
    raise ValueError("Negative numbers are not allowed")
else:
    print("Valid number")

# MODULES & LIBRARIES (BUILT-IN + USERDEFINED)

# 🔹 Built-in ( math only)
# 16. Write a program that uses the math module to find the square root of a number.

import math
num = int(input("Enter number: "))
print(math.sqrt(num))


# 17. Write a program that uses the math module to calculate power of a number.

import math
print(math.pow(2, 3))

# 18. Write a program that uses the math module to find the factorial of a number.

import math
print(math.factorial(5))

# 🔹 User-Defined Modules
# 19. Create a user-defined module named calculator.py that contains functionsfor addition, subtraction, multiplication, and division.
# Import and use this module in another Python file.

import calculator
print(calculator.add(10, 5))


# 20. Create a user-defined module that contains a function to check whether a
# number is even or odd, and use it in another program.

import evenoddmodule
evenoddmodule.evenorodd(5)

# 21. Create a user-defined module with a function that returns the area of a circle,and import it in another file.

import areaofcircle
print(areaofcircle.area(3))