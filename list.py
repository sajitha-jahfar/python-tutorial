#list creation
a=["anu","minu"]
#replace a particular element
a[0]="ninu"
print(a)

# to append an element-append at the end
a.append("ammu")
print(a)
#to insert a new element in aparticular index
a.insert(2,"saji")
print(a)
#to combine two list together
b=[25,36,37]
a.extend(b)
print(a)

#remove()-the the first occurance of an element
f=["apple","banana","orange","banana"]
f.remove("banana")
print(f)

#pop()-to remove a particular element from the list

popped_item=f.pop(1)
print(popped_item)
#del()-to delete a list completely
# del f
print(f)

del f[1] #to delete a particular element
print(f)

#clear-to remove the elemts but not the structure

f.clear()
print(f)


my_list = [1, 2, 3, 2, 4]
print(my_list.count(2)) 

fruits = ['apple', 'banana', 'cherry']
print(fruits.index('banana'))

num1= [1, 2, 3]
num1.reverse()
print(num1)

abc = [3, 1, 2]
abc.sort()
print(abc) 

original_list = [1, 2, 3]
copied_list = original_list.copy()
print(copied_list) 


numbers = [3, 5, 1, 4, 2]
numbers.sort() # Ascending
print(numbers) 
numbers.sort(reverse=True) # Descending
print(numbers) 

original = [3, 1, 4]
sorted_list = sorted(original)
print(sorted_list) # Output: [1, 3, 4]
