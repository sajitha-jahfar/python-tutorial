a="sajitha" #string declaration  #string is immutable
#d='afa'

#string operations
#1.slicing

#print(a[0:5]) #slice
#print(a[::-1]) #reverse
#print(a[-3:-1]) #negative slicing
print(a[0:6:2]) 

#2.string modification

# w="hello world"
# new_w=w.replace("world","python")
# print(new_w)

#3. string case conversion
# e="hello world"
# print(e.upper())
# print(e.lower())

# #4.string concatination

# f="hello"
# n="world"
# result=f+" "+n
# print(result)

# d=["python","is","simple"]
# s=" ".join(d)
# print(s)

#5.formating string

# #1.
# print("my name is %s and %d years old "%("sajitha",27))
# #2.
# print("my name {} and my age is {}".format("saji",25))
# #3.
# a="afa"
# b="22"
# print(f"my name is { a} and my age is { b}")

# #6.string length
v="helloo helloo hii"
print(len(v))

# f="    good  "

# #7.removing whitw space from beginning and end of the string
# print(f.strip())

# #8.to split the string based on a seperator and get the string as a list
print(v.split("o"))

# #9.to get the start index of a particular word
# print(v.find("hello"))

# #10.to check howmany times a substring repeatrd in astring
# print(v.count("helloo"))
# print(v.count("o"))
# #11.startswith()-to check a string is start with a particular substring
# print(v.startswith("he"))

# #12.endswith()-to check a string is start with a particular substring
# print(v.endswith("hii"))


