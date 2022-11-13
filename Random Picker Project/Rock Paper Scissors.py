from random import *

# print(random())
# print(randint(1,100))

print("Welcome to rock paper and scissors")
while(True):
    choices=input("Pick your hand!(Rock, Paper or Scissors?)").lower()
    botchoice=randint(1,3)

    if botchoice==1:
        botchoice="rock"

    elif botchoice==2:
        botchoice="paper"

    else:
        botchoice="scissors"
    print(botchoice)

    if choices==botchoice:
        print("Draw")

    if choices=="rock":
        if botchoice=="paper":
            print("Lose") 
        elif botchoice=="scissors":
            print("Win") 

    elif choices=="paper":
        if botchoice=="rock":
            print("Win") 
        elif botchoice=="scissors":
            print("Lose") 

    elif choices=="scissors":
        if botchoice=="rock":
            print("Lose") 
        elif botchoice=="paper":
            print("Win") 

    else:
        print("Invalid Choices")

    exit=input("Do you want to stop? y/n").lower()
    if exit=="y":
        break
