# Single Inheritance

class Father:
    income=2000

class Son(Father):
    income1=50000

    def sum(self):
        print(self.income+self.income1)

obj=Son()
obj.sum()
