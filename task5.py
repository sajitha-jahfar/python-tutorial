# # Dictionary QUESTIONS
# # 1. Create a dictionary with keys "name" and "age" and values "Nik" and 20 .

person={"name":"Nik","age":20}

# # 2. Access the value of key "name" from
# # {"name": "Nik", "age": 20} .

person={"name":"Nik","age":20}
print(person["name"])

# # 3. Add a new key "city" with value "Delhi" to
# # {"name": "Nik", "age": 20} .

person={"name":"Nik","age":20}
person["city"]="Delhi"
print(person)

# # 4. Update the value of "age" to 25 in
# # {"name": "Nik", "age": 20} .

person={"name":"Nik","age":20}
person["age"]=25
print(person)

# # 5. Delete the key "age" from
# # {"name": "Nik", "age": 20} .

person={"name":"Nik","age":20}
del person["age"]

# # 6. Check if the key "email" exists in
# # {"name": "Nik", "age": 20} .

person={"name":"Nik","age":20}
print("email" in person)

# 7. Get all keys from
# {"name": "Nik", "age": 20} using a dictionary method.

person={"name":"Nik","age":20}
print(person.keys())

# 8. Get all values from
# {"name": "Nik", "age": 20} using a dictionary method.

person={"name":"Nik","age":20}
print(person.values())

# 9. Convert the dictionary
# {"a": 1, "b": 2} into a list of (key, value) pairs.

dict1={"a": 1, "b": 2} 
dictlist=list(dict1.items())
print(dictlist)

# 10. Create a dictionary from two lists: (use zip method)
# keys = ["name", "age"]
# values = ["Nik", 20] .

keys = ["name", "age"]
values = ["Nik", 20] 
listdict=dict(zip(keys,values))
print(listdict)

# 11. Count how many keys are in
# {"a": 1, "b": 2, "c": 3} .

abc={"a": 1, "b": 2, "c": 3} 
print(len(abc))

# 12. Merge two dictionaries
# {"a": 1} and {"b": 2} into one.

first={"a": 1} 
second={"b": 2} 
merged={**first,**second}
print(merged)

# 13. Clear all elements from
# {"a": 1, "b": 2} using a dictionary method.

data={"a": 1, "b": 2}
data.clear()
print(data)


# 14. Copy the dictionary
# {"x": 10, "y": 20} using a dictionary method.

dict2={"x": 10, "y": 20}
copydict=dict2.copy()
print(copydict)

# 15. Get the value of key "salary" safely from
# {"name": "Nik", "age": 20} without getting an error.

personal= {"name": "Nik", "age": 20}
salary=personal.get("salary")
print(salary)

# 16. From
# {"a": 1, "b": 2, "c": 3} , remove the last inserted item using a dictionary method.

dictdata={"a": 1, "b": 2, "c": 3}
dictdata.popitem()
print(dictdata)

# 17. Given
# student = {"name": "Rahul", "marks": {"math": 90, "science": 85}} ,
# access only the "science" marks.

student = {"name": "Rahul", "marks": {"math": 90, "science": 85}} 
science_score=student["marks"]["science"]
print(science_score)

# 18. From the above student dictionary, update "math" marks to 95 .


student = {"name": "Rahul", "marks": {"math": 90, "science": 85}} 
student["marks"]["math"]=95
print(student)

# 19. Add a new subject "english": 88 inside the "marks" dictionary.

student = {"name": "Rahul", "marks": {"math": 90, "science": 85}} 
student["marks"]["english"]=88
print(student)

# 20. Delete the subject "science" from inside "marks" .

student = {"name": "Rahul", "marks": {"math": 90, "science": 85}} 
del student["marks"]["science"]
print(student)
