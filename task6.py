# Set QUESTIONS
# 1. Create a set with values {1, 2, 3, 4} .

s={1,2,3,4}
print(s)

# 2. Add the value 5 to the set {1, 2, 3, 4} using a set method.
s={1,2,3,4}
s.add(5)
print(s)

# 3. Remove the value 3 from the set {1, 2, 3, 4} using a set method.
s={1,2,3,4}
s.remove(3)
print(s)

# 4. Check if 2 exists in the set {1, 2, 3, 4} .
s={1,2,3,4}
print(2 in s)

# 5. Convert the list [1, 2, 2, 3, 4, 4] into a set to remove duplicates.

list1= [1, 2, 2, 3, 4, 4]
set1=(set(list1))
print(set1)

# 6. Convert the tuple (10, 20, 30) into a set.

tuple1=(10, 20, 30) 
newset=(set(tuple1))
print(newset)

# 7. Find the union of sets {1, 2, 3} and {3, 4, 5} .

a={1, 2, 3} 
b={3, 4, 5}
union_set=(a.union(b))
print(union_set)

# 8. Find the intersection of sets {1, 2, 3} and {1, 2, 3}.

c={1, 2, 3}
d={1, 2, 3}
intersection_set=(c.intersection(d))
print(intersection_set)

# 9. Find the difference between sets {1, 2, 3, 4} and {3, 4} .

e={1, 2, 3, 4}
f={3,4}
difference_set=(e.difference(f))
print(difference_set)

# 10. Create a copy of the set {5, 6, 7} using a set method.

x={5, 6, 7} 
y=x.copy()
print(y)

# 11. Remove all elements from the set {1, 2, 3} using one set method.

m={1, 2, 3}
n=m.clear()
print(n)

# 12. Check whether {1, 2} is a subset of {1, 2, 3} .

ab={1,2,3}
bc={1,2}
result=(bc.issubset(ab))
print(result)

# 13. Check whether {1, 2, 3} is a superset of {1, 2} .

u={1,2,3}
v={1,2}
result2=(u.issuperset(v))
print(result2)

# 14. Find the symmetric difference between {1, 2, 3} and {3, 4, 5} .

i={1,2,3}
j={3,4,5}
result3=(j.symmetric_difference(i))
print(result3)

# 15. Add multiple elements {8, 9, 10} into {1, 2, 3} using a set method.

first={1,2,3}

result4=first.update({8,9,10})
print(first)

# 16. Remove a random element from the set {1, 2, 3} using a set method.

random_set={1,2,3}
result5=random_set.pop()
print(random_set)

# 17. Check if two sets {1, 2, 3} and {3, 2, 1} are equal.

set1={1,2,3}
set2={3,2,1}
res=set1==set2
print(res)

# 18. From the list [1, 2, 2, 3, 4, 4, 5] , extract only unique values using a set.

lst1=[1, 2, 2, 3, 4, 4, 5]
print(set(lst1))

# 19. Convert the set {1, 2, 3} into a list.

set5={1,2,3}
list5=(list(set5))
print(list5)

# 20. From {1, 2, 3, 4, 5} , remove {2, 4} using a set method.
newset={1,2,3,4,5}
newset.difference_update({2,4})
print(newset)
