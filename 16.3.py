
'''
1.if methods is not found in the chield class then it check in another class
'''

class B:
    def m1(self):
        print('m1 from B')

class A(B):
    def m2(self):
        print('m2 from A')

obj=A()
obj.m1()