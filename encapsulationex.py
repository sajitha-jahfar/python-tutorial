class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary
    def emp_details(self):
        print(f"name:{self.name} salary:{self.__salary}")
    def update_salary(self,new_salary):
        self.__salary=new_salary
e1=Employee("anu",20000)
e1.emp_details()
print(e1.name)


e1.emp_details()
e1.name="afa"
e1.emp_details()
e1.update_salary(30000)