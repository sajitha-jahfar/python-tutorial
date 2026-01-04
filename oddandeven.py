odd=[]
even=[]
squareodd=[]
squareeven=[]
for i in range(1,11):
    if i%2==0:
       even.append(i)
       squareeven.append(i**2)
       

    else:
      odd.append(i)
      squareodd.append(i**2)

print("odd numbers are:",odd)
print("even numbers are:",even)
print("even numbers square are:",squareeven)
print("odd numbers square are:",squareodd)

comprehensive list
a=[x**2 for x in range(1,11)]
print(a)

