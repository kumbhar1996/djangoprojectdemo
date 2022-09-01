
# Single inheritance 
class B:
    n1=10
    def f1(self):
        print('f1 called')

class A(B):
    n2=20
    def f2(self):
        print('f2 called')

obj=A()
obj.f1()
obj.f2()

'''
1.A class inherits the all properties from or methods from another class.
2.Inheritance is a process by which genetic information from parents to chiield.
3.A derived class is derived from single parent class.
'''

class B:
    n2=20

class A(B):
    n1=10

    def sum(self):
        print(self.n1+self.n2)

obj=A()
obj.sum()
