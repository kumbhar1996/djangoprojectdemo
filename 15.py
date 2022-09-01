
# Multiple inheritance


class Grandfather:
    income1=500

class Father:
    income2=30000


class Son(Father,Grandfather):
    income3=50000


    def sum(self):
        print(self.income3+self.income2+self.income1)

obj=Son()
obj.sum()
