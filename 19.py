
# Parent class constructor Execution
'''
for parent class constructor execution supermethode is used
'''
class B:
    n2=20
    def __init__(self):
        print('B class constructor/parent/super/base')

class A(B):
    n1=10
    def __init__(self):
        print('A class constructor chield/sub/derived')

        super().__init__()

    def sum(self):
        print(self.n1+self.n2)

obj=A()
obj.sum()