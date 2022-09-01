
# Classmethod

class Player:
    name='Sachin'

    def __init__(self):
        self.runs=2000

    @classmethod 

    def getname(cls):
        print(cls.name)

    
    @classmethod 

    def getruns(cls):
        obj=cls()
        print(obj.runs)
    

obj=Player()
obj.getname()
Player.getruns()

'''
1.classmethod declare by using @classmethod decorator
2.classmethod acess by using object as well as class name 
3.classmethod takes cls as current obj
'''
    
