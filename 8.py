
# including all variables and methodes

class A:
    name='Sachin'

    def __init__(self,loc,rno):
        self.loc=loc
        self.rno=rno 

    def f1(self):
        print('instant method called')

    def instant():
        print('instant method called')

    @staticmethod 

    def f2():
        print('static method called')

    @classmethod 
    def f3(cls):
        cls.friend='akshay'
        print('class method called')

# Creating object for class
obj=A('mumbai',55)

# Acessing the static variable by using obj and classname
print(A.name)
print(obj.name)

#Accesing the instance variable by using object only
print(obj.rno)
print(obj.loc)

#Accessing the instance method by using obj
obj.f1()
# we can Access instant method by using classname but without using self
A.instant()
# Acess the static method by using classname as well as obj
obj.f2()
A.f2()

# Acess the class method by using obj as well as classname

obj.f3()
A.f3()