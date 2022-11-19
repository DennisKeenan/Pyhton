from random import *

print("welcome to guessing the number game!")
botchoice=randint(1,100)
choice=int(input("Please choose a number between 1-100!"))

while(True):
    if choice==botchoice:
        print("Yay, you win!!!")
        break

    if choice!=botchoice:
        choice=int(input("Please enter the number again!"))
