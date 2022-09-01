# Multilevel inheritance

class Grandfather:
    income1=100

class Father(Grandfather):
    income2=20000

class Son(Father):
    income3=50000

    def sum(self):
        print(self.income3+self.income2+self.income1)

obj=Son()
obj.sum()