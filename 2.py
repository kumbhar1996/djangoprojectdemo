# instant variable

class Student:
    # Static variable
    school='public school'

    def __init__(self,name,loc,rno):
        # instant variable 
        self.name=name
        self.loc=loc
        self.rno=rno

obj=Student('sachin','mumbai',55)
print(obj.name)
print(obj.loc)
print(obj.rno)

#print(Student.name)   instant variable can not acess by using class name

'''
1.instant variable declare inside the constructor only
2.instant variable acess by using object only
4.Instant variable can not acess by using calss name 
'''