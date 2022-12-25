from turtle import *
from time import sleep

bgcolor("Black")
pencolor("White")
for i in range (2):
    for j in range(9):
        forward(50)
        right(40)
    penup()
    left(180)
    forward(150)
    right(180)
    pendown()
    for j in range(9):
        forward(50)
        right(40)
    penup()
    left(180)
    forward(150)
    right(180)
    pendown()
sleep(3.0)