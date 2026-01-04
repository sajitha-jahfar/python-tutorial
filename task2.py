# 1. Create a tuple (1,2,3,4) and access the element 3 using indexing.

my_tuple=(1,2,3,4)
print(my_tuple[2])

# 2. Convert the tuple (10,20,30) into a list 
tuple1=(10,20,30)
list1=list(tuple1)

print(type(list1))

# 3. Convert the list [1,2,3] into a tuple.
list_new=[1,2,3]
tuple_new=tuple(list_new)
print(type(tuple_new))

# 4. From the tuple ("a","b","c","d") , extract ("b","c") using slicing
a=("a","b","c","d")
b= a[1:3]
print(b)

# 5. Check if "x" exists inside the tuple ("x","y","z") .
n=("x","y","z")
m="x" in n
print(m)

# 6. Given (5,3,9,1) , find the maximum value using a tuple function.
given_tuple=(5,3,9,1)
v=max(given_tuple)
print(v)

# 7. Given (1,2,3) , create a new tuple (1,2,3,1,2,3) using tuple operations only.
p=(1,2,3)
p=p+p
print(p)

#8. Count how many times 2 appears in (1,2,2,3,2) using a tuple method.
pq=(1,2,2,3,2)  
print(pq.count(2))

#9. Find the index of "cat" in ("dog","cat","mouse") .
animals=("dog","cat","mouse")
print(animals.index("cat"))

#10. Reverse (1,2,3,4,5) using slicing.
ab=(1,2,3,4,5)
print(ab[::-1])
 
#11. Combine (1,2) and (3,4) into (1,2,3,4) using tuple operations.
ij=(1,2)
jk=(3,4)
ik=ij+jk
print(ik)

#12. Convert "hello" into a tuple of characters.
t=tuple("hello")
print(t)

#13. Convert (1,2,3,4) into the list [1,4] by extracting only first & last elements.
abc=(1,2,3,4)
lst=[abc[0],abc[-1]]
print(lst)

#14. Given a tuple (10,20,30,40) , replace the value 30 with 99 (hint: convert to list→ modify → convert back).

tpl=(10,20,30,40)
lst1=list(tpl)
lst1[2]=99
tpl=tuple(lst1)
print(tpl)

#15. Using unpacking, extract a=1 , b=2 , c=3 from (1,2,3) .
tpl2=(1,2,3)
(a,b,c)=tpl2
print(a,b,c)

#16. Create a nested tuple: turn (1,2,3) into ((1,2,3),) .
tpl3=(1,2,3)
ntpl=((tpl3),)
print(ntpl)

#17. Merge ("a","b") with ["c","d"] to get a single tuple ("a","b","c","d") 
tpl4=("a","b")
lst5=["c","d"]
lst6=list(tpl4)
merge=lst6+lst5
tpl7=tuple(merge)
print(tpl7)

#18. Check if tuple (1,2,3) is equal to its reverse.
tpl9=(1,2,3)
rev=tpl9[::-1]
res=tpl9==rev
print(res)

#19. Convert a tuple of lists ([1,2],[3,4]) into a single flat list [1,2,3,4] .
tuplist=([1,2],[3,4])
newlst=list(tuplist)
lstnew=newlst[0]+newlst[1]
print(lstnew)

#20. Given (1, [2,3], 4) , add 5 inside the inner list so result becomes (1, [2,3,5], 4) .
tuplist1=(1,[2,3],4)
newlst1=list(tuplist1)
newlst1[1].append(5)
tuplist1=tuple(newlst1)
print(tuplist1)

















