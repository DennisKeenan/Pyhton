from turtle import *
from time import sleep

# def drawCircle(quality:int=4,color="black",size:int=10):
#     speed(0)
#     fillcolor(color)
#     begin_fill()
#     for i in range(int(360/quality)):
#         forward(size)
#         left(quality)
#     end_fill()
#     sleep(3)

# def drawRectangle(color="maroon",length=50,width=70):
#     speed(1)
#     fillcolor(color)
#     begin_fill()
#     forward(width)
#     right(90)
#     forward(length)
#     right(90)
#     forward(width)
#     right(90)
#     forward(length)
#     right(90)
#     end_fill()
#     sleep(5)
#     return mul(length,width)

# def add(numberA,numberB):
#     return numberA+numberB

# def sub(numberA,numberB):
#     return numberA-numberB

# def mul(numberA,numberB):
#     return numberA*numberB

# def div(numberA,numberB):
#     return numberA/numberB

# def factorial(numberA):
#     result=1
#     for i in range(2,numberA+1):
#         result=mul(result,i)
#     return result

def funcname(*argument):
    global varname
    varname="something"
    print(argument)
    
funcname()
print(varname)

div=lambda a,b: a/b
print(div(2,4))

numbers=[2,6,8,10,11,4,12,7,13,17,0,3,21]
mapnumbers=list(map(lambda num: num%2, numbers))
# print(mapnumbers)
oddeven=lambda num: num%2
Listnum=[]
for i in numbers:
    Listnum.append(oddeven(i))
print(Listnum)