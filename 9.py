class Arth:
    n1=10
    
    def __init__(self,n2):
        self.n2=n2
    
    def add(self):
        print(self.n1+self.n2)

    @staticmethod 

    def sub():
        n2=100
        print(Arth.n1-n2)

    @classmethod 

    def div(cls):
        obj=cls(20)

        print(obj.n1+obj.n2)

obj=Arth()
obj.add()
Arth.sub()
Arth.div()