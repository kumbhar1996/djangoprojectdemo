
# Parent class constructor Execution

'''
for parent class constructor execution is also by using parent class also (passing the self argument)
'''
class B:
    n2=20
    def __init__(self):
        print('B class constructor/parent/super/base')

class A(B):
    n1=10
    
    def __init__(self):
        print('A class constructor chield/sub/derived')
        

        B.__init__(self)

    def sum(self):
        print(self.n1+self.n2)

obj=A()
obj.sum()