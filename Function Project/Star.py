from turtle import *
from time import sleep
from random import randint

x=144
size=120
stars=30
speed(0)
for i in range(stars):
    r=randint(0,255)
    g=randint(0,255)
    b=randint(0,255)
    colormode(255)
    pencolor(r,g,b)
    fillcolor(r,g,b)
    begin_fill()
    for j in range(5):
        forward(5*stars-10*i)
        right(x)
        forward(5*stars-10*i)
        right(72-x)
    end_fill()
    right(13)
    sleep(0.5)