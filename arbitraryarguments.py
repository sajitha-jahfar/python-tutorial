def sum_arguments(*arg):
    total=0
    
    for i in arg:
        total+=i
    return total
    
print(sum_arguments(1,2,3,55,6,7))