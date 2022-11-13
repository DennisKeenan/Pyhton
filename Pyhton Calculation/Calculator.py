from math import *

print("Welcome to multi-purpose calculator.")
while(True):
    print("_"*37)
    print("Press 1 for basic-operation calculator")
    print("Press 2 for geometric area calculator")
    print("Press 3 for geometric volume calculator ")
    print("Press 4 for bmi calculation")
    print("Press 5 for number converter")
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
        print("Press 7 for square-root")
        print("Press 8 for factorial")
        print("Press 9 for odd-even checker")
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
        elif choices2=="7": #square-root
            a=float(input("Number:"))
            print("sqrt({})={}".format(a,sqrt(a)))
        elif choices2=="8": #factorial
            a=int(input("Number:"))
            print("{}!={}".format(a,factorial(a)))
        elif choices2=="9": # odd-even checker
            a=int(input("Number:"))
            if a%2==1:
                print(a,"is an odd number")
            else:
                print(a,"is an even number")

    # geomtric area calculator 
    elif choices=="2":
        print("Press 1 for square area")
        print("Press 2 for rectangle area")
        print("Press 3 for triangle area")
        print("Press 4 for circle area")
        print("Press 5 for trapesium area")
        print("Press 6 for kite area")
        print("Press 7 for rhombus area")
        print("Press 8 for parallelogram area")
        choices2=input()
        if choices2=="1": #square
            s=float(input("Side:"))
            print("Area of the square with side:{} is {}".format(s,s*s))
        elif choices2=="2": #rectangle 
            l=float(input("Length:"))
            w=float(input("Width:"))
            print("Area of the rectangle with length:{} and width:{} is {}".format(l,w,l*w))
        elif choices2=="3": #triangle 
            b=float(input("Base:"))
            h=float(input("Height:"))
            print("Area of the triangle with base:{} and height:{} is {}".format(b,h,b*h/2))
        elif choices2=="4": #circle 
            r=int(input("Radius:"))
            print("Area of the circle with radius:{} is {}".format(r,pi*r*r))
        elif choices2=="5": #trapesium 
            b=float(input("Base:"))
            t=float(input("Top:"))
            h=float(input("Height:"))
            print("Area of the trapesium with base:{}, top:{}, and height:{} is {}".format(b,t,h,(b+t)*h/2))
        elif choices2=="6": #kite 
            d1=float(input("Diagonal 1:"))
            d2=float(input("Diagonal 2:"))
            print("Area of the trapesium with diagonal 1:{} and diagonal 2:{} is {}".format(d1,d2,d1*d2/2))
        elif choices2=="7": #rhombus
            d1=float(input("Diagonal 1:"))
            d2=float(input("Diagonal 2:"))
            print("Area of the trapesium with diagonal 1:{} and diagonal 2:{} is {}".format(d1,d2,d1*d2/2))
        elif choices2=="8": #parallelogram
            b=float(input("Base:"))
            h=float(input("Height:"))
            print("Area of the trapesium with base:{} and height:{} is {}".format(b,h,b*h))

    #geometric volume calculator
    elif choices=="3":
        print("Press 1 for cube volume")
        print("Press 2 for cuboid volume")
        choices2=input()
        if choices2=="1": #cube
            s=float(input("Side:"))
            print("Volume of the cube with side:{} is {}".format(s,s*s*s)) 
        elif choices2=="2": #cube
            l=float(input("Length:"))
            w=float(input("Width:"))
            h=float(input("Height:"))
            print("Volume of the cuboid with length:{}, width:{}, and height:{} is {}".format(l,w,h,l*w*h))        
        
    # bmi calculation
    elif choices=="4":
        bh=int(input("Body Height (kg):"))
        m=int(input("Body Weight (m):"))

    # number converter
    elif choices=="5":
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
