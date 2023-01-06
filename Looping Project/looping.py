from secrets import choice
from tkinter.messagebox import YES


for i in "hello world":
    print(i)

i=0
while(True):
   choice=input("do you want to stop? ").lower()
   if choice=="yes":
    break
