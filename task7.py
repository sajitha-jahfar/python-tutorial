# # 1. Write a program to check whether a number is positive, negative, or zero.
# num=int(input("Enter a number:\t"))
# if num==0:
#     print("number is zero")
# elif num<0:
#     print("number is negative")
# else:
#     print("number is positive")
# print("----------------------------------------------")    

# # 2. Check if a number is even or odd.
# number=int(input("Enter a number:\t"))
# if number%2==0:
#     print(number ,"is even")
# else:
#     print(number ,"is odd")
# print("-----------------------------------------------")

# # 3. Given a number, check if it is greater than 100.
# a=101
# if a>100:
#     print(a,"is greater than 100")
# else:
#     print(a,"is less than 100")
# print("-------------------------------------------------")

# # 4. Check whether a person is eligible to vote (age ≥ 18).
# age=int(input("Enter the age:\t"))
# if age>=18:
#     print("Eligible for vote")
# else:
#     print("Not eligible for vote")
# print("----------------------------------------------------")

# # 5. Given two numbers, print the greater number.
# first=5
# second=10
# if first>second:
#     print(first)
# else:
#     print(second)
# print("----------------------------------------------------")

# # 6. Given three numbers, print the largest number.
# ab=70
# bc=17
# ac=6
# if ab>bc and ab>ac:
#     print(ab,"is greater")
# elif bc>ab and bc>ac:
#     print(bc,"is greater")
# else:
#     print(ac,"is greater")
# print("---------------------------------------------------")

# # 7. Check whether a year is a leap year.
# year=int(input("Enter the year:\t"))
# if (year%4==0 and year%100!=0) or (year%400==0):
#     print("leap year")
    
# else:
#     print("not a leap year")
# print("---------------------------------------------------")

# # 8. Given a mark, print:
# # "Pass" if marks ≥ 40
# # "Fail" otherwise
# mark=80
# if mark>=40:
#     print("pass")
# else:
#     print("fail")
# print("---------------------------------------------------")

# #9. Given a mark, print grades:
# # A → ≥ 90
# # B → ≥ 75
# # C → ≥ 60
# # Fail → below 60
# score=float(input("Enter the mark\t"))
# if score>=90:
#     print("A")
# elif score>=75:
#     print("B")
# elif score>=60:
#     print("c")
# else:
#     print("fail")
# print("---------------------------------------------------")

# #10. Check if a character is a vowel or consonant.
# character=str(input("Enter the character:\t"))
# vowels=['a','e','i','o','u']
# if character in vowels:
#     print(character,"  is a vowel")
# else:
#     print(character,"  is a consonent")
# print("---------------------------------------------------")

# # 11. Print numbers from 1 to 10 but stop when number is 6.

# i=1
# for i in range(1,11):
#      if i==6:
#       break
#      print(i)
# print("---------------------------------------------------")    
    


# #12. Print numbers from 1 to 10 but skip number 5.
# i=1
# for i in range(1,11):
#      if i==5:
#       continue
#      print(i)
# print("---------------------------------------------------")

# #13. Use pass inside an if block and explain why it doesn’t cause an error.
# i=1
# if i>5:
#     pass
# else:
#     print("The pass statement in Python is a null operation; it does nothing and acts as a placeholder.\n It does not produce an error because it is a syntactically valid statement that fulfills the requirement for a statement in a given context without executing any code")
# print("---------------------------------------------------")   

# # 14. Print all even numbers between 1 and 20 .

# for i in range(1,21):
#     if i%2==0:
#         print(i)
    
# print("---------------------------------------------------")

# #15. Find the sum of numbers from 1 to 10.
# sum=0
# for i in range(1,11):
#     sum+=i
# print(sum)
# print("---------------------------------------------------")

# # #16. Check whether a given number is a multiple of both 3 and 5.
# num=int(input("Enter the number:\t"))
# if num%3==0 and num%5==0:
#     print(num ," is multiple of both 3 and 5")
# else:
#     print(num,"is not the multiple of both 3 and 5")
# print("---------------------------------------------------")

