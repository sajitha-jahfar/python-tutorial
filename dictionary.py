my_dict={"name":"saji","age":27}#dictionary creation
print(my_dict)

# Using the dict() constructor
another_dict = dict(name="Alice", age=25, city="Los Angeles")
print(another_dict)

#empty dictionary
empty_dict = {}
print(empty_dict) 

#accessing dict items
#Accessing with Brackets:
my_dict = {"name": "John", "age": 30}
print(my_dict["name"]) # Output: John
# Using get(): This method is safer because it returns None if the
#key doesn't exist instead of raising an error.
print(my_dict.get("age")) # Output: 30
print(my_dict.get("salary")) # Output: None

new_dict={
    "person1":{

    "name":"suni",
    "age":45
},
    "person2":{

    "name":"manju",
    "age":34
    }
}
person1_name=new_dict["person1"]["name"]#nested dictionary
print(new_dict["person1"])

new_dict["person2"]["age"]=20 #modifying an element in the dictionary
print(new_dict["person2"])
 
new_dict["person1"]["place"]="kolathur" #adding an element to a dictionary
print(new_dict["person1"])

del new_dict["person1"]["place"]
print(new_dict["person1"]) #removing place from person1

#pop(key): Removes the element with the specified key and
#returns the value. If the key doesn’t exist, it raises a KeyError.
my_dict = {"name": "John", "age": 30, "city": "New York"}
age = my_dict.pop("age")
print(age) # Output: 30
print(my_dict) # Output: {'name': 'John', 'city': 'New York'}

# popitem(): Removes and returns the last inserted key-value pair.
my_dict = {"name": "John", "age": 30}
last_item = my_dict.popitem()
print(last_item) # Output: ('age', 30)


#del statement: Deletes the specified key-value pair.
my_dict = {"name": "John", "age": 30}
del my_dict["age"]
print(my_dict) # Output: {'name': 'John'}


#clear(): Removes all elements from the dictionary.
my_dict.clear()
print(my_dict) # Output: {}

#Copying a Dictionary
# Using copy(): Creates a shallow copy of the dictionary.
original = {"name": "John", "age": 30}
copy_dict = original.copy()
print(copy_dict) # Output: {'name': 'John', 'age': 30}


#Using dict() constructor: Another way to create a shallow copy.
original = {"name": "John", "age": 30}
copy_dict = dict(original)
print(copy_dict) # Output: {'name': 'John', 'age': 30}



#Dictionary Methods
#keys(): Returns a view object that displays a list of all the keys in the dictionary.
my_dict = {"name": "John", "age": 30}
print(my_dict.keys()) # Output: dict_keys(['name', 'age'])

#values(): Returns a view object that displays a list of all the values in the dictionary.
print(my_dict.values()) # Output: dict_values(['John', 30])

#items(): Returns a view object that displays a list of all the keyvalue pairs in the dictionary.
print(my_dict.items()) # Output: dict_items([('name', 'John'),('age', 30)])


#update(): Updates the dictionary with the key-value pairs from another dictionary.
my_dict = {"name": "John", "age": 30}
my_dict.update({"city": "New York", "age": 31})

print(my_dict) # Output: {'name': 'John', 'age': 31, 'city': 'New
York'}

# fromkeys(): Creates a new dictionary from the given sequence of keys with the specified value.
keys = ["name", "age", "city"]
new_dict = dict.fromkeys(keys, "Unknown")
print(new_dict) # Output: {'name': 'Unknown', 'age': 'Unknown','city': 'Unknown'}

#setdefault(key, value): Returns the value of the specified key. If the key doesn’t exist, it inserts the key with the specified value.
my_dict = {"name": "John", "age": 30}

city = my_dict.setdefault("city", "New York")
print(city) # Output: New York
print(my_dict) # Output: {'name': 'John', 'age': 30, 'city': 'NewYork'}





