# 2) Write a program to generate the
# following number pyramid for a given
# integer n:
# Input Format:
# Enter the number of rows: 5
# n=int(input("enter the no of rows:"))

# for i in range(n):
#     for j in range(i+1):
#      print(" ",end="")
#     for i in range(1,n-i+1):
#      print(i,end=" ")
#     print()

# 1) Write a program that:
# 1. Finds the largest element in an
# array.
# 2. Finds the smallest element in
# an array.
# 3. Calculates the sum of all
# elements in the array.
# 4. Prints only the even numbers
# from the array.
# 5. Prints only the odd numbers
# from the array.
# 6. Counts the number of odd and
# even numbers in the array.
# 7. Calculates the sum of odd
# numbers in the array.
# 8. Calculates the sum of even
# numbers in the array.
n=int(input("Enter the size of the array:"))
a=[]
print("enter the array elements:")
for i in range(n):
    element=int(input())
    a.append(element)
print("array elements are:")
for i in range(n):
 print(a[i],end=" ")
even_number=[]
odd_number=[]
even_sum=0
odd_sum=0
for num in a:
    if num%2==0:
        even_number.append(num)
        even_sum+=num
    else:
        odd_number.append(num)
        odd_sum+=num
print(f"Largest element:",max(a))
print(f"Smallest element:",min(a))
print(f"Sum of all elements:",sum(a))
print(f"even numbers:",even_number)
print(f"odd numbers:",odd_number)
print(f"count of even numbers:",len(even_number))
print(f"count of odd numbers:",len(odd_number))
print(f"sum of even number:",sum(even_number))
print(f"sum of odd numbers:",sum(odd_number))


    
    
    