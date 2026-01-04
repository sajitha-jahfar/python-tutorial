#1. Create a list [1,2,3] and add 4 to the end using a list method.
lst=[1,2,3]
lst.insert(3,4)
print(lst)

#2. Given [10,20,30] , remove 20 using a list method.
lst1=[10,20,30]
lst1.remove(20)
print(lst1)

#3. From [5,3,9,1] , sort the list in ascending order using a list method.
ab=[5,3,9,1]
ab.sort()
print(ab)

#4. From [1,2,3,4,5] , extract [2,3,4] using slicing only.
n=[1,2,3,4,5]
print(n[1:4])

#5. Reverse the list [1,2,3,4] using slicing (no loops).
lst3=[1,2,3,4]
print(lst3[::-1])

#6. Combine [1,2] and [3,4] into one list using list operations.
abc=[1,2]
bc=[3,4]
ac=abc+bc
print(ac)

#7. Convert [7,8] into [7,8,7,8] using list operations.
v=[7,8]
v=v+v
print(v)

#8. Check if 3 exists in [1,2,3,4] using a list operator.
mn=[1,2,3,4]
c=3 in mn
print(c)

#9. Count how many times 2 appears in [1,2,2,3,2] using a list method.
g=[1,2,2,3,2]
print(g.count(2))

#10. Remove the last element from ["a","b","c","d"] using a list method.
df=["a","b","c","d"]
df.pop()
print(df)

#11. Insert "x" at index 1 in ["a","b","c"] using a list method.
k=["a","b","c"]
k.insert(1,"x")
print(k)

#12. Replace the element at index 2 in [10,20,30,40] with 99 using indexing.
bn=[10,20,30,40]
bn[2]=99
print(bn)

#13. Convert range(5) into a list using list functions.
xx=range(5)
xy=list(xx)
print(xy)

#14. Using slicing, extract every 2nd element from [1,2,3,4,5,6] → expected [2,4,6] .
jk=[1,2,3,4,5,6]
print(jk[1:7:2])

#15. Remove all elements from [1,2,3] using one list method.
bb=[1,2,3]
del bb
# print(bb)

#16. Copy a list [4,5,6] using only list tools (no modules).
fg=[4,5,6]
zz=fg.copy()
print(zz)

#17. Convert [1,2,3] into a nested list [[1,2,3]] using list operations.
list9=[1,2,3]
nested=[list9]
print(nested)

#18. Extend [1,2] with [3,4,5] using a list method.
hj=[1,2]
ijk=[3,4,5]
hj.extend(ijk)
print(hj)

#19. Using list repetition, create a list ["hello","hello","hello"] .
e=["hello"]
repeated_list=e*3
print(repeated_list)

#20. Remove the element at index 2 from [10,20,30,40] using a list method.
s=[10,20,30,40]
s.pop(2)
print(s)























