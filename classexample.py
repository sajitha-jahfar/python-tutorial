class StudentDetails:
    marks_info={"student1":{
             "maths":68,
             "english":67,
             "language":75},
          "student2":{
             "maths":85,
             "english":80,
            "language":85}}
    def __init__(self,name,mark):
        self.name=name
        self.mark=marks_info
    def avgmarks(marks_info):
        for i in mar

    def marks(self):
        if self.mark>=90:
            print("Grade:A")
        elif self.mark>=70:
            print("grade:B")
        elif self.mark>=50:
            print("grade:C")

        else:
            print("failed") 
    def student_info(self):
        print(f"name:{self.name} mark:{self.mark} ")
student1=StudentDetails("sajitha",80)
student2=StudentDetails("afa",90)
student1.student_info()
student1.marks()
student2.student_info()
student2.marks()

# class Employee:
#     company="softronics"
#     def __init__(self,name,place):
#         self.name=name
#         self.place=place
# # def display_info(self):
# #     print(f"name:{self.name} place:{self.place}")
# emp1=Employee("sajitha","kolathur")
# emp2=Employee("maji","pookkattiri")
# # emp1.display_info()
# print(emp1.company)
# print(emp2.company)
# print(emp1.name)
# print(emp2.name)

#TIGHTLY COUPLED INNER CLASS
# class Employee:
#     class company:
#         def __init__(self,cname,position):
#             self.cname=cname
#             self.position=position
#     def __init__(self,name,age,cname,position):
#         self.name=name
#         self.age=age
#         self.company=Employee.company(cname,position)
        
#     def emp_info(self):
#         print(f"name:{self.name} age:{self.age} cname:{self.company.cname} position:{self.company.position}")

# emp1=Employee("sajitha",27,"softronics","intern")
# emp1.emp_info()

#LOOSLY COUPLED INNER CLASS
# class Employee:
#     class company:
#         def __init__(self,cname,position):
#             self.cname=cname
#             self.position=position
#     def __init__(self,name,age,company):
#         self.name=name
#         self.age=age
#         self.company=Employee.company
        
#     def emp_info(self):
#         print(f"name:{self.name} age:{self.age} cname:{self.company.cname} position:{self.company.position}")
# c1=company("abc","intern")

# emp1=Employee("sajitha",27,c1)
# emp1.emp_info()


#loosly coupled
# class company:
#     def __init__(self,cname,position):
#         self.cname=cname
#         self.position=position
# class Employee:
#     def __init__(self,name,age,company):
#         self.name=name
#         self.age=age
#         self.company=company
#     def emp_info(self):
#         print(f"name:{self.name} age:{self.age} cname:{self.company.cname} position:{self.company.position}")

# c1=company("abc","intern")

# emp2=Employee("sajitha",27,c1)
# emp2.emp_info()
# del emp1
# print(c1.cname)



