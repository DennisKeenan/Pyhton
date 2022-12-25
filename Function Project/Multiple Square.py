from turtle import *
from time import sleep

bgcolor("Black")
pencolor("White")
for i in range (2):
    for j in range(4):
        forward(100)
        right(90)
    penup()
    left(90)
    forward(120)
    right(90)
    pendown()
    for j in range(4):
        forward(100)
        right(90)
    penup()
    left(90)
    forward(120)
    right(90)
    pendown()
sleep(3.0)