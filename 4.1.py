# Instant method calling by using class name but it can not take self as an current object
class A:
    def f():
        print('f called')

obj=A()
A.f()

'''
1.method f not containing any self argument
'''