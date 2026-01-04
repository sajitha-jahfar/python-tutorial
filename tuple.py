# a=("saji",) #single element tuple
# print(a)
b=("saji","maji")
b=("afa","saji") #reassign for changing elements

temp_list=list(b)
temp_list[1]="suhara"
b=tuple(temp_list)
print(b)

my_tuple=("car","bike","auto")
(vehicle1,*vehicle2)= my_tuple
print(my_tuple)