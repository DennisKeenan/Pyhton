from random import *

print("Welcome to throw the dice project!")
while(True):
    print("_"*37)
    print("Press 1 for single dice")
    print("Press 2 for double dice")
    print("_"*37)
    choices=input()

    if choices=="1":
        print(randint(1,6))

    else:
        print(randint(2,12))
        