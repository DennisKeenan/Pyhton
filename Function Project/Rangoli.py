from turtle import *
from Function import *
from time import sleep
from random import randint

pencolor("red")
speed(0)
counter=0
# for i in range(69):
#     colormode(255)
#     fillcolor(randint(0,255),randint(0,255),randint(0,255))
#     if counter==0:
#         begin_fill()
#     forward(100)
#     left(122)
#     counter+=1
#     if counter==3:
#         end_fill()
#         counter=0

for i in range(23):
    colormode(255)
    color=(randint(0,255),randint(0,255),randint(0,255))
    drawRectangle(color)
    left(15.0)
sleep(5.0)
