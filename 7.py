
# Creating and Accessing the varibles with methode

class bus:
    fw=2
    bw=4

    def totalwheels(self):
        print(self.fw+self.bw)

obj=bus()
obj.totalwheels()

print()
#static variable acess by using object name
print(obj.fw)
print(obj.bw)
# Static variable acessing by using classname
print()

print(bus.fw)
print(bus.bw)