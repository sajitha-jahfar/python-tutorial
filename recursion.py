# def fact(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return  n*fact(n-1) 
# print(fact(5))

#tail recursion
#tail factorial
def tailfactorial(n,accumalator=1):
    if n==0 or n==1:
        return accumalator
    else:
        return tailfactorial(n-1,accumalator*n) 
print(tailfactorial(5))
