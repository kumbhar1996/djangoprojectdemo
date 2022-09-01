
# instant method 

class Add:
    n1=10
    n2=20
    
    def sum(self):
        print(self.n1+self.n2)

    def sum2(self,x,y):
        print(x+y)

obj=Add()
obj.sum()
obj.sum2(100,200)



'''
1.the methode declare inside the class without any decorator 
2.it takes self is current class argument 
3.instant methode access by using obj
4.instant methode can not acess by using class name if method contain self
'''