#17. Print "Hello" 5 times using a loop.
i=1
while i<=5:
    print("hello")
    i+=1
print("---------------------------------------------------")

#18. Given a list [1,2,3,4,5] , print only numbers greater than 3.
list1=[1,2,3,4,5]
i=1
for i in list1:
    if i>3:
        print(i)
print("---------------------------------------------------")

# 19. Advanced Login System
# Write a Python program to simulate a login system with the following rules:
# The correct username is "admin" and the correct password is "1234" .
# The user is allowed a maximum of 3 login attempts.
# The username comparison should be case-insensitive.
# The password comparison should be case-sensitive.
# If the user enters correct credentials within the allowed attempts, display
# Login successful .
# If all attempts are used without success, display
# Account locked .
# After each failed attempt, display the number of attempts remaining.
correct_uname="admin"
correct_password="1234"
max_attempts=3
for attempts in range(1,max_attempts+1):
    username=input("Enter the username\t")
    password=input("Enter the password\t")
    if username.lower()==correct_uname and password==correct_password:
        print("Login Successful")
        break
    else:
        remaining_attempts=max_attempts-attempts
        if remaining_attempts>0:
            print(f"Incorrect credentials.Attempts remaining:{remaining_attempts}")
        else:
            print("Account Locked")
print("---------------------------------------------------")

# 20. Enhanced Traffic Light Controller
# Write a Python program that acts as a traffic light controller with the following
# conditions:
# The program should accept either a color or a number as input.
# Use the mapping:
# 1 or "red" → Stop and wait for 60 seconds
# 2 or "yellow" → Ready and wait for 5 seconds
# 3 or "green" → Go and drive safely
# The program should handle inputs in a case-insensitive manner.
# If the input does not match any valid color or number, display
# Invalid Signal.
signal=input("Enter traffic signal(color or number):")
signal=signal.lower()
if signal=="red" or signal=="1":
    print("Stop and wait for 60 seconds")
elif signal=="yellow" or signal=="2":
    print("ready and wait for 5 seconds")
elif signal=="green" or signal=="3":
    print("Go and drive safely")
else:
    print("Invalid Signal")
print("---------------------------------------------------")

    # LIST COMPREHENSION QUESTIONS
# 1. Given a list of numbers, write a program to find the sum of all numbers, the
# sum of even numbers, and the sum of odd numbers using list
# comprehension.

list2=[1,3,5,6,4]
total_sum=sum([x for x in list2])
even_sum=sum([x for x in list2 if x%2==0])
odd_sum=sum([x for x in list2 if x%2!=0])
print("sum of all numbers:",total_sum)
print("sum of odd numbers:",odd_sum)
print("sum of even numbers:",even_sum)
print("---------------------------------------------------")

# 2. Given a list of numbers, create a new list that contains only numbers
#greater than 10 and divisible by 3 using list comprehension.
list3=[5,6,15,18,20,24,25,30]
new_list=[x for x in list3 if x>10 and x%3==0]
print(new_list)
print("---------------------------------------------------")

#  3. Given a list of numbers, create a new list containing only even numbers
# greater than 10 using list comprehension.
list4=[5,3,8,12,24,15,18]
even_list=[x for x in list4 if x>10 and x%2==0]
print(even_list)
print("---------------------------------------------------")

# 4. Given a list of strings, create a new list containing the length of each string
# using list comprehension.
fruits=['apple','banana','orange','lichi']
fruits_length=[len(x) for x in fruits]
print(fruits_length)
print("---------------------------------------------------")

# 5. Given a list of numbers, create a new list where:
# even numbers are replaced with "even"
# odd numbers are replaced with "odd"
list7=[2,7,9,33,56,20]  
list_new=["odd" if x%2!=0 else "even" for x in list7]
print(list_new)    
print("---------------------------------------------------")

