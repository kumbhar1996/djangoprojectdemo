
# What is the MRO (Method Resolution Order)

# used for check the path 

class B:
    def m1(self):
        print('m1 from B')

class A(B):
    def m2(self):
        print('m2 from A')

obj=A()
obj.m1()


print(A.mro())
