class B:
    def m1(self):
        print('m1 from B')

class A(B):
    def m2(self):
        print('m2 from A')

obj=A()
obj.m1()
obj.m2()
