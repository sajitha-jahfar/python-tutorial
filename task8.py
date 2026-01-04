# 1. Write a function that takes a number as input and returns whether the
# number is even or odd.

# a=int(input("Enter a number:\t"))
# def typenumber():
#     if a%2==0:
#         print("Even number")
#     else:
#         print("odd number")  
# typenumber()       

# # 2. Write a function that takes three numbers as input and returns the largest
# # number among them.

# a=int(input("enter the first number\t"))
# b=int(input("enter the second number\t"))
# c=int(input("enter the third number\t"))
# def largest():
#     if a>b and a>c:
#         print(a," is greater")
#     elif b>a and b>c:
#         print(b ,"is greater")
#     else:
#         print(c,"is greater")
# largest()

# # 3. Write a function that takes a list of numbers as input and returns the sum of
# # all elements in the list.

# def sum_arguments(*arg):
#     total=0
    
#     for i in arg:
#         total+=i
#     return total
    
# print(sum_arguments(1,2,3,55,6,7))

# # 4. Write a function that takes a list of numbers as input and returns a new list
# # containing only even numbers.

# def even_numbers(numbers):
#     even_list=[]
#     for n in numbers:
#         if n%2==0:
#             even_list.append(n)
#     return even_list
# print("Even numbers:")
# print(even_numbers([1,2,3,4,5,6]))

# # 5. Write a function that takes a string as input and returns the length of the
# # string.

# def str_length(s):
#     return len(s)
# print("length of string:",str_length("sajitha"))

# # 6. Write a function that takes a string as input and returns the string in
# # uppercase.

# def convtoupper(s):
#     return s.upper()
# print("uppercase string is:",convtoupper("python"))

# # 7. Write a function that takes a number as input and returns whether the
# # number is positive, negative, or zero.

# def numbercheck(n):
#     if n>0:
#         return "positive"
#     elif n<0:
#         return "negative"
#     else:
#         return "zero"
# print("the numberis",numbercheck(6))

# # 8. Write a function that takes a number as input and returns True if the number
# # is a multiple of both 3 and 5, otherwise returns False .

# def mul_of3and5(n):
#     if n%3==0 and n%5==0:
#         return " multiple of both 3 and 5"
#     else:
#         return "not a multiple of both 3 and 5"
# print("the number is",mul_of3and5(8))

# # 9. Write a function that takes a list of numbers as input and returns the
# # maximum value in the list.

# def max_number(numbers):
#     return max(numbers)
# print("maximum value is",max_number([4,89,7,60]))

# # 10. Write a function that takes marks as input and returns the grade 
# # to the following rules:
# # A for marks ≥ 90
# # B for marks ≥ 75
# # C for marks ≥ 60
# # Fail for marks below 60

# def grade(n):
#     if n>=90:
#         return "A"
#     elif n>=75:
#         return "B"
#     elif n>=60:
#         return "C"
#     else:
#         return "fail"
# print("Grade is",grade(75))

# # 11. Write a function that takes a price as input and returns the discounted
# # price after applying a 10% discount.

# def discount_price(price):
#     discount=price*0.10
#     return price-discount
# print("discounted price is",discount_price(1000))

# # 12. Write a function that takes a list of numbers as input and returns the count
# # of even and odd numbers.

# def countofnumbers(numbers):
#     even=0
#     odd=0
#     for n in numbers:
#         if n%2==0:
#             even+=1
#         else:
#             odd+=1
#     return even,odd
# odd,even=countofnumbers([1,2,3,4,5,6])
   
# print("count of even numberis",even)
# print("count of odd numberis",odd)
    
# # 13. Write a function that takes a temperature in Celsius as input and returns
# # the temperature in Fahrenheit.

# def c_to_f(celcious):
#     return (celcious*9/5)+32
# print("temperature in fahrenheit:",c_to_f(38))

num=int(input("Enter a number:"))
def factorial(n):
    factorial=1
    if n<=0:
        return
    else:

        for i in range(1,n+1):
          factorial=factorial*i 
    
        return factorial
   
print(factorial(num))
    