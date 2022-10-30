from cmath import pi
from random import choices
from secrets import choice
from tkinter import Y
from traceback import print_tb
from unittest import result


print("Welcome to multi-purpose calculator.")
while(True):
    print("_"*37)
    print("Press 1 for basic-operation calculator")
    print("Press 2 for geometric calculator")
    print("Press 3 for bmi calculation")
    print("Press 4 for number converter")
    print("_"*37)
    choices=input()

    # basic-operation calculator
    if choices=="1":
        print("Press 1 for addition")
        print("Press 2 for subtraction")
        print("Press 3 for multiplication")
        print("Press 4 for division")
        print("Press 5 for division with remainder")
        print("Press 6 for exponent")
        print("Press 7 for odd-even checker")
        choices2=input()
        if choices2=="1": # addition
            a=float(input("First Number:"))
            b=float(input("Second Number:"))
            # print(a,"+",b,"=",a+b)
            print("{} + {} = {}".format(a,b,a+b))
        elif choices2=="2": # subtraction
            a=float(input("First Number:"))
            b=float(input("Second Number:"))
            print("{} - {} = {}".format(a,b,a-b))
        elif choices2=="3": # multiplication
            a=float(input("First Number:"))
            b=float(input("Second Number:"))
            print("{} x {} = {}".format(a,b,a*b))
        elif choices2=="4": # division
            a=float(input("First Number:"))
            b=float(input("Second Number:"))
            print("{} : {} = {}".format(a,b,a/b))
        elif choices2=="5": # division with remainder
            a=float(input("First Number:"))
            b=float(input("Second Number:"))
            print("{} : {} = {}, with remainder= {}".format(a,b,a//b,a%b))
        elif choices2=="6": # exponent
            a=float(input("Number:"))
            b=float(input("Power:"))
            print("{} ^ {} = {}".format(a,b,a**b))
        elif choices2=="7": # odd-even checker
            a=int(input("Number:"))
            if a%2==1:
                print(a,"is an odd number")
            else:
                print(a,"is an even number")

    # geomtric calculator
    elif choices=="2":
        print("Press 1 for square area")
        print("Press 2 for rectangle area")
        print("Press 3 for triangle area")
        print("Press 4 for circle area")
        choices2=input()
        if choices2=="1": #square
            s=int(input("Side:"))
            print("Area of the square with side:{} is {}".format(s,s*s))
        elif choices2=="2": #rectangle 
            l=int(input("Length:"))
            w=int(input("Width:"))
            print("Area of the rectangle with length:{} and width:{} is {}".format(l,w,l*w))
        elif choices2=="3": #triangle 
            b=int(input("Base:"))
            h=int(input("Height:"))
            print("Area of the triangle with base:{} and height:{} is {}".format(b,h,b*h/2))
        elif choices2=="4": #circle 
            r=int(input("Radius:"))
            print("Area of the circle with radius:{} is {}".format(r,pi*r*r))

    # bmi calculation
    elif choices=="3":
        bh=int(input("Body Height (kg):"))
        m=int(input("Body Weight (m):"))

    # number converter
    elif choices=="4":
        print("Press 1 for binary to decimal")
        print("Press 2 for decimal to binary")
        choices2=input()
        if choices2=="1": #binary to decimal;
            b=(input("Number:"))[::-1]
            result=0
            index=0
            for i in b:
                if int(i)<0 or int(i)>1:
                    print("Invalid Input") 
                    break
                elif i=="1":
                    result+=2**index
                index+=1
            print("{} in decimal={}".format(b,result))
        elif choices2=="2": #decimal to binary
            l=int(input("Length:"))
            w=int(input("Width:"))
            print("Area of the rectangle with length:{} and width:{} is {}".format(l,w,l*w))

    exit=input("do you want to stop? y/n: ").lower()
    if exit=="y":
        break
