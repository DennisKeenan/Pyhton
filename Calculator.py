from cmath import pi
from random import choices
from secrets import choice
from traceback import print_tb


print("Welcome to multi-purpose calculator.")
print("_"*35)
print("Press 1 for addition")
print("Press 2 for subtraction")
print("Press 3 for multiplication")
print("Press 4 for division")
print("Press 5 for division with remainder")
print("Press 6 for exponent")
print("Press 7 for odd-even number")
print("Press 8 for square area")
print("Press 9 for rectangle area")
print("Press 10 for triangle area")
print("Press 11 for circle area")
print("_"*35)
choices=input()

# addition
if choices=="1":
    a=float(input("First Number:"))
    b=float(input("Second Number:"))
    # print(a,"+",b,"=",a+b)
    print("{} + {} = {}".format(a,b,a+b))

# subtraction
elif choices=="2":
    a=float(input("First Number:"))
    b=float(input("Second Number:"))
    print("{} - {} = {}".format(a,b,a-b))

# multiplication
elif choices=="3":
    a=float(input("First Number:"))
    b=float(input("Second Number:"))
    print("{} x {} = {}".format(a,b,a*b))

# division
elif choices=="4":
    a=float(input("First Number:"))
    b=float(input("Second Number:"))
    print("{} : {} = {}".format(a,b,a/b))

# division with remainder
elif choices=="5":
    a=float(input("First Number:"))
    b=float(input("Second Number:"))
    print("{} : {} = {}, with remainder= {}".format(a,b,a//b,a%b))

# exponent
elif choices=="6":
    a=float(input("Number:"))
    b=float(input("Power:"))
    print("{} ^ {} = {}".format(a,b,a**b))

# odd-even checker
elif choices=="7":
    a=int(input("Number:"))
    if a%2==1:
        print(a,"is an odd number")
    else:
        print(a,"is an even number")

# square area
elif choices=="8":
    s=int(input("Side:"))
    print("Area of the square with side:{} is {}".format(s,s*s))

# rectangle area
elif choices=="9":
    l=int(input("Length:"))
    w=int(input("Width:"))
    print("Area of the rectangle with length:{} and width:{} is {}".format(l,w,l*w))

# triangle area
elif choices=="10":
    b=int(input("Base:"))
    h=int(input("Height:"))
    print("Area of the triangle with base:{} and height:{} is {}".format(b,h,b*h/2))

#  circle area
elif choices=="11":
    r=int(input("Radius:"))
    print("Area of the circle with radius:{} is {}".format(r,pi*r*r))