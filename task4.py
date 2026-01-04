#1. Create a dictionary with keys "name" and "age" and values "Nik" and 20 .
my_dict={
    "name":"Nik",
    "age":20
}
print(my_dict)

#2. Access the value of key "name" from {"name": "Nik", "age": 20} .
print(my_dict["name"])

#3. Add a new key "city" with value "Delhi" to {"name": "Nik", "age": 20} .
my_dict["city"]="Delhi"
print(my_dict)

#4. Update the value of "age" to 25 in {"name": "Nik", "age": 20} .
my_dict["age"]=25
print(my_dict)

#5. Delete the key "age" from {"name": "Nik", "age": 20} .
my_dict.pop("age")
print(my_dict)

#6. Check if the key "email" exists in {"name": "Nik", "age": 20} .

new_dict={
    "name": "Nik",
     "age": 20
     } 
a="email" in new_dict
print(a)

#7. Get all keys from {"name": "Nik", "age": 20} using a dictionary method.
print(new_dict.keys())

#8. Get all values from {"name": "Nik", "age": 20} using a dictionary method.
print(new_dict.values())

#9. Convert the dictionary {"a": 1, "b": 2} into a list of (key, value) pairs.
letters={
    "a":1,
    "b":2
}
print(letters.items())

#10. Create a dictionary from two lists: (use zip method) keys = ["name", "age"] values = ["Nik", 20] .
keys=["name", "age"] 
values=["Nik", 20] 
zip_=dict(zip(keys,values))
print(zip_)

#11. Count how many keys are in {"a": 1, "b": 2, "c": 3} .
f={
    "a":1,
    "b":2,
    "c":3
}
count=len(f)
print(count)

#12. Merge two dictionaries {"a": 1} and {"b": 2} into one.
s={"a":1}
p={"b":2}

new_zip=dict(zip(s,p))
print(new_zip)











