
#Task 1:Given a positive integer n:
# ● If 1 ≤ n ≤ 9, print its lowercase English word (one to nine).
# ● If n > 9, print Greater than 9.
n=int(input("enter a number:"))
list1=['1','2','3','4','5','6','7','8','9']
list2=["one","two","three","four","five","six","seven","eight","nine"]
if n>=1 and n<=9:
    print(list2[n-1])
else:
    print("greater than 9")

#     Task 2:Given a positive integer N, print numbers from 1 to N with the
# following rules:
# ● If the number is divisible by 3, print Fizz
# ● If the number is divisible by 5, print Buzz
# ● If the number is divisible by both 3 and 5, print FizzBuzz
# ● Otherwise, print the number itself

n=int(input("Enter a positive integer:"))
for i in range(1,n+1):
  if i%3==0:
    print("fizz")
  elif i%5==0:
    print("Buzz")
  elif i%3==0 and i%5==0:
    print("FizzBuzz")
  else:
    print(i)
