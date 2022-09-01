
# Multiple inheritance 

class C:
    n1=10

class B:
    n2=20

class A(B,C):
    n3=30

    def sum(self):
        print(self.n1+self.n2+self.n3)

obj=A()
obj.sum()

'''
1.the class which derived from more than one base or parent class is known as multiple inherutance.
'''