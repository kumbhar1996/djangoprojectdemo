
l1=[10,20,30,40,50]
print('before copy ')
print(l1)

l2=l1

print('after copy')
print(l1)
print(l2)
print(id(l1))
print(id(l2))

# By using importing method copy
import copy 

l1=[100,200,300,400,500]

l2=copy.copy(l1)
print('After copy')
print(l1)
print(l2)
print(id(l1))
print(id(l2))
