from turtle import *
from time import sleep

# Setup turtle
setup(700,700)
speed(0)
bgcolor("Black")
shape("turtle")


# Rectangle Function
def drawrec(length,width,fill):
    pendown()
    if fill:
        begin_fill()
    forward(length)
    right(90)
    forward(width)
    right(90)
    forward(length)
    right(90)
    forward(width)
    if fill:
        end_fill()

# Circle Function
def drawcir(size,fill):
    pendown()
    if fill:
        begin_fill()
    setheading(180)
    circle(size,360)
    if fill:
        end_fill()

# Head Function
def drawhead():
    color("Blue")
    penup()
    goto(0,100)
    drawcir(75,True)
    color("White")
    penup()
    goto(0,72)
    drawcir(60,True)

# Eyes Function
def draweyes():
    color("Black","White")
    penup()
    goto(-15,80)
    drawcir(17,True)
    penup()
    goto(19,80)
    drawcir(17,True)
    color("Black","Black")
    penup()
    goto(-8,70)
    drawcir(6,True)
    penup()
    goto(12,70)
    drawcir(6,True)
    color("White","White")
    penup()
    goto(-8,66)
    drawcir(2,True)
    penup()
    goto(12,66)
    drawcir(2,True)   

# Bell Function
def drawbell():
    color("Yellow")
    penup()
    goto(0,-41)
    drawcir(8,True)
    color("Black")
    penup()
    goto(5,-47)
    drawrec(10,4,False)
    color("Black")
    penup()
    goto(0,-53)
    drawcir(2,True)

# Mouth Function
def drawmouth():
    color("Black")
    penup()
    goto(-30,-20)
    pendown()
    setheading(-27)
    circle(70,55)
    penup()
    goto(0,26)
    pendown()
    goto(0,-25)

# Nose Function
def drawnose():
    color("Red")
    penup()
    goto(0,40)
    drawcir(7,True)

# Hands Function
def drawhand():
    color("Black","White")
    penup()
    goto(-90,-71)
    drawcir(15,True)
    penup()
    goto(90,-71)
    drawcir(15,True)

# Arms Function
def drawarms():
    color("Blue")
    penup()
    begin_fill()
    goto(-35,-50)
    pendown()
    goto(-41,-75)
    left(70)
    goto(-71,-85)
    left(70)
    goto(-86,-70)
    left(70)
    goto(-35,-50)
    end_fill()
    
    penup()
    begin_fill()
    goto(35,-50)
    pendown()
    goto(39,-75)
    left(70)
    goto(74,-85)
    left(70)
    goto(84,-70)
    left(70)
    goto(35,-50)
    end_fill()

# Feet Function
def drawfeet():
    color("Black","White")
    penup()
    goto(-30,-110)
    drawcir(20,True)
    penup()
    goto(30,-110)
    drawcir(20,True)

# Body Function
def drawbody():
    color("Blue")
    penup()
    goto(0,-35)
    drawcir(50,True)
    color("White")
    penup()
    goto(0,-35)
    drawcir(40,True)
    penup()
    goto(15,-127)
    color("Red")
    penup()
    goto(35,-50)
    setheading(180)
    drawrec(70,10,True)

# Whiskers Function:
def drawwhis():
    color("Black")
    penup()
    goto(10,5)
    pendown()
    goto(-40,5)
    penup()
    goto(10,5)
    pendown()
    goto(40,5)
    penup()
    goto(-10,15)
    pendown()
    goto(-40,20)
    penup()
    goto(10,15)
    pendown()
    goto(40,20)
    penup()
    goto(-10,-5)
    pendown()
    goto(-40,-10)
    penup()
    goto(10,-5)
    pendown()
    goto(40,-10)

# Pocket Function
def drawpoc():
    color("Black")
    penup()
    goto(-25,-70)
    pendown()
    setheading(-90)
    circle(25,180)
    goto(-25,-70)
    hideturtle()

drawhead()
drawwhis()
draweyes()
drawmouth()
drawnose()
drawhand()
drawarms()
drawfeet()
drawbody()
drawpoc()
drawbell()
penup()
goto(0,100)
sleep(3)