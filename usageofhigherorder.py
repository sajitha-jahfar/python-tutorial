def calculate(a,b,operation):
    return operation(a,b)
# def add(a,b):
#     return(a+b)
# def sub(a,b):
#     return(a-b)
# def mult(a,b):
#     return(a*b)
# def div(a,b):
#     return(a/b)

#print(calculate(20,10,add))

#by using lambda 
add=lambda a,b:a+b
print(calculate(20,10,add))