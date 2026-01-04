def get_arg(a,*args,**kwargs):
    print("positional arguments:",a) #position arguments
    print("arbitrary arguments:",args) #arbitrary arguments
    print("keyword arguments:",kwargs)#keyword argumements
get_arg(1,2,3,name="anu",age=45)
#priority : position>arbitrary>keyword