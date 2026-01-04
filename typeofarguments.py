#1.position arguments
# def greet(name,age):
#     print(f"my name is {name} and my age is {age}")
# greet("saji",27)

#default argument

# def greet(name="saji",age=27):
#     print(f"my name is {name} and my age is {age}")
# greet()
#keyword arguments
# def greet(name,age):
#     print(f"my name is {name} and my age is {age}")
# greet(age=27,name="saji")
#docstring argument
def greet():
      """this is a docstring"""
    # print(f"my name is{name}")
  
print(greet.__doc__)