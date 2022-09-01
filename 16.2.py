
'''
If both methode are same then my child class is exicuted.

here 

1.A is chield class
2.B is parent class
'''

class B:
    def m1(self):
        print('m1 from B')

class A(B):
    def m1(self):
        print('m1 from A')

obj=A()
obj.m1()
