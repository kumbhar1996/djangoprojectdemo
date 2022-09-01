
# Static methode 

class A:
    name='Sachin'

    @staticmethod

    def f():
        print('f called')

    '''
    def f(self):
        print('f called')
    '''

   
obj=A()
print(obj.name)
print(A.name)

obj.f()
A.f()

'''
1.staticmethod represent by using  @staticmethod Decorator 
2.staticmethod acess by using classname as well as object
3.static method doesnot work with self current class object
'''
