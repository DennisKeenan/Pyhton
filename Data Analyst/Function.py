import numpy as np
 
x1=np.random.randint(1,10,size=10) 
x2=np.random.randint(1,10,size=(10,7)) #2 Dimension
x3=np.random.randint(1,10,size=(10,4,3)) #3 Dimension
# print(x1)
# print(x2)
# print(x3)

list_A=[2,3,4,9,6]
array_A=np.array(list_A)
print(list_A)
print(array_A)

array_0s=np.zeros(100)
print(array_0s)

array_1s=np.ones((100,10))
print(array_1s)

array_range=np.arange(31)
print(array_range)

array_range_step=np.arange(3,25,1.5)
print(array_range_step)

array_linspace=np.linspace(3,275,27)
print(array_linspace)

array_linspace_smallnumber=np.linspace(0,10,5)
print(array_linspace_smallnumber)