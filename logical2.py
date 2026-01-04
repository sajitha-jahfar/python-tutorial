

# 1.Create a program to find the maximum and minimum of two numbers without using any loops or
# conditional statements.
# Rules / Constraints
#  ❌Do not use loops (for, while, do-while)
#  ❌Do not use conditional statements (if, else, switch)
#  ❌Do not use the ternary operator (? :)
#  ❌Do not use built-in functions such as max() or min()
#  ✅You may use only the absolute value operation provided by the language
# (e.g., abs(), Math.abs(), or .abs())
#  ❌Do not use any other built-in utility functions
# Input
#  Two numbers
# Output
#  Print the maximum value
#  Print the minimum value

x=int(input("Enter the first number:"))
y=int(input("Enter the second number:"))
max=((x+y)+abs(x-y))//2
min=((x+y)-abs(x-y))//2

print("minimum is",min)
print("maximum is",max)
# 2.Write a program to check whether two numbers are equal without using comparison operators.
# Rule:
# ❌Do not use == or any other comparison operator

a=int(input("enter first number:"))
b=int(input("enter the second number:"))
c=abs(a-b)
if not (c):
    print("numbers are equal")
else:
    print("numbers are not equal")
