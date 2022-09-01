
# Constructor execution 
'''
1.Chield class Constructor automatically execute after creating object

here chield class is A (chield/derived/sub)
parent class is B    (parent/super/base)
'''

class B:
    n2=20

class A(B):
    n1=10

    def __init__(self):
        print('A class constuctor')

    def sum(self):
        print(self.n1+self.n2)

obj=A()
obj.sum()