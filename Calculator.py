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